# Day 73 – Flask Update User Profile

## 📌 Overview

Today I learned how to **update user profile information in a Flask application**.

After displaying user data on the profile page, the next step is to allow users to edit and update their own information. This makes the application interactive and user-friendly.

In this lesson, I added functionality to:
- Edit user profile data
- Pre-fill form with existing user data
- Update database using SQLAlchemy
- Save changes and reflect in UI

---

## 🛠 What I Did

- Created `/edit-profile` route
- Fetched logged-in user using session
- Pre-filled form with existing data
- Updated user record using SQLAlchemy
- Committed changes to database

---

## 📂 Folder Structure

```
Day73/
│
├── app.py
├── database.db
├── templates/
│   ├── profile.html
│   ├── edit_profile.html
│   └── login.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- Updating records using ORM
- Pre-filling form fields
- Handling POST requests
- `db.session.commit()` for saving changes
- User-specific updates

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/profile")
@login_required
def profile():
    user = User.query.get(session.get("user_id"))
    return render_template("profile.html", user=user)

@app.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    user = User.query.get(session.get("user_id"))

    if request.method == "POST":
        user.email = request.form.get("email")
        db.session.commit()
        return redirect("/profile")

    return render_template("edit_profile.html", user=user)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

### templates/edit_profile.html

```html
<h2>Edit Profile</h2>

<form method="POST">
    <input type="email" name="email" value="{{ user.email }}">
    <button type="submit">Update</button>
</form>

<a href="/profile">Back</a>
```

---

## ▶️ Output / Result

1. Login to the app

2. Open profile page

3. Click edit profile

4. Update email and submit

5. Changes reflected instantly

---

## ✅ Summary

- Implemented profile update feature
- Used ORM for updating data
- Improved user interactivity
- Built editable user profile system

---

✅ **Day 73 Completed**

Today I learned how to **update user profile data in Flask**, allowing users to edit and save their information.
