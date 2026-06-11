from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = "jobs.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            date_applied TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Applied'
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = get_db()
    jobs = conn.execute("SELECT * FROM applications ORDER BY date_applied DESC").fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        company = request.form["company"]
        position = request.form["position"]
        date_applied = request.form["date_applied"]
        conn = get_db()
        conn.execute(
            "INSERT INTO applications (company, position, date_applied, status) VALUES (?, ?, ?, ?)",
            (company, position, date_applied, "Applied")
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/update/<int:job_id>", methods=["POST"])
def update(job_id):
    new_status = request.form["status"]
    conn = get_db()
    conn.execute("UPDATE applications SET status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/delete/<int:job_id>", methods=["POST"])
def delete(job_id):
    conn = get_db()
    conn.execute("DELETE FROM applications WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
