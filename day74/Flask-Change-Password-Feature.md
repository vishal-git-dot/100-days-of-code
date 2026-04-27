# Day 74 – Flask Change Password Feature

## 📌 Overview

Today I learned how to **implement a change password feature in a Flask application**.

After building user authentication and profile management, the next important step is allowing users to securely update their passwords. This improves both usability and security.

In this lesson, I added functionality to:
- Allow users to change their password
- Verify old password before updating
- Hash new password securely
- Update password in database

---

## 🛠 What I Did

- Created `/change-password` route
- Verified old password using `check_password_hash()`
- Hashed new password using `generate_password_hash()`
- Updated password in database
- Added validation for incorrect old password

---

## 📂 Folder Structure

```
Day74/
│
├── app.py
├── database.db
├── templates/
│   ├── change_password.html
│   ├── profile.html
│   └── login.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- Password verification before update
- `check_password_hash()` vs `generate_password_hash()`
- Secure password handling
- Updating sensitive user data
- Enhancing application security

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    user = User.query.get(session.get("user_id"))

    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        if not check_password_hash(user.password, old_password):
            flash("Old password is incorrect")
            return redirect("/change-password")

        user.password = generate_password_hash(new_password)
        db.session.commit()

        flash("Password updated successfully")
        return redirect("/profile")

    return render_template("change_password.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
