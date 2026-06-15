# Day 90 – Flask Security Best Practices

## 📌 Overview

In this project, I learned the fundamental security practices required to build secure Flask applications.

Security is one of the most important aspects of backend development. Even a small vulnerability can expose user data, passwords, payment information, and application resources.

Professional Flask applications implement multiple layers of security to protect users and systems.

Examples:

- Authentication Security
- Password Protection
- Session Security
- CSRF Protection
- Environment Variables
- Secure File Uploads
- SQL Injection Prevention

In this project:

- Implemented password hashing
- Added CSRF protection
- Secured sessions
- Protected forms
- Used environment variables
- Improved authentication security
- Applied production-ready security practices

---

# 🛠 What I Did

- Learned common web vulnerabilities
- Implemented password hashing
- Protected forms against CSRF attacks
- Secured user sessions
- Stored secrets in environment variables
- Prevented SQL injection
- Added secure file upload validation
- Reviewed Flask security best practices

---

# 📂 Folder Structure

```plaintext
flask-security-best-practices/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

---

# 🧠 Key Concepts Learned

## Password Hashing

Never store passwords as plain text.

❌ Bad:

```python
password = "mypassword"
```

Database:

```plaintext
mypassword
```

---

✅ Good:

```python
generate_password_hash(
    password
)
```

Database:

```plaintext
pbkdf2:sha256:600000$....
```

---

Verify password:

```python
check_password_hash(
    stored_password,
    password
)
```

---

## CSRF Protection

### What is CSRF?

Cross-Site Request Forgery tricks a logged-in user into performing actions without their consent.

Example:

```plaintext
Delete Account
Transfer Money
Change Password
```

---

Use:

```python
Flask-WTF
```

to generate CSRF tokens.

---

## Session Security

Store minimal information inside sessions.

Good:

```python
session["user_id"]
```

Bad:

```python
session["password"]
```

---

Secure session configuration:

```python
app.config[
    "SESSION_COOKIE_HTTPONLY"
] = True

app.config[
    "SESSION_COOKIE_SECURE"
] = True
```

---

## Environment Variables

Never hardcode:

```python
SECRET_KEY = "mysecret"
```

Use:

```python
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
```

---

## SQL Injection Prevention

❌ Dangerous:

```python
query = (
    "SELECT * FROM users "
    f"WHERE username='{username}'"
)
```

---

✅ Safe:

```python
User.query.filter_by(
    username=username
)
```

SQLAlchemy automatically escapes values.

---

## File Upload Security

Always validate:

- File Type
- File Extension
- File Size

Example:

```python
ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}
```

---

Use:

```python
secure_filename()
```

before saving uploads.

---

## Authentication Security

Implement:

- Password Hashing
- Login Protection
- Session Expiration
- Account Lockout
- Password Reset

---

## Principle of Least Privilege

Users should only access resources they need.

Example:

```plaintext
Admin → Full Access

User → Limited Access
```

---

# 💻 Example Code

## requirements.txt

```txt
Flask
Flask-WTF
Flask-SQLAlchemy
python-dotenv
Werkzeug
```

---

## .env

```env
SECRET_KEY=my-super-secret-key

DATABASE_URL=sqlite:///database.db
```

---

## app.py

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from flask_sqlalchemy import (
    SQLAlchemy
)

from flask_wtf import (
    FlaskForm
)

from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from dotenv import (
    load_dotenv
)

import os

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = (
    os.getenv("SECRET_KEY")
)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = (
    os.getenv("DATABASE_URL")
)

app.config[
    "SESSION_COOKIE_HTTPONLY"
] = True

db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True
    )

    password = db.Column(
        db.String(255)
    )

class RegisterForm(
    FlaskForm
):

    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField(
        "Register"
    )

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        hashed_password = (
            generate_password_hash(
                form.password.data
            )
        )

        user = User(
            username=form.username.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration Successful",
            "success"
        )

        return redirect(
            url_for("register")
        )

    return render_template(
        "register.html",
        form=form
    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

---

## templates/register.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Secure Registration</title>
</head>
<body>

<h1>Secure Registration</h1>

<form method="POST">

    {{ form.hidden_tag() }}

    <p>

        {{ form.username.label }}

        <br>

        {{ form.username() }}

    </p>

    <p>

        {{ form.password.label }}

        <br>

        {{ form.password() }}

    </p>

    <p>

        {{ form.submit() }}

    </p>

</form>

</body>
</html>
```

---

## static/style.css

```css
body {

    font-family: Arial, sans-serif;

    margin: 40px;
}

form {

    width: 350px;
}

input {

    width: 100%;

    padding: 10px;

    margin-top: 5px;

    margin-bottom: 15px;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Password hashing
- CSRF protection
- Secure sessions
- Environment variables
- SQL injection prevention
- Secure registration system

Example Workflow:

```plaintext
User Registers
       ↓
Password Hashed
       ↓
Stored Securely
       ↓
CSRF Token Verified
       ↓
Account Created
```

---

# 🔥 Common Flask Security Vulnerabilities

## Plain Text Passwords

❌ Never do this:

```python
password = "123456"
```

---

## Hardcoded Secret Keys

❌ Never do this:

```python
app.secret_key = "secret"
```

---

## Unvalidated Uploads

❌ Dangerous:

```python
file.save(...)
```

without validation.

---

## SQL Injection

❌ Dangerous:

```python
SELECT * FROM users
```

using string concatenation.

---

## Exposed Debug Mode

Development:

```python
app.run(debug=True)
```

Production:

```python
debug=False
```

---

# 🔐 Flask Security Checklist

Before deploying:

### Password Hashing

```plaintext
✔ Enabled
```

### CSRF Protection

```plaintext
✔ Enabled
```

### Environment Variables

```plaintext
✔ Enabled
```

### Session Security

```plaintext
✔ Enabled
```

### SQL Injection Protection

```plaintext
✔ Enabled
```

### Secure File Uploads

```plaintext
✔ Enabled
```

### Debug Mode Disabled

```plaintext
✔ Enabled
```

---

# 🚀 Skills Gained

After completing Day 90, you can:

- Build secure Flask applications
- Protect passwords
- Prevent CSRF attacks
- Secure sessions
- Use environment variables
- Prevent SQL injection
- Secure file uploads
- Apply production-ready security practices

---

# ✅ Summary

In Day 90, I learned the most important Flask Security Best Practices required for production applications.

I implemented:

- Password Hashing
- CSRF Protection
- Session Security
- Environment Variables
- SQL Injection Prevention
- Secure Authentication

These practices are essential for building professional Flask applications and prepare me for the next phase:

# 🚀 Phase 5 — APIs & Modern Backend Development

### Day 91 – Flask REST API Basics

