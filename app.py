from flask import Flask, render_template, request, redirect, session, jsonify

import sqlite3
import os

app = Flask(__name__)
app.secret_key = "healthbot_secret_key"

DB_NAME = "healthbot.db"


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
                password TEXT NOT NULL
            )
        """)


init_db()


# ---------------- CHAT LOGIC ----------------
def get_reply(msg):
    msg = msg.lower()

    if "fever" in msg:
        return "Drink plenty of fluids and rest. If fever is high or lasts more than 2 days, consult a doctor."
    elif "cold" in msg:
        return "Steam inhalation helps. Avoid cold drinks and get enough rest."
    elif "cough" in msg:
        return "Warm water with honey is recommended. See a doctor if it persists beyond a week."
    elif "dengue" in msg:
        return "Go to the hospital immediately for a blood test if you suspect dengue."
    elif "headache" in msg:
        return "Rest in a quiet, dark room and stay hydrated. Consult a doctor if it's severe or frequent."
    else:
        return "I'm not fully sure about that. Please consult a doctor for a proper diagnosis."


# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not name or not email or not password:
            error = "Please fill in all fields."
        else:
            try:
                with db() as conn:
                    conn.execute(
                        "INSERT INTO users(name, email, password) VALUES(?,?,?)",
                        (name, email, password),
                    )
                return redirect("/login")
            except sqlite3.IntegrityError:
                error = "An account with this email already exists."

    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        with db() as conn:
            user = conn.execute(
                "SELECT * FROM users WHERE email=? AND password=?",
                (email, password),
            ).fetchone()

        if user:
            session["user"] = email
            session["name"] = user["name"]
            return redirect("/dashboard")
        error = "Invalid email or password."

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", name=session.get("name", ""))


@app.route("/chatbot")
def chatbot():
    if "user" not in session:
        return redirect("/login")
    return render_template("chatbot.html", name=session.get("name", ""))


@app.route("/ask", methods=["POST"])
def ask():
    if "user" not in session:
        return jsonify({"reply": "Please log in first."}), 401
    data = request.json.get("msg", "")
    return jsonify({"reply": get_reply(data)})


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
