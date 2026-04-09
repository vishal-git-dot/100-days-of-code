import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# Home Page - Display Data
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("list.html", users=users)

# Add Data
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("form.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
