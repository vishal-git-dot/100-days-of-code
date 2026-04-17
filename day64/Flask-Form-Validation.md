# Day 64 – Flask Form Validation

## 📌 Overview

Today I learned how to **validate form inputs in a Flask application**.

Form validation ensures that user input is correct before storing it in the database. This helps prevent empty or invalid data and improves the reliability of the application.

In this lesson, I added functionality to:
- Validate user input before saving
- Prevent empty form submissions
- Show error messages using flash messages
- Improve overall data quality

---

## 🛠 What I Did

- Added validation for form inputs
- Checked for empty fields using Python conditions
- Used `flash()` to display error messages
- Prevented invalid data from being saved
- Redirected users after successful submission

---

## 📂 Folder Structure

```
Day64/
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

- **Form Validation** → Ensuring correct user input
- Checking empty fields (`if not name`)
- Using `flash()` for error messages
- Preventing invalid database operations
- Improving user input handling

---

## 💻 Example Code

### app.py

```python
import sqlite3
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "secret123"

# Home route
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return render_template("list.html", users=users)


# Add user with validation
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")

        # Validation
        if not name or name.strip() == "":
            flash("Name cannot be empty!")
            return redirect("/add")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        flash("User added successfully!")
        return redirect("/")

    return render_template("form.html")
```

---

### templates/form.html

```html
<h2>Add User</h2>

<!-- Flash Messages -->
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li style="color: red;">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
{% endwith %}

<form method="POST">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Add</button>
</form>

<a href="/">Back</a>
```

---

## ▶️ Output / Result

1. Open add user page:
http://127.0.0.1:5000/add

2. Submit empty form

3. Error message appears:
Name cannot be empty!

4. Enter valid name and submit

5. User is added successfully and redirected to list page

---

## ✅ Summary

- Implemented **Form Validation in Flask**
- Prevented empty input submissions
- Used `flash()` for error handling
- Improved data integrity and user experience

---

✅ **Day 64 Completed**

Today I learned how to **validate form inputs in Flask**, ensuring only correct data is stored in the database.
