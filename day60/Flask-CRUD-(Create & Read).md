# Day 60 – Flask CRUD (Create & Read)

## 📌 Overview

Today I learned how to implement **basic CRUD operations (Create & Read)** in Flask using **SQLite database**.

CRUD stands for:
- **Create** → Add new data  
- **Read** → Display data  

In this step, I built a simple application where users can:
- Add new records through a form
- View stored records from the database

This is the foundation for building **data-driven web applications**.

---

## 🛠 What I Did

- Created a form to add data
- Inserted data into SQLite database
- Retrieved data from database
- Displayed records in HTML template
- Connected backend with frontend

---

## 📂 Folder Structure

```
Day60/
│
├── app.py
├── database.db
├── templates/
│   ├── form.html
│   └── list.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **CRUD (Create & Read)** operations
- `INSERT INTO` → Add data
- `SELECT *` → Fetch data
- `request.form` → Get form input
- Rendering database data in templates

---

## 💻 Example Code

### app.py

```python
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
```

---

### templates/form.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
</head>
<body>

<h2>Add User</h2>

<form method="POST">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Add</button>
</form>

<a href="/">View Users</a>

</body>
</html>
```

---

### templates/list.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>

<h2>Users</h2>

<a href="/add">Add New User</a>

<ul>
{% for user in users %}
    <li>{{ user[1] }}</li>
{% endfor %}
</ul>

</body>
</html>
```

---

## ▶️ Output / Result

1. Open:
```
http://127.0.0.1:5000/
```

2. Click **Add New User**

3. Enter a name and submit

4. Data appears in the list:

```
Users:
- John
- Alice
```

---

## ✅ Summary

- Implemented **Create (Insert)** operation
- Implemented **Read (Display)** operation
- Connected Flask with SQLite database
- Built a simple data-driven app

---

✅ **Day 60 Completed**

Today I learned how to **implement basic CRUD operations (Create & Read) in Flask**, enabling users to add and view data from a database.
