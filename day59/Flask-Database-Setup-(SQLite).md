# Day 59 – Flask Database Setup (SQLite)

## 📌 Overview

Today I learned how to **connect a Flask application to a database using SQLite**.

SQLite is a lightweight, file-based database that is perfect for beginners and small projects. I learned how to:
- Create a database
- Connect it with Flask
- Create tables
- Insert data

This is the first step toward building **data-driven applications** in Flask.

---

## 🛠 What I Did

- Connected Flask app to SQLite database
- Created a database file (`database.db`)
- Created a table using SQL
- Inserted sample data into the table
- Retrieved data from the database

---

## 📂 Folder Structure

```
Day59/
│
├── app.py
├── database.db
└── README.md
```

---

## 🧠 Key Concepts Learned

- **SQLite** → Lightweight database stored as a file
- `sqlite3` → Python module to interact with SQLite
- `connect()` → Connect to database
- `cursor()` → Execute SQL queries
- `commit()` → Save changes
- `close()` → Close connection

---

## 💻 Example Code

### app.py

```python
import sqlite3
from flask import Flask

app = Flask(__name__)

# Create Database and Table
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

# Insert Data
def insert_data(name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))

    conn.commit()
    conn.close()

# Fetch Data
@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return str(users)


if __name__ == "__main__":
    init_db()
    insert_data("John")
    insert_data("Alice")
    app.run(debug=True)
```

---

## ▶️ Output / Result

Run the app:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

Output:

```
[(1, 'John'), (2, 'Alice')]
```

This shows data successfully stored and retrieved from the database.

---

## ✅ Summary

- Connected Flask with SQLite database
- Created tables using SQL
- Inserted and retrieved data
- Understood basic database operations

---

✅ **Day 59 Completed**

Today I learned how to **set up and use SQLite database in Flask**, enabling data storage and retrieval in web applications.
