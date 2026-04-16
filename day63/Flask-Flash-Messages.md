# Day 63 – Flask Flash Messages

## 📌 Overview

Today I learned how to **use flash messages in Flask to display feedback to users**.

Flash messages are useful for showing success, error, or informational messages after performing actions like adding, updating, or deleting records.

In this lesson, I added functionality to:
- Display success messages after actions
- Show feedback to users on the UI
- Improve user experience using alerts

---

## 🛠 What I Did

- Enabled **flash messaging system in Flask**
- Set a **secret key** for session handling
- Used `flash()` to send messages
- Displayed messages in templates using Jinja2
- Styled messages using simple HTML

---

## 📂 Folder Structure

```
Day63/
│
├── app.py
├── database.db
├── templates/
│   ├── list.html
│   └── edit.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Flash Messages** → Temporary messages stored in session
- `flash("message")`
- `get_flashed_messages()`
- Importance of `secret_key` in Flask
- Enhancing UI feedback

---

## 💻 Example Code

### app.py

```python
import sqlite3
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = "secret123"  # Required for flash messages

# Fetch all users
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return render_template("list.html", users=users)


# Delete user with flash message
@app.route("/delete/<int:id>")
def delete_user(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash("User deleted successfully!")
    return redirect("/")
```

---

### templates/list.html

```html
<h2>Users</h2>

<!-- Flash Messages -->
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li style="color: green;">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
{% endwith %}

<a href="/add">Add User</a>

<ul>
{% for user in users %}
    <li>
        {{ user[1] }}
        <a href="/edit/{{ user[0] }}">Edit</a>
        <a href="/delete/{{ user[0] }}">Delete</a>
    </li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

1. Open user list:
http://127.0.0.1:5000/

2. Click **Delete** next to a user

3. User is deleted from database

4. Success message appears:
User deleted successfully!

---

## ✅ Summary

- Implemented **Flash Messages in Flask**
- Used `flash()` to send messages
- Displayed messages using Jinja2
- Improved user experience with feedback alerts

---

✅ **Day 63 Completed**

Today I learned how to **use flash messages in Flask to display user feedback after actions**, improving the usability of my application.
