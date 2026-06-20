import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Database Connection
conn = sqlite3.connect('healthbot.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    feedback TEXT
)
''')
conn.commit()

# Repository Function
def save_feedback(name, email, feedback):
    cursor.execute(
        "INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)",
        (name, email, feedback)
    )
    conn.commit()

app = Flask(__name__, template_folder='.')

# Mock Knowledge Base for Public Health Awareness
HEALTH_KNOWLEDGE_BASE = {
    "fever": "Fever could indicate an infection like Flu, Typhoid, or Dengue. Rest well, stay hydrated with fluids/ORS, and monitor temperature. If it exceeds 102°F, consult a physician.",

    "fever with joint pain": "High fever accompanied by severe joint pain is a primary indicator of Chikungunya or Dengue. Avoid self-medication, eliminate stagnant water around your home to prevent mosquitoes, and get a blood test done.",

    "cold": "Common cold is viral. Drink warm fluids, practice steam inhalation, and maintain hand hygiene to avoid spreading it to others.",

    "cough": "Persistent dry cough or cough with mucus could be a sign of respiratory viral infections. Ensure good ventilation, take steam, and seek advice if breathing issues occur.",

    "skin rashes": "Rashes can be due to allergies, viral infections, or vector-borne conditions. Keep the skin clean and dry. Avoid scratching to prevent secondary skin infections.",

    "dengue": "Dengue awareness: Caused by Aedes mosquitoes. Look out for high fever, severe headache, rash, and muscle pain. Drink plenty of water and seek immediate medical evaluation for platelet counts.",

    "headache": "Headache may occur due to stress, dehydration, or infection. Drink water and take adequate rest.",

    "vomiting": "Vomiting may be caused by food poisoning or infection. Stay hydrated and consult a doctor if severe.",

    "diarrhea": "Diarrhea can lead to dehydration. Drink ORS and maintain hygiene.",

    "malaria": "Malaria is spread by mosquitoes. Symptoms include fever, chills, and sweating. Seek medical care."
}

DEFAULT_RESPONSE = "Thank you for detailing your symptoms. While I cannot diagnose you definitively, I recommend monitoring your symptoms closely. Ensure proper hydration and sanitization. If symptoms persist or worsen, please visit your nearest public primary health care center (PHC)."

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        if email == "admin@gmail.com" and password == "1234":
            return redirect(url_for('dashboard'))
        else:
            return "invalid email or password"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# REST API Endpoint
@app.route('/api/health', methods=['GET'])
def health_api():
    return jsonify({
        "status": "success",
        "message": "AI Public Health Chatbot API Working"
    })

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data.get('message', '').lower().strip()

    if not user_message:
        return jsonify({
            "reply": "I couldn't catch that. Could you please specify your symptoms again?"
        })

    bot_reply = None

    for key in HEALTH_KNOWLEDGE_BASE:
        if key in user_message:
            bot_reply = HEALTH_KNOWLEDGE_BASE[key]
            break

    if not bot_reply:
        bot_reply = DEFAULT_RESPONSE

    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
