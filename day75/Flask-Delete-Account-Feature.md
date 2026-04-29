# Day 75 – Flask Delete Account Feature

## 📌 Overview

Today I learned how to **implement a delete account feature in a Flask application**.

After building authentication, profile management, and password updates, the next important step is giving users control over their data. This includes the ability to delete their account permanently.

In this lesson, I added functionality to:
- Allow users to delete their account
- Remove user data from database
- Clear session after deletion
- Redirect safely after account removal

---

## 🛠 What I Did

- Created `/delete-account` route
- Retrieved logged-in user from session
- Deleted user using `db.session.delete()`
- Committed changes to database
- Cleared session after deletion
- Redirected to login page

---

## 📂 Folder Structure

```
Day75/
│
├── app.py
├── database.db
├── templates/
│   ├── profile.html
│   ├── login.html
│   └── confirm_delete.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- Deleting records using ORM
- `db.session.delete()` usage
- Session handling after deletion
- Data ownership and control
- Safe user flow after account removal

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, redirect, session
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

@app.route("/delete-account")
@login_required
def delete_account():
    user = User.query.get(session.get("user_id"))

    db.session.delete(user)
    db.session.commit()

    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

### templates/confirm_delete.html

```html
<h2>Delete Account</h2>

<p>Are you sure you want to delete your account?</p>

<a href="/delete-account">Yes, Delete</a>
<a href="/profile">Cancel</a>
```

---

## ▶️ Output / Result

1. Login to the app

2. Go to delete account page

3. Confirm deletion

4. Account is permanently removed

5. User is logged out and redirected

---

## ✅ Summary

- Implemented account deletion feature
- Removed user data from database
- Cleared session after deletion
- Improved user control over data

---

✅ **Day 75 Completed**

Today I learned how to **delete user accounts in Flask**, completing full user lifecycle management.
