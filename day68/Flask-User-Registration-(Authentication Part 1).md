# Day 68 – Flask User Registration (Authentication Part 1)

## 📌 Overview

Today I learned how to **implement user registration in a Flask application**.

After completing CRUD operations with SQLAlchemy, the next step is to build real-world features like authentication. User registration allows new users to create an account and store their credentials securely.

In this lesson, I added functionality to:
- Create a user registration system
- Store user credentials in the database
- Hash passwords for security
- Validate user input

---

## 🛠 What I Did

- Created a **User model with email and password**
- Used `werkzeug.security` for password hashing
- Built a registration route (`/register`)
- Validated user input (empty fields, duplicate email)
- Stored secure password hashes in database

---

## 📂 Folder Structure

```
Day68/
│
├── app.py
├── database.db
├── templates/
│   ├── register.html
│   └── login.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **User Authentication (Part 1)** → Registration system
- `generate_password_hash()` for security
- Storing hashed passwords instead of plain text
- Validating unique users (email)
- Preparing for login system

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("All fields are required!")
            return redirect("/register")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists!")
            return redirect("/register")

        hashed_password = generate_password_hash(password)

        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!")
        return redirect("/login")

    return render_template("register.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

---

### templates/register.html

```html
<h2>Register</h2>

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
    <button type="submit">Register</button>
</form>

<a href="/login">Login</a>
```

---

## ▶️ Output / Result

1. Open register page:
http://127.0.0.1:5000/register

2. Enter email and password

3. Submit form

4. User is registered successfully

5. Password is stored securely (hashed)

---

## ✅ Summary

- Implemented **User Registration system**
- Secured passwords using hashing
- Validated user input and uniqueness
- Prepared foundation for login system

---

✅ **Day 68 Completed**

Today I learned how to **build a user registration system in Flask with password hashing**, starting the authentication process.
