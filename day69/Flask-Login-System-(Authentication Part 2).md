# Day 69 – Flask Login System (Authentication Part 2)

## 📌 Overview

Today I learned how to **implement a login system in a Flask application**.

After building user registration, the next step in authentication is allowing users to log in securely. This involves verifying credentials and managing user sessions.

In this lesson, I added functionality to:
- Authenticate users using email and password
- Verify hashed passwords
- Manage user sessions
- Redirect users after login

---

## 🛠 What I Did

- Created a **login route (`/login`)**
- Retrieved user data from the database
- Verified passwords using `check_password_hash()`
- Used `session` to store logged-in user
- Redirected users after successful login
- Displayed error messages for invalid login

---

## 📂 Folder Structure

```
Day69/
│
├── app.py
├── database.db
├── templates/
│   ├── login.html
│   └── register.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **User Authentication (Part 2)** → Login system
- `check_password_hash()` for password verification
- Flask `session` for login state
- Handling invalid credentials
- Redirecting authenticated users

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash("Login successful!")
            return redirect("/")

        flash("Invalid email or password")
        return redirect("/login")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully!")
    return redirect("/login")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

---

### templates/login.html

```html
<h2>Login</h2>

{% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
{% endwith %}

<form method="POST">
    <input type="email" name="email" placeholder="Enter email">
    <input type="password" name="password" placeholder="Enter password">
    <button type="submit">Login</button>
</form>

<a href="/register">Register</a>
```

---

## ▶️ Output / Result

1. Open login page:
http://127.0.0.1:5000/login

2. Enter registered email and password

3. Submit form

4. If valid → Login successful and redirected

5. If invalid → Error message shown

---

## ✅ Summary

- Implemented **Login system in Flask**
- Verified passwords securely using hashing
- Used sessions to track logged-in users
- Handled login errors properly

---

✅ **Day 69 Completed**

Today I learned how to **build a secure login system in Flask using sessions and password verification**, continuing the authentication process.
