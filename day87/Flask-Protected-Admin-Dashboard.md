# Day 87 – Flask Protected Admin Dashboard

## 📌 Overview

In this project, I learned how to create a Protected Admin Dashboard in Flask applications.

In Day 86, we introduced User Roles.

Now, we will build a dedicated Admin Dashboard that can only be accessed by users with the Admin role.

This is a common feature in real-world applications where administrators need special access to manage users, content, settings, and reports.

Examples:

- E-commerce Admin Panels
- Blog CMS Dashboards
- School Management Systems
- CRM Applications
- SaaS Platforms

In this project:

- Users can login
- Admins can access the Admin Dashboard
- Regular users are blocked
- Unauthorized access is prevented
- Role-based protection is enforced

---

# 🛠 What I Did

- Created a protected admin route
- Checked user authentication
- Checked user authorization
- Restricted access based on role
- Displayed admin-only content
- Redirected unauthorized users
- Added flash messages for access control

---

# 📂 Folder Structure

```plaintext
flask-protected-admin-dashboard/
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── admin.html
│   └── base.html
│
└── static/
    └── style.css
```

---

# 🧠 Key Concepts Learned

## Authentication

Authentication verifies:

```plaintext
Who is the user?
```

Example:

```python
session["user_id"]
```

---

## Authorization

Authorization verifies:

```plaintext
What is the user allowed to access?
```

Example:

```python
session["role"]
```

---

## Protected Routes

Routes that require permission.

Example:

```python
@app.route("/admin")
```

Only admins should access this route.

---

## Session-Based Security

Store logged-in user information:

```python
session["user_id"]
session["username"]
session["role"]
```

---

## Access Control

Admin:

```plaintext
Access Granted
```

User:

```plaintext
Access Denied
```

---

# 💻 Example Code

## app.py

```python
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for,
    session,
    flash
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"
)

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
        db.String(100)
    )

    role = db.Column(
        db.String(20),
        default="user"
    )

@app.route("/")
def home():

    return redirect(
        url_for("login")
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:

            session["user_id"] = user.id
            session["username"] = user.username
            session["role"] = user.role

            flash(
                "Login Successful",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid Credentials",
            "danger"
        )

    return render_template(
        "login.html"
    )

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    return render_template(
        "dashboard.html"
    )

@app.route("/admin")
def admin_dashboard():

    if "user_id" not in session:

        flash(
            "Please Login First",
            "danger"
        )

        return redirect(
            url_for("login")
        )

    if session["role"] != "admin":

        flash(
            "Access Denied",
            "danger"
        )

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "admin.html"
    )

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged Out Successfully",
        "success"
    )

    return redirect(
        url_for("login")
    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
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

<h1>Login</h1>

<form method="POST">

    <input
        type="text"
        name="username"
        placeholder="Username"
        required
    >

    <input
        type="password"
        name="password"
        placeholder="Password"
        required
    >

    <button type="submit">
        Login
    </button>

</form>

</body>
</html>
```

---

## templates/dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>

<h1>User Dashboard</h1>

<p>
Welcome,
{{ session.username }}
</p>

<p>
Role:
<strong>
{{ session.role }}
</strong>
</p>

<a href="/admin">
Admin Dashboard
</a>

<br><br>

<a href="/logout">
Logout
</a>

</body>
</html>
```

---

## templates/admin.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Admin Dashboard</title>
</head>
<body>

<h1>Admin Dashboard</h1>

<h3>
Protected Area
</h3>

<p>
Only Admins Can Access This Page
</p>

<ul>

    <li>Manage Users</li>

    <li>Manage Posts</li>

    <li>View Reports</li>

    <li>System Settings</li>

</ul>

<a href="/dashboard">
Back To Dashboard
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

h1 {

    margin-bottom: 20px;
}

a {

    text-decoration: none;

    color: blue;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Login system
- User sessions
- Role verification
- Protected admin dashboard
- Access denied protection
- Logout functionality

Example Workflow:

```plaintext
Login
   ↓
User Dashboard
   ↓
Admin Route Requested
   ↓
Role Check
   ↓
Admin ?
   ↓
YES → Admin Dashboard

NO → Access Denied
```

---

# 🔥 Real-World Use Cases

Protected Admin Dashboards are used in:

- E-commerce Websites
- Blogging Platforms
- CRM Systems
- School Portals
- SaaS Products
- Inventory Systems
- Enterprise Applications

---

# ⚠️ Security Improvements For Production

This project uses simple role checking for learning.

Production applications should also use:

### Password Hashing

```python
generate_password_hash()
check_password_hash()
```

---

### Flask-Login

```python
Flask-Login
```

for session management.

---

### Decorators

Example:

```python
@admin_required
```

for reusable admin protection.

---

### CSRF Protection

Using:

```python
Flask-WTF
```

---

# 🚀 Skills Gained

After completing Day 87, you can:

- Build protected admin areas
- Implement authorization
- Restrict routes
- Manage user permissions
- Create secure dashboards
- Build multi-role applications

---

# ✅ Summary

In Day 87, I learned how to build a Protected Admin Dashboard in Flask.

I implemented:

- User authentication
- Role-based authorization
- Protected routes
- Admin-only pages
- Session-based security

This is a crucial backend concept used in nearly every production application and prepares me for:

### Day 88 – Flask Password Reset Basics

---
