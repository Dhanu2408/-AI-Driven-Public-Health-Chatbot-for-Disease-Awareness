from flask import Flask, render_template, request, redirect, session, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3
import re
import datetime
import io

app = Flask(__name__)
app.secret_key = "healthbot_secret_key"

DB_NAME = "healthbot.db"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
MOBILE_REGEX = r"^[6-9]\d{9}$"


def db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                mobile TEXT,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Migration safeguard: if an older healthbot.db already exists without
        # the mobile column, add it without touching existing user data.
        existing_cols = [r["name"] for r in conn.execute("PRAGMA table_info(users)").fetchall()]
        if "mobile" not in existing_cols:
            conn.execute("ALTER TABLE users ADD COLUMN mobile TEXT")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS chat_history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                reply TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS login_activity(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                login_time TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS feedback(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                chat_id INTEGER,
                name TEXT,
                email TEXT,
                rating TEXT NOT NULL,
                comment TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        fb_cols = [r["name"] for r in conn.execute("PRAGMA table_info(feedback)").fetchall()]
        if "name" not in fb_cols:
            conn.execute("ALTER TABLE feedback ADD COLUMN name TEXT")
        if "email" not in fb_cols:
            conn.execute("ALTER TABLE feedback ADD COLUMN email TEXT")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS profile(
                user_id INTEGER PRIMARY KEY,
                age INTEGER,
                gender TEXT,
                blood_group TEXT,
                weight REAL,
                height REAL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)


init_db()


# ---------------- DAILY HEALTH TIPS ----------------
TIPS = [
    "Sit for long hours? Stand up and stretch for 2 minutes every hour — it improves circulation and eases back strain.",
    "Aim for 7-8 hours of sleep. Consistent sleep timing matters as much as the total hours.",
    "Wash your hands for at least 20 seconds — it's still one of the simplest ways to avoid infections.",
    "Add one extra vegetable to your plate today. Small changes add up over time.",
    "Screen time before bed can delay sleep. Try dimming lights an hour before you sleep.",
    "Drink a glass of water first thing in the morning to kickstart your metabolism.",
    "Take the stairs instead of the lift when you can — small activity bursts count too.",
]


def get_daily_tip():
    day_index = datetime.date.today().timetuple().tm_yday
    return TIPS[day_index % len(TIPS)]


# ---------------- DAILY PROGRESS TRACKING (water / movement / meds) ----------------
PROGRESS_LIMITS = {"water": 8, "move": 20, "meds": 2}
PROGRESS_STEP = {"water": 1, "move": 5, "meds": 1}


def get_progress():
    today_str = datetime.date.today().isoformat()
    if session.get("progress_date") != today_str:
        session["progress_date"] = today_str
        session["progress"] = {"water": 0, "move": 0, "meds": 0}
        session.modified = True
    return session["progress"]


# ---------------- LOGIN STREAK ----------------
def compute_streak(user_id):
    with db() as conn:
        rows = conn.execute(
            "SELECT DISTINCT date(login_time) as d FROM login_activity WHERE user_id=? ORDER BY d DESC",
            (user_id,),
        ).fetchall()

    dates = [r["d"] for r in rows]
    streak = 0
    today = datetime.date.today()
    for i, d in enumerate(dates):
        expected = today - datetime.timedelta(days=i)
        if d == expected.isoformat():
            streak += 1
        else:
            break
    return streak


# ---------------- VALIDATION ----------------
def validate_registration(name, email, mobile, password, confirm_password):
    if not name or len(name.strip()) < 2:
        return "Name must be at least 2 characters."
    if not email or not re.match(EMAIL_REGEX, email):
        return "Please enter a valid email address."
    if not mobile or not re.match(MOBILE_REGEX, mobile):
        return "Please enter a valid 10-digit mobile number."
    if not password or len(password) < 6:
        return "Password must be at least 6 characters."
    if not re.search(r"[A-Za-z]", password) or not re.search(r"[0-9]", password):
        return "Password must contain both letters and numbers."
    if password != confirm_password:
        return "Password and Confirm Password do not match."
    return None


# ---------------- FOLLOW-UP QUESTIONS ----------------
SYMPTOM_QUESTIONS = {
    "fever": ["age", "temperature", "days"],
    "cold": ["age", "days"],
    "cough": ["age", "cough_type", "days"],
    "dengue": ["age", "days"],
    "headache": ["age", "days"],
    "vomiting": ["age", "days"],
    "diarrhea": ["age", "days"],
    "body pain": ["age", "days"],
    "diabetes": ["age", "days"],
    "blood pressure": ["age", "days"],
    "malaria": ["age", "days"],
    "typhoid": ["age", "days"],
    "asthma": ["age", "days"],
    "covid-19": ["age", "days"],
    "allergy": ["age", "days"],
    "food poisoning": ["age", "days"],
    "migraine": ["age", "days"],
}

QUESTION_TEXT = {
    "age": "Got it. What is your age?",
    "temperature": "What is your body temperature (in °F), if you've measured it?",
    "cough_type": "Is your cough dry, or is it with mucus (wet cough)?",
    "days": "How many days have you had this symptom?",
}


def detect_symptom(msg):
    msg = msg.lower()
    if "fever" in msg:
        return "fever"
    if "cold" in msg:
        return "cold"
    if "cough" in msg:
        return "cough"
    if "dengue" in msg:
        return "dengue"
    if "headache" in msg:
        return "headache"
    if "vomit" in msg:
        return "vomiting"
    if "diarrhea" in msg or "loose motion" in msg:
        return "diarrhea"
    if "body pain" in msg or "bodyache" in msg:
        return "body pain"
    if "diabet" in msg or "sugar" in msg:
        return "diabetes"
    if "blood pressure" in msg or "hypertension" in msg or " bp" in msg or msg.strip() == "bp":
        return "blood pressure"
    if "malaria" in msg:
        return "malaria"
    if "typhoid" in msg:
        return "typhoid"
    if "asthma" in msg or "breathless" in msg or "wheez" in msg:
        return "asthma"
    if "covid" in msg or "corona" in msg:
        return "covid-19"
    if "allerg" in msg:
        return "allergy"
    if "food poison" in msg:
        return "food poisoning"
    if "migraine" in msg:
        return "migraine"
    return None


def build_summary(symptom, answers):
    bits = []
    if "age" in answers:
        bits.append(f"Age: {answers['age']}")
    if "temperature" in answers:
        bits.append(f"Temperature: {answers['temperature']}")
    if "cough_type" in answers:
        bits.append(f"Cough type: {answers['cough_type']}")
    if "days" in answers:
        bits.append(f"Duration: {answers['days']}")

    summary = "📋 Thanks! Based on what you shared — " + ", ".join(bits) + ".\n\n"

    digits = "".join(ch for ch in answers.get("days", "") if ch.isdigit())
    if digits and int(digits) >= 3:
        summary += "⚠️ Since this has lasted a few days already, please consider seeing a doctor if there's no improvement.\n\n"

    return summary


DISCLAIMER = (
    "\n\nThese are common over-the-counter medicines that are often used for these symptoms. "
    "Always follow the label instructions and consult a healthcare professional before taking "
    "any medicine, especially if symptoms are severe, persistent, or you have other medical conditions."
)


# ---------------- CHAT LOGIC ----------------
def get_reply(msg, name=""):
    msg = msg.lower()

    if "thank" in msg or "thanks" in msg or "tq" in msg:
        greet = f", {name}" if name else ""
        return f"You're welcome{greet}! Take care and don't hesitate to ask if you have more questions. Get well soon!"

    if "fever" in msg:
        return (
            "🌡️ Fever\n"
            "Fever is your body's natural response to fighting infection — usually a virus or bacteria.\n\n"
            "Home remedies:\n"
            "1. Drink plenty of fluids (water, ORS, coconut water) to avoid dehydration.\n"
            "2. Rest as much as possible — don't overexert yourself.\n"
            "3. Use a lukewarm sponge/cloth on your forehead to help cool down.\n"
            "4. Monitor your temperature every few hours.\n\n"
            "Common OTC medicine: Paracetamol (Crocin, Dolo 650) — helps reduce fever and body ache."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: fever is above 103°F (39.4°C), lasts more than 2-3 days, "
            "or comes with rash, breathing trouble, severe headache, or vomiting."
        )

    elif "cold" in msg:
        return (
            "🤧 Common Cold\n"
            "A viral infection of the nose and throat, usually mild and clears up on its own.\n\n"
            "Home remedies:\n"
            "1. Steam inhalation 2-3 times a day helps clear congestion.\n"
            "2. Drink warm fluids like soup or herbal tea.\n"
            "3. Avoid cold drinks and cold weather exposure.\n"
            "4. Get adequate rest and sleep.\n\n"
            "Common OTC medicine: Cetirizine (antihistamine) for runny nose/sneezing, "
            "or a combination cold tablet (e.g. Sinarest, Cetzine)."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: symptoms last more than 10 days or worsen with high fever."
        )

    elif "cough" in msg:
        return (
            "😷 Cough\n"
            "Can be caused by infection, allergies, or irritation in the throat/airways.\n\n"
            "Home remedies:\n"
            "1. Warm water with honey soothes the throat.\n"
            "2. Stay hydrated and avoid cold or fried foods.\n"
            "3. Avoid smoke, dust, and strong smells.\n"
            "4. Use a humidifier if the air is dry.\n\n"
            "Common OTC medicine: Cough syrup with dextromethorphan (dry cough) or an expectorant like "
            "guaifenesin (wet/productive cough) — e.g. Benadryl, Ascoril."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: cough persists beyond a week, or you cough up blood or thick colored mucus."
        )

    elif "dengue" in msg:
        return (
            "🦟 Dengue\n"
            "A mosquito-borne viral infection, usually causing high fever, body pain, and low platelet count.\n\n"
            "What to do:\n"
            "1. Go to a hospital immediately for a blood test (platelet count).\n"
            "2. Drink plenty of fluids — ORS, coconut water, fruit juice.\n"
            "3. Rest completely and monitor for warning signs.\n\n"
            "Medicine caution: Only Paracetamol is safe for fever/pain. "
            "Do NOT take aspirin or ibuprofen — they increase bleeding risk."
            f"{DISCLAIMER}\n\n"
            "Go to hospital urgently if: severe abdominal pain, bleeding gums, persistent vomiting, or extreme fatigue."
        )

    elif "headache" in msg:
        return (
            "🤕 Headache\n"
            "Often caused by stress, dehydration, lack of sleep, or eye strain.\n\n"
            "Home remedies:\n"
            "1. Rest in a quiet, dark room.\n"
            "2. Drink water — dehydration is a common trigger.\n"
            "3. Gently massage your temples/neck.\n"
            "4. Limit screen time and take breaks.\n\n"
            "Common OTC medicine: Paracetamol (Crocin, Dolo 650) for mild headaches."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: headache is sudden and severe, frequent, or comes with vision changes or vomiting."
        )

    elif "vomit" in msg or "vomiting" in msg:
        return (
            "🤢 Vomiting\n"
            "Can result from food poisoning, infection, motion sickness, or digestive issues.\n\n"
            "Home remedies:\n"
            "1. Sip small amounts of water or ORS frequently.\n"
            "2. Avoid solid food until vomiting settles, then eat bland food (rice, banana, toast).\n"
            "3. Rest and avoid strong smells.\n\n"
            "Common OTC medicine: Domperidone or Ondansetron (anti-nausea) — commonly used, "
            "but best taken after pharmacist/doctor advice."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: vomiting continues beyond 24 hours, or with blood, high fever, or severe pain."
        )

    elif "diarrhea" in msg or "loose motion" in msg:
        return (
            "🚽 Diarrhea\n"
            "Usually caused by infection, contaminated food/water, or digestive upset.\n\n"
            "Home remedies:\n"
            "1. Drink ORS solution to prevent dehydration.\n"
            "2. Eat light, easily digestible food (rice, curd, banana).\n"
            "3. Avoid oily, spicy, or dairy-heavy food.\n"
            "4. Wash hands frequently to prevent spread.\n\n"
            "Common OTC medicine: ORS packets are the priority. Loperamide may help short-term, "
            "but avoid it if there's fever or blood in stool."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: it lasts more than 2 days, or with blood, high fever, or signs of dehydration."
        )

    elif "body pain" in msg or "bodyache" in msg:
        return (
            "💪 Body Pain\n"
            "Often linked to viral infections, fatigue, dehydration, or overexertion.\n\n"
            "Home remedies:\n"
            "1. Rest and avoid strenuous activity.\n"
            "2. Stay hydrated.\n"
            "3. A warm water bath can help ease muscle pain.\n\n"
            "Common OTC medicine: Paracetamol (Crocin, Dolo 650) for pain relief."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: pain is severe, localized with swelling, or accompanied by high fever."
        )

    elif "diabet" in msg or "sugar" in msg:
        return (
            "🍬 Diabetes\n"
            "A long-term condition where the body cannot properly regulate blood sugar levels.\n\n"
            "Home care & lifestyle:\n"
            "1. Monitor blood sugar regularly as advised by your doctor.\n"
            "2. Eat a balanced diet low in refined sugar and processed carbs.\n"
            "3. Stay active — at least 30 minutes of walking most days.\n"
            "4. Take prescribed medication/insulin exactly as directed.\n\n"
            "Note: Diabetes medicines must be doctor-prescribed and monitored — there is no safe "
            "generic OTC option for blood sugar control."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: blood sugar is very high/low, or you notice excessive thirst, frequent "
            "urination, fatigue, blurred vision, or slow-healing wounds."
        )

    elif "blood pressure" in msg or "hypertension" in msg or "bp" in msg:
        return (
            "🩺 Blood Pressure (Hypertension)\n"
            "A condition where the force of blood against artery walls stays consistently high.\n\n"
            "Home care & lifestyle:\n"
            "1. Reduce salt intake and avoid processed/packaged foods.\n"
            "2. Exercise regularly and maintain a healthy weight.\n"
            "3. Manage stress through relaxation, sleep, and breathing exercises.\n"
            "4. Limit alcohol and avoid smoking.\n\n"
            "Note: Blood pressure medicines must be doctor-prescribed based on your readings — "
            "self-medicating can be dangerous."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: reading is above 180/120, or with chest pain, severe headache, "
            "vision problems, or shortness of breath — this needs urgent care."
        )

    elif "malaria" in msg:
        return (
            "🦟 Malaria\n"
            "A mosquito-borne disease causing high fever with chills, sweating, and body pain in cycles.\n\n"
            "What to do:\n"
            "1. Get a blood test (malaria smear/rapid test) as soon as possible.\n"
            "2. Rest and drink plenty of fluids.\n"
            "3. Use mosquito nets/repellents to avoid spreading further.\n\n"
            "Common OTC medicine: Paracetamol for fever. Antimalarial drugs "
            "(e.g. chloroquine, ACT) must only be taken as prescribed after diagnosis."
            f"{DISCLAIMER}\n\n"
            "See a doctor urgently if: fever comes in cycles with chills/sweating, or with "
            "confusion, severe weakness, or jaundice."
        )

    elif "typhoid" in msg:
        return (
            "🦠 Typhoid\n"
            "A bacterial infection spread through contaminated food/water, causing prolonged fever.\n\n"
            "Home care:\n"
            "1. Drink only boiled/purified water.\n"
            "2. Eat soft, easily digestible food.\n"
            "3. Rest completely and monitor temperature.\n\n"
            "Note: Typhoid requires a doctor-prescribed course of antibiotics — it should not be "
            "self-treated with OTC medicine alone."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: fever persists beyond 3 days, especially if it rises in the evening, "
            "or with stomach pain, weakness, or rash."
        )

    elif "asthma" in msg or "breathless" in msg or "wheez" in msg:
        return (
            "🌬️ Asthma\n"
            "A chronic condition causing airway inflammation, wheezing, and breathlessness.\n\n"
            "Home care & lifestyle:\n"
            "1. Avoid known triggers — dust, smoke, cold air, strong odours.\n"
            "2. Keep your prescribed inhaler accessible at all times.\n"
            "3. Practice breathing exercises and avoid strenuous exertion during flare-ups.\n\n"
            "Note: Inhalers/bronchodilators must be prescribed by a doctor based on severity."
            f"{DISCLAIMER}\n\n"
            "See a doctor urgently if: breathlessness is severe, lips/fingertips turn bluish, "
            "or the inhaler isn't providing relief."
        )

    elif "covid" in msg or "corona" in msg:
        return (
            "🦠 COVID-19\n"
            "A viral respiratory infection that can range from mild cold-like symptoms to severe illness.\n\n"
            "Home care:\n"
            "1. Isolate yourself to avoid spreading it to others.\n"
            "2. Rest, stay hydrated, and monitor oxygen levels (SpO2) if possible.\n"
            "3. Take paracetamol for fever/body ache as needed.\n\n"
            "Common OTC medicine: Paracetamol for fever and body pain."
            f"{DISCLAIMER}\n\n"
            "See a doctor urgently if: breathing difficulty, oxygen level drops below 94%, "
            "chest pain, or confusion."
        )

    elif "allerg" in msg:
        return (
            "🤧 Allergy\n"
            "An overreaction of the immune system to substances like dust, pollen, or certain foods.\n\n"
            "Home care:\n"
            "1. Identify and avoid the trigger where possible.\n"
            "2. Keep your surroundings clean and dust-free.\n"
            "3. Wash hands/face after exposure to suspected allergens.\n\n"
            "Common OTC medicine: Antihistamines like Cetirizine or Loratadine for mild allergic symptoms."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: swelling of the face/throat, difficulty breathing, or widespread "
            "rash — these need immediate medical attention."
        )

    elif "food poison" in msg:
        return (
            "🍽️ Food Poisoning\n"
            "Illness caused by eating contaminated or spoiled food, leading to stomach upset.\n\n"
            "Home care:\n"
            "1. Drink ORS or clear fluids frequently to stay hydrated.\n"
            "2. Eat bland food (rice, banana, toast) once you can tolerate it.\n"
            "3. Avoid dairy, spicy, or oily food until fully recovered.\n\n"
            "Common OTC medicine: ORS is the priority. Anti-nausea/anti-diarrheal medicine only "
            "if advised by a pharmacist or doctor."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: symptoms last more than 2 days, or with high fever, blood in stool, "
            "or signs of severe dehydration."
        )

    elif "migraine" in msg:
        return (
            "🤕 Migraine\n"
            "A recurring type of headache often with throbbing pain, sensitivity to light/sound, and nausea.\n\n"
            "Home care:\n"
            "1. Rest in a quiet, dark room at the first sign of an attack.\n"
            "2. Apply a cold compress to your forehead/neck.\n"
            "3. Identify and avoid personal triggers (certain foods, stress, lack of sleep).\n\n"
            "Common OTC medicine: Paracetamol or ibuprofen for occasional mild attacks."
            f"{DISCLAIMER}\n\n"
            "See a doctor if: migraines are frequent, worsening, or come with vision changes, "
            "confusion, or numbness."
        )

    else:
        return (
            "I don't have specific information on that symptom yet.\n"
            "Please consult a doctor for a proper diagnosis, or try describing symptoms like "
            "fever, cold, cough, dengue, headache, diabetes, blood pressure, malaria, typhoid, "
            "asthma, covid-19, allergy, food poisoning, or migraine."
        )


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        mobile = request.form.get("mobile", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        error = validate_registration(name, email, mobile, password, confirm_password)

        if not error:
            try:
                with db() as conn:
                    conn.execute(
                        "INSERT INTO users(name, email, mobile, password_hash) VALUES(?,?,?,?)",
                        (name, email, mobile, generate_password_hash(password)),
                    )
                return redirect("/login")
            except sqlite3.IntegrityError:
                error = "An account with this email already exists."

    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        with db() as conn:
            user = conn.execute(
                "SELECT * FROM users WHERE email=?", (email,)
            ).fetchone()

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["name"] = user["name"]
            session["email"] = user["email"]

            with db() as conn:
                conn.execute(
                    "INSERT INTO login_activity(user_id) VALUES(?)", (user["id"],)
                )

            return redirect("/dashboard")
        error = "Invalid email or password."

    return render_template(
        "login.html",
        error=error,
        reset_error=request.args.get("reset_error"),
        reset_success=request.args.get("reset_success"),
    )


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "GET":
        return redirect("/login")

    email = request.form.get("email", "").strip().lower()
    new_password = request.form.get("new_password", "")

    if not new_password or len(new_password) < 6:
        return redirect("/login?reset_error=New+password+must+be+at+least+6+characters.")

    with db() as conn:
        user = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        if not user:
            return redirect("/login?reset_error=No+account+found+with+that+email.")
        conn.execute(
            "UPDATE users SET password_hash=? WHERE id=?",
            (generate_password_hash(new_password), user["id"]),
        )

    return redirect("/login?reset_success=Password+updated!+You+can+log+in+with+your+new+password+now.")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        name=session.get("name", ""),
        tip=get_daily_tip(),
    )


@app.route("/log-progress", methods=["POST"])
def log_progress():
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    kind = data.get("type")
    if kind not in PROGRESS_LIMITS:
        return jsonify({"error": "invalid type"}), 400

    progress = get_progress()
    progress[kind] = min(progress[kind] + PROGRESS_STEP[kind], PROGRESS_LIMITS[kind])
    session["progress"] = progress
    session.modified = True

    return jsonify({"progress": progress, "limits": PROGRESS_LIMITS})


# ---------------- PROFILE (its own dedicated page) ----------------
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        save_profile()
        return redirect("/profile")

    with db() as conn:
        prof = conn.execute(
            "SELECT * FROM profile WHERE user_id=?", (session["user_id"],)
        ).fetchone()

    return render_template("profile.html", name=session.get("name", ""), profile=prof)


def save_profile():
    age = request.form.get("age") or None
    gender = request.form.get("gender") or None
    blood_group = request.form.get("blood_group") or None
    weight = request.form.get("weight") or None
    height = request.form.get("height") or None

    with db() as conn:
        existing = conn.execute(
            "SELECT 1 FROM profile WHERE user_id=?", (session["user_id"],)
        ).fetchone()
        if existing:
            conn.execute(
                "UPDATE profile SET age=?, gender=?, blood_group=?, weight=?, height=? WHERE user_id=?",
                (age, gender, blood_group, weight, height, session["user_id"]),
            )
        else:
            conn.execute(
                "INSERT INTO profile(user_id, age, gender, blood_group, weight, height) VALUES(?,?,?,?,?,?)",
                (session["user_id"], age, gender, blood_group, weight, height),
            )


# ---------------- DAILY HEALTH TIPS (its own dedicated page) ----------------
@app.route("/daily-health-tips")
def daily_health_tips_page():
    if "user_id" not in session:
        return redirect("/login")

    daily_tips = [
        "Drink at least 8 glasses of water today.",
        "Take a 10-minute walk after meals to aid digestion.",
        "Wash your hands before eating and after using the washroom.",
        "Get 7-8 hours of sleep for better immunity and focus.",
        "Include a portion of fruits or vegetables in every meal.",
    ]
    faqs = [
        {"q": "How often should I check my BMI?", "a": "Checking once a month is enough unless you're actively managing your weight."},
        {"q": "Is the chatbot a replacement for a doctor?", "a": "No — it's an awareness tool. Always consult a doctor for diagnosis and treatment."},
        {"q": "How much water should I drink daily?", "a": "Around 8 glasses (2-3 litres) is a common guideline, more in hot weather or with exercise."},
        {"q": "How do vaccines help prevent disease?", "a": "They train your immune system to recognize and fight specific germs before you get seriously ill."},
    ]

    return render_template(
        "daily_health_tips.html",
        name=session.get("name", ""),
        daily_tips=daily_tips,
        faqs=faqs,
    )


# ---------------- CHAT HISTORY (search + clear) ----------------
@app.route("/chat-history")
def chat_history_page():
    if "user_id" not in session:
        return redirect("/login")

    q = request.args.get("q", "").strip()
    with db() as conn:
        if q:
            rows = conn.execute(
                "SELECT id, message, reply, created_at FROM chat_history "
                "WHERE user_id=? AND (message LIKE ? OR reply LIKE ?) ORDER BY id DESC",
                (session["user_id"], f"%{q}%", f"%{q}%"),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT id, message, reply, created_at FROM chat_history WHERE user_id=? ORDER BY id DESC",
                (session["user_id"],),
            ).fetchall()

    return render_template("chat_history.html", name=session.get("name", ""), rows=rows, q=q)


@app.route("/chat-history/clear", methods=["POST"])
def clear_chat_history():
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401
    with db() as conn:
        conn.execute("DELETE FROM chat_history WHERE user_id=?", (session["user_id"],))
    return jsonify({"status": "cleared"})


@app.route("/download-chat-pdf")
def download_chat_pdf():
    if "user_id" not in session:
        return redirect("/login")

    with db() as conn:
        rows = conn.execute(
            "SELECT message, reply, created_at FROM chat_history WHERE user_id=? ORDER BY id ASC",
            (session["user_id"],),
        ).fetchall()

    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import simpleSplit
    except ImportError:
        return "PDF export needs the 'reportlab' package. Run: pip install reportlab", 500

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    y = height - 30 * mm

    c.setFont("Helvetica-Bold", 14)
    c.drawString(20 * mm, y, f"Chat History — {session.get('name', '')}")
    y -= 12 * mm
    c.setFont("Helvetica", 10)

    for row in rows:
        for label, text in (("You", row["message"]), ("Bot", row["reply"])):
            lines = simpleSplit(f"{label}: {text}", "Helvetica", 10, width - 40 * mm)
            for line in lines:
                if y < 20 * mm:
                    c.showPage()
                    c.setFont("Helvetica", 10)
                    y = height - 20 * mm
                c.drawString(20 * mm, y, line)
                y -= 6 * mm
        y -= 4 * mm

    c.save()
    buf.seek(0)
    return Response(
        buf.read(),
        mimetype="application/pdf",
        headers={"Content-Disposition": "attachment; filename=chat_history.pdf"},
    )


DISEASE_DETAILS = [
    {"emoji": "🌡️", "name": "Fever",
     "desc": "The body's natural response to infection, raising internal temperature to fight off germs.",
     "symptoms": "High temperature, chills, sweating, weakness, headache, body ache.",
     "causes": "Viral or bacterial infections, heat exhaustion, inflammation.",
     "risk_factors": "Weak immunity, recent infection exposure, young children and elderly.",
     "prevention": "Wash hands regularly, stay hydrated, avoid contact with infected people.",
     "home_remedies": "Rest, drink plenty of fluids, tepid sponging, light clothing.",
     "doctor": "Temperature above 103°F (39.4°C), fever lasting more than 3 days, or with rash/stiff neck.",
     "otc": "Paracetamol for fever reduction."},
    {"emoji": "🤧", "name": "Common Cold",
     "desc": "A mild viral infection of the nose and throat, usually harmless and short-lived.",
     "symptoms": "Runny/blocked nose, sneezing, sore throat, mild cough.",
     "causes": "Rhinovirus and other respiratory viruses spread through droplets or contact.",
     "risk_factors": "Cold weather, crowded places, weakened immunity, lack of sleep.",
     "prevention": "Frequent hand washing, avoiding close contact with sick people, adequate rest.",
     "home_remedies": "Warm fluids, steam inhalation, honey with warm water, rest.",
     "doctor": "Symptoms lasting beyond 10 days, high fever, or difficulty breathing.",
     "otc": "Antihistamines or decongestants for symptom relief."},
    {"emoji": "😷", "name": "Cough",
     "desc": "A reflex action to clear the airways, often caused by infection, allergy, or irritation.",
     "symptoms": "Dry or productive cough, throat irritation, chest discomfort.",
     "causes": "Viral infection, allergies, smoking, acid reflux, dust/pollution.",
     "risk_factors": "Smoking, asthma, allergies, exposure to pollutants.",
     "prevention": "Avoid smoke/dust exposure, stay hydrated, treat colds early.",
     "home_remedies": "Warm water with honey and ginger, steam inhalation, throat lozenges.",
     "doctor": "Cough lasting more than 2-3 weeks, blood in mucus, or breathing difficulty.",
     "otc": "Cough syrup or lozenges suited to dry/wet cough type."},
    {"emoji": "🤕", "name": "Headache",
     "desc": "Pain or discomfort in the head, often linked to stress, dehydration, or tension.",
     "symptoms": "Dull or throbbing pain, pressure around forehead/temples, sensitivity to light.",
     "causes": "Stress, dehydration, lack of sleep, eye strain, sinus issues.",
     "risk_factors": "High stress lifestyle, poor sleep habits, excessive screen time.",
     "prevention": "Stay hydrated, maintain regular sleep, manage stress, take screen breaks.",
     "home_remedies": "Rest in a quiet dark room, cold compress, adequate water intake.",
     "doctor": "Sudden severe headache, headache with vision changes, confusion, or after injury.",
     "otc": "Paracetamol or ibuprofen for occasional headaches."},
    {"emoji": "🍬", "name": "Diabetes",
     "desc": "A chronic condition where the body cannot properly regulate blood sugar levels.",
     "symptoms": "Excessive thirst, frequent urination, fatigue, blurred vision, slow-healing wounds.",
     "causes": "Insulin resistance (Type 2) or insufficient insulin production (Type 1).",
     "risk_factors": "Family history, obesity, sedentary lifestyle, poor diet, age above 45.",
     "prevention": "Balanced diet, regular exercise, healthy weight, routine sugar checks.",
     "home_remedies": "Balanced low-sugar diet, regular physical activity, stress management.",
     "doctor": "Very high/low blood sugar readings, or any new symptoms — needs ongoing medical care.",
     "otc": "No safe OTC option — all diabetes medication must be doctor-prescribed and monitored."},
    {"emoji": "🩺", "name": "Hypertension",
     "desc": "A condition where blood pressure against artery walls stays consistently elevated.",
     "symptoms": "Often none (silent); sometimes headache, dizziness, or nosebleeds.",
     "causes": "High salt intake, obesity, stress, lack of exercise, genetics.",
     "risk_factors": "Family history, high salt diet, smoking, obesity, older age.",
     "prevention": "Low-salt diet, regular exercise, limit alcohol, manage stress, routine BP checks.",
     "home_remedies": "Reduce salt, exercise regularly, relaxation techniques, adequate sleep.",
     "doctor": "Reading above 180/120, or with chest pain, severe headache, or vision problems.",
     "otc": "No safe OTC option — BP medicines must be doctor-prescribed based on readings."},
    {"emoji": "🌬️", "name": "Asthma",
     "desc": "A chronic condition causing airway inflammation, wheezing, and breathlessness.",
     "symptoms": "Wheezing, shortness of breath, chest tightness, coughing (often at night).",
     "causes": "Allergens, air pollution, respiratory infections, exercise, cold air.",
     "risk_factors": "Family history of asthma/allergies, exposure to smoke or pollutants.",
     "prevention": "Avoid known triggers, keep living spaces dust-free, get flu vaccinations.",
     "home_remedies": "Breathing exercises, avoiding triggers, keeping air moist and clean.",
     "doctor": "Severe breathlessness, bluish lips/fingertips, or inhaler not providing relief.",
     "otc": "Inhalers/bronchodilators must be doctor-prescribed based on severity."},
    {"emoji": "🦟", "name": "Dengue",
     "desc": "A mosquito-borne viral infection causing high fever, rash, and severe body pain.",
     "symptoms": "Sudden high fever, severe joint/muscle pain, rash, low platelet count.",
     "causes": "Bite from an infected Aedes mosquito carrying the dengue virus.",
     "risk_factors": "Living in/travel to mosquito-prone tropical areas, stagnant water nearby.",
     "prevention": "Eliminate stagnant water, use mosquito nets/repellents, wear full-sleeve clothing.",
     "home_remedies": "Rest, plenty of fluids, papaya leaf extract (as a supportive measure), monitor platelets.",
     "doctor": "Any suspected dengue needs prompt medical evaluation and platelet monitoring.",
     "otc": "Paracetamol only for fever — avoid aspirin/ibuprofen as they increase bleeding risk."},
    {"emoji": "🦟", "name": "Malaria",
     "desc": "A mosquito-borne disease causing high fever with chills, sweating, and body pain in cycles.",
     "symptoms": "Cyclic fever with chills and sweating, headache, nausea, fatigue.",
     "causes": "Bite from an infected Anopheles mosquito carrying the Plasmodium parasite.",
     "risk_factors": "Living in/travel to malaria-endemic areas, stagnant water sources nearby.",
     "prevention": "Use mosquito nets/repellents, eliminate stagnant water, take prophylaxis if travelling.",
     "home_remedies": "Rest, hydration, and monitoring temperature — alongside prescribed antimalarial treatment.",
     "doctor": "Cyclic fever with chills needs urgent blood testing and doctor-guided treatment.",
     "otc": "Paracetamol for fever only; antimalarial drugs must be doctor-prescribed after diagnosis."},
    {"emoji": "🦠", "name": "Typhoid",
     "desc": "A bacterial infection spread through contaminated food/water, causing prolonged fever.",
     "symptoms": "Sustained fever (often rising in the evening), stomach pain, weakness, rash.",
     "causes": "Infection with Salmonella typhi bacteria from contaminated food or water.",
     "risk_factors": "Poor sanitation, contaminated drinking water, street food in high-risk areas.",
     "prevention": "Drink boiled/purified water, maintain hygiene, get vaccinated if in high-risk areas.",
     "home_remedies": "Boiled water, soft digestible food, complete rest.",
     "doctor": "Fever persisting beyond 3 days needs testing and a doctor-prescribed antibiotic course.",
     "otc": "No safe OTC cure — typhoid requires a doctor-prescribed antibiotic course."},
    {"emoji": "🦠", "name": "COVID-19",
     "desc": "A viral respiratory infection ranging from mild cold-like symptoms to severe illness.",
     "symptoms": "Fever, cough, sore throat, loss of taste/smell, fatigue, breathlessness in severe cases.",
     "causes": "Infection with the SARS-CoV-2 virus, spread via respiratory droplets.",
     "risk_factors": "Close contact with an infected person, crowded indoor spaces, weak immunity.",
     "prevention": "Vaccination, hand hygiene, masks in crowded areas, good ventilation.",
     "home_remedies": "Isolation, rest, hydration, monitoring oxygen levels (SpO2) if possible.",
     "doctor": "Breathing difficulty, oxygen level below 94%, chest pain, or confusion.",
     "otc": "Paracetamol for fever and body ache."},
    {"emoji": "🍽️", "name": "Food Poisoning",
     "desc": "Illness caused by eating contaminated or spoiled food, leading to stomach upset.",
     "symptoms": "Nausea, vomiting, diarrhea, stomach cramps, sometimes mild fever.",
     "causes": "Bacteria, viruses, or toxins in contaminated or improperly stored food.",
     "risk_factors": "Eating undercooked food, street food, poor food storage/hygiene.",
     "prevention": "Eat freshly cooked food, wash hands before eating, store food properly.",
     "home_remedies": "ORS and fluids, bland food (rice, banana, toast), avoid dairy/oily food.",
     "doctor": "Symptoms lasting more than 2 days, blood in stool, high fever, or severe dehydration.",
     "otc": "ORS is the priority; anti-nausea/anti-diarrheal only if advised by a pharmacist/doctor."},
    {"emoji": "🤧", "name": "Allergy",
     "desc": "An overreaction of the immune system to substances like dust, pollen, or certain foods.",
     "symptoms": "Sneezing, itchy/watery eyes, skin rash, swelling, in severe cases breathing difficulty.",
     "causes": "Immune reaction to allergens such as pollen, dust mites, pet dander, or foods.",
     "risk_factors": "Family history of allergies, asthma, frequent exposure to allergens.",
     "prevention": "Identify and avoid triggers, keep living spaces clean and dust-free.",
     "home_remedies": "Avoid the trigger, wash exposed skin, keep surroundings clean.",
     "doctor": "Swelling of face/throat, breathing difficulty, or widespread rash needs urgent care.",
     "otc": "Antihistamines like Cetirizine or Loratadine for mild allergic symptoms."},
    {"emoji": "🩸", "name": "Anemia",
     "desc": "A condition where the blood lacks enough healthy red blood cells to carry adequate oxygen.",
     "symptoms": "Fatigue, pale skin, weakness, dizziness, shortness of breath.",
     "causes": "Iron/vitamin deficiency, blood loss, chronic disease, poor diet.",
     "risk_factors": "Poor diet, heavy menstrual bleeding, pregnancy, chronic illness.",
     "prevention": "Iron-rich diet (leafy greens, legumes, meat), regular health check-ups.",
     "home_remedies": "Iron and vitamin-rich foods, adequate rest, avoiding overexertion.",
     "doctor": "Persistent fatigue, dizziness, or paleness should be evaluated with a blood test.",
     "otc": "Iron/vitamin supplements only as advised by a doctor after a blood test."},
    {"emoji": "🤕", "name": "Migraine",
     "desc": "A recurring headache disorder often with throbbing pain, light sensitivity, and nausea.",
     "symptoms": "Throbbing one-sided headache, nausea, sensitivity to light/sound, visual aura.",
     "causes": "Triggers include stress, certain foods, hormonal changes, lack of sleep.",
     "risk_factors": "Family history, high stress, irregular sleep, hormonal fluctuations.",
     "prevention": "Identify and avoid personal triggers, maintain regular sleep, manage stress.",
     "home_remedies": "Rest in a quiet dark room, cold compress, adequate hydration.",
     "doctor": "Frequent/worsening migraines, or with vision changes, confusion, or numbness.",
     "otc": "Paracetamol or ibuprofen for occasional mild attacks."},
]


@app.route("/disease-info")
def disease_info():
    if "user_id" not in session:
        return redirect("/login")

    return render_template("disease_info.html", diseases=DISEASE_DETAILS, name=session.get("name", ""))


@app.route("/emergency")
def emergency():
    if "user_id" not in session:
        return redirect("/login")

    emergency_numbers = [
        {"icon": "🚑", "label": "Ambulance", "number": "108"},
        {"icon": "👮", "label": "Police", "number": "100"},
        {"icon": "🚒", "label": "Fire Service", "number": "101"},
        {"icon": "💜", "label": "Women's Helpline", "number": "1091"},
        {"icon": "🧒", "label": "Child Helpline", "number": "1098"},
        {"icon": "☎️", "label": "National Emergency Number", "number": "112"},
    ]
    nearby_hospitals = [
        {"name": "Government General Hospital", "type": "Multi-specialty · Govt.", "number": "044-25305000"},
        {"name": "City Community Health Centre", "type": "Primary care · 24x7", "number": "044-24337777"},
        {"name": "Apollo Hospitals", "type": "Multi-specialty · Private", "number": "044-28293333"},
        {"name": "Fortis Malar Hospital", "type": "Multi-specialty · Private", "number": "044-42892222"},
        {"name": "St. John's Ambulance Service", "type": "Emergency transport", "number": "1298"},
    ]
    return render_template(
        "emergency.html",
        emergency_numbers=emergency_numbers,
        nearby_hospitals=nearby_hospitals,
        name=session.get("name", ""),
    )


@app.route("/health-tools")
def health_tools():
    if "user_id" not in session:
        return redirect("/login")

    with db() as conn:
        prof = conn.execute(
            "SELECT * FROM profile WHERE user_id=?", (session["user_id"],)
        ).fetchone()

    return render_template(
        "health_tools.html",
        name=session.get("name", ""),
        profile=prof,
        progress=get_progress(),
        streak=compute_streak(session["user_id"]),
    )


@app.route("/chatbot")
def chatbot():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("chatbot.html", name=session.get("name", ""))


@app.route("/ask", methods=["POST"])
def ask():
    if "user_id" not in session:
        return jsonify({"reply": "Please log in first."}), 401

    msg = request.json.get("msg", "").strip()
    if not msg:
        return jsonify({"reply": "Please type something."})

    state = session.get("chat_state")

    if state:
        fields = state["fields"]
        index = state["index"]
        state["answers"][fields[index]] = msg
        index += 1

        if index < len(fields):
            state["index"] = index
            session["chat_state"] = state
            reply = QUESTION_TEXT[fields[index]]
        else:
            symptom = state["symptom"]
            answers = state["answers"]
            session.pop("chat_state", None)
            reply = build_summary(symptom, answers) + get_reply(symptom, session.get("name", ""))

    else:
        symptom = detect_symptom(msg)
        if symptom:
            fields = SYMPTOM_QUESTIONS[symptom]
            session["chat_state"] = {"symptom": symptom, "fields": fields, "index": 0, "answers": {}}
            reply = QUESTION_TEXT[fields[0]]
        else:
            reply = get_reply(msg, session.get("name", ""))

    with db() as conn:
        cur = conn.execute(
            "INSERT INTO chat_history(user_id, message, reply) VALUES(?,?,?)",
            (session["user_id"], msg, reply),
        )
        chat_id = cur.lastrowid

    return jsonify({"reply": reply, "chat_id": chat_id})


@app.route("/feedback", methods=["POST"])
def feedback():
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    chat_id = data.get("chat_id")
    rating = data.get("rating")
    comment = data.get("comment", "")

    valid_ratings = {"up", "down", "1", "2", "3", "4", "5", 1, 2, 3, 4, 5}
    if rating not in valid_ratings:
        return jsonify({"error": "invalid rating"}), 400

    with db() as conn:
        conn.execute(
            "INSERT INTO feedback(user_id, chat_id, rating, comment) VALUES(?,?,?,?)",
            (session["user_id"], chat_id, str(rating), comment),
        )

    return jsonify({"status": "ok"})


# ---------------- DEDICATED FEEDBACK PAGE ----------------
@app.route("/feedback-page", methods=["GET", "POST"])
def feedback_page():
    if "user_id" not in session:
        return redirect("/login")

    submitted = False
    if request.method == "POST":
        fb_name = request.form.get("name", "").strip() or session.get("name", "")
        fb_email = request.form.get("email", "").strip().lower() or session.get("email", "")
        rating = request.form.get("rating")
        comment = request.form.get("comment", "")
        if rating in {"1", "2", "3", "4", "5"}:
            with db() as conn:
                conn.execute(
                    "INSERT INTO feedback(user_id, chat_id, name, email, rating, comment) VALUES(?,?,?,?,?,?)",
                    (session["user_id"], None, fb_name, fb_email, rating, comment),
                )
            submitted = True

    return render_template("feedback.html", name=session.get("name", ""), email=session.get("email", ""), submitted=submitted)


# ---------------- LOGOUT (final Thank You page) ----------------
@app.route("/logout")
def logout():
    name = session.get("name", "")
    session.clear()
    return render_template("thank_you.html", name=name)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)