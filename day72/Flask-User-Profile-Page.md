# Day 72 – Flask User Profile Page

## 📌 Overview

Today I learned how to **create a user profile page in a Flask application**.

After implementing authentication and protecting routes, the next step is to display user-specific data. A profile page allows logged-in users to view their own information from the database.

In this lesson, I added functionality to:
- Fetch logged-in user details
- Display user-specific data
- Use session to identify the current user
- Build a personalized profile page

---

## 🛠 What I Did

- Retrieved `user_id` from session
- Queried database for logged-in user
- Passed user data to template
- Created a profile route (`/profile`)
- Displayed user information dynamically

---

## 📂 Folder Structure

```
Day72/
│
├── app.py
├── database.db
├── templates/
│   ├── profile.html
│   └── login.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **User Sessions** → Identify logged-in user
- Fetching data using `Model.query.get()`
- Passing dynamic data to templates
- Personalized user interface
- Building user-specific pages

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, session, redirect
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
    user_id = session.get("user_id")
    user = User.query.get(user_id)
    return render_template("profile.html", user=user)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

### templates/profile.html

```html
<h2>User Profile</h2>

<p><strong>Email:</strong> {{ user.email }}</p>

<a href="/">Dashboard</a>
```

---

## ▶️ Output / Result

1. Login to the application

2. Open:
http://127.0.0.1:5000/profile

3. Profile page displays logged-in user's email

4. Only accessible if user is logged in

---

## ✅ Summary

- Created **user profile page**
- Displayed logged-in user data
- Used session to fetch user details
- Built personalized UI

---

✅ **Day 72 Completed**

Today I learned how to **create a user profile page in Flask**, displaying dynamic data for the logged-in user.
