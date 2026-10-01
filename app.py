from flask import Flask, render_template, request
import sqlite3
from analyzer import analyze_job

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("recruitsafe.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_text TEXT,
            risk_score INTEGER,
            risk_level TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        job_text = request.form["job_text"]

        result = analyze_job(job_text)

        conn = sqlite3.connect("recruitsafe.db")

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO scans
            (job_text, risk_score, risk_level)
            VALUES (?, ?, ?)
        """, (
            job_text,
            result["risk_score"],
            result["risk_level"]
        ))

        conn.commit()
        conn.close()

    return render_template("index.html", result=result)


@app.route("/history")
def history():

    conn = sqlite3.connect("recruitsafe.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, risk_score, risk_level, created_at
        FROM scans
        ORDER BY id DESC
    """)

    scans = cursor.fetchall()

    conn.close()

    return render_template("history.html", scans=scans)


if __name__ == "__main__":

    init_db()

    app.run(debug=True)