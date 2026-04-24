# Day 71 – Flask Login Required Decorator

## 📌 Overview

Today I learned how to **create a reusable login required decorator in Flask**.

Previously, I manually checked `if "user_id" in session` inside each protected route. This approach becomes repetitive as the application grows. To solve this, I created a custom decorator to handle authentication checks cleanly.

In this lesson, I added functionality to:
- Create a reusable `login_required` decorator
- Apply it to multiple routes
- Avoid repeated authentication logic
- Improve code structure and readability

---

## 🛠 What I Did

- Imported `wraps` from `functools`
- Created a custom `login_required` decorator
- Checked session inside decorator
- Redirected unauthorized users
- Applied decorator to protected routes

---

## 📂 Folder Structure

```
Day71/
│
├── app.py
├── database.db
├── templates/
│   ├── login.html
│   └── dashboard.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Decorators in Flask**
- `@login_required` for route protection
- `functools.wraps` for preserving function metadata
- Cleaner and reusable authentication logic
- Scalable route protection

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
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
            flash("Please login first")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def dashboard():
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
```

---

### templates/dashboard.html

```html
<h2>Dashboard</h2>

<p>Welcome! You are logged in.</p>

<a href="/logout">Logout</a>
```

---

## ▶️ Output / Result

1. Try accessing dashboard without login

2. Automatically redirected to login page

3. Login successfully

4. Access granted to protected routes

5. Decorator handles authentication cleanly

---

## ✅ Summary

- Created reusable **login_required decorator**
- Removed repetitive session checks
- Improved code structure and scalability
- Applied clean authentication pattern

---

✅ **Day 71 Completed**

Today I learned how to **use decorators in Flask to protect routes**, making my code cleaner and more maintainable.
