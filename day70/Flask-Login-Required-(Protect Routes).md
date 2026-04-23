# Day 70 – Flask Login Required (Protect Routes)

## 📌 Overview

Today I learned how to **protect routes in a Flask application using login required logic**.

After implementing login and logout, the next step is to restrict access so that only authenticated users can access certain pages. This ensures better security and proper user flow.

In this lesson, I added functionality to:
- Restrict access to certain routes
- Check if a user is logged in using session
- Redirect unauthorized users to login page
- Protect sensitive pages

---

## 🛠 What I Did

- Used `session` to track logged-in users
- Created a login check using `if "user_id" in session`
- Restricted access to protected routes
- Redirected unauthorized users to `/login`
- Ensured secure navigation flow

---

## 📂 Folder Structure

```
Day70/
│
├── app.py
├── database.db
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Route Protection** → Restrict access to authenticated users
- Flask `session` for login tracking
- Conditional route access
- Redirect unauthorized users
- Basic access control

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route("/")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect("/")

        flash("Invalid credentials")
        return redirect("/login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
