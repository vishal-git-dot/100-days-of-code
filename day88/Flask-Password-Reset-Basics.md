# Day 88 – Flask Password Reset Basics

## 📌 Overview

In this project, I learned the fundamentals of Password Reset functionality in Flask applications.

Password reset systems are essential in modern web applications because users frequently forget their passwords.

Instead of storing or revealing passwords, applications generate secure reset tokens that allow users to create a new password safely.

Examples:

- Gmail
- Facebook
- Instagram
- GitHub
- Banking Applications
- SaaS Platforms

In this project:

- Users can request a password reset
- A secure reset token is generated
- Users can reset their password using the token
- Password reset workflow is introduced

---

# 🛠 What I Did

- Created a password reset request form
- Generated secure reset tokens
- Created reset password links
- Verified reset tokens
- Updated user passwords
- Implemented password reset workflow
- Added security validation

---

# 📂 Folder Structure

```plaintext
flask-password-reset/
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── forgot_password.html
│   ├── reset_password.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

---

# 🧠 Key Concepts Learned

## Password Reset Workflow

Typical workflow:

```plaintext
Forgot Password
       ↓
Generate Token
       ↓
Send Reset Link
       ↓
Verify Token
       ↓
Reset Password
       ↓
Login Again
```

---

## Secure Tokens

Tokens provide temporary access for password resets.

Example:

```python
from itsdangerous import URLSafeTimedSerializer
```

---

## Token Verification

A token must:

- Exist
- Be valid
- Not be expired

---

## Password Security

Never store passwords as plain text.

Use:

```python
generate_password_hash()
```

and

```python
check_password_hash()
```

---

## Expiration Time

Reset tokens should expire.

Example:

```python
max_age=300
```

Meaning:

```plaintext
300 seconds = 5 minutes
```

---

# 💻 Example Code

## app.py

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from itsdangerous import (
    URLSafeTimedSerializer
)

app = Flask(__name__)

app.secret_key = "secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"
)

db = SQLAlchemy(app)

serializer = URLSafeTimedSerializer(
    app.secret_key
)

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

@app.route("/")
def home():

    return redirect(
        url_for("login")
    )

@app.route("/login")
def login():

    return render_template(
        "login.html"
    )

@app.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    if request.method == "POST":

        username = request.form["username"]

        user = User.query.filter_by(
            username=username
        ).first()

        if user:

            token = serializer.dumps(
                username,
                salt="reset-password"
            )

            reset_link = url_for(
                "reset_password",
                token=token,
                _external=True
            )

            print(
                "\nPassword Reset Link:"
            )

            print(reset_link)

            flash(
                "Reset link generated. Check terminal.",
                "success"
            )

        else:

            flash(
                "User not found.",
                "danger"
            )

    return render_template(
        "forgot_password.html"
    )

@app.route(
    "/reset-password/<token>",
    methods=["GET", "POST"]
)
def reset_password(token):

    try:

        username = serializer.loads(
            token,
            salt="reset-password",
            max_age=300
        )

    except:

        flash(
            "Invalid or expired token.",
            "danger"
        )

        return redirect(
            url_for("forgot_password")
        )

    user = User.query.filter_by(
        username=username
    ).first()

    if request.method == "POST":

        new_password = request.form[
            "password"
        ]

        user.password = (
            generate_password_hash(
                new_password
            )
        )

        db.session.commit()

        flash(
            "Password Updated Successfully.",
            "success"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "reset_password.html"
    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

---

## templates/forgot_password.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Forgot Password</title>
</head>
<body>

<h1>Forgot Password</h1>

<form method="POST">

    <input
        type="text"
        name="username"
        placeholder="Username"
        required
    >

    <button type="submit">
        Generate Reset Link
    </button>

</form>

</body>
</html>
```

---

## templates/reset_password.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Reset Password</title>
</head>
<body>

<h1>Reset Password</h1>

<form method="POST">

    <input
        type="password"
        name="password"
        placeholder="New Password"
        required
    >

    <button type="submit">
        Reset Password
    </button>

</form>

</body>
</html>
```

---

## templates/login.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>

<h1>Login Page</h1>

<a href="/forgot-password">
Forgot Password?
</a>

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

    margin-top: 20px;
}

input {

    padding: 10px;

    width: 250px;

    margin-bottom: 10px;
}

button {

    padding: 10px 20px;

    cursor: pointer;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Password reset request form
- Secure token generation
- Token validation
- Password update functionality
- Password hashing
- Expiring reset links

Example Workflow:

```plaintext
Forgot Password
      ↓
Generate Token
      ↓
Create Reset Link
      ↓
Verify Token
      ↓
Enter New Password
      ↓
Password Updated
```

---

# 🔥 Real-World Use Cases

Password reset systems are used in:

- Gmail
- Facebook
- Instagram
- Twitter
- GitHub
- Banking Portals
- E-Commerce Websites
- SaaS Applications

---

# ⚠️ Production Improvements

This project prints reset links in the terminal for learning purposes.

Production systems should:

### Send Email

Using:

```python
Flask-Mail
```

---

### Use HTTPS

Protect reset links with SSL.

---

### Short Token Expiry

Example:

```python
5–15 Minutes
```

---

### Password Complexity Rules

Require:

- Uppercase letters
- Numbers
- Symbols
- Minimum length

---

### One-Time Use Tokens

Invalidate token after successful reset.

---

# 🚀 Skills Gained

After completing Day 88, you can:

- Generate secure tokens
- Implement password reset workflows
- Hash passwords securely
- Verify token validity
- Build account recovery systems
- Improve application security

---

# ✅ Summary

In Day 88, I learned how Password Reset systems work in Flask applications.

I implemented:

- Reset request forms
- Token generation
- Token verification
- Password updates
- Password hashing

This is one of the most important authentication features in modern web applications and prepares me for:

### Day 89 – Flask Environment Variables
