# Day 86 – Flask User Roles

## 📌 Overview

In this project, I learned how to implement User Roles in Flask applications.

Most real-world applications have different types of users with different permissions.

Examples:

- Admin
- Moderator
- Editor
- Customer
- Student
- Teacher

Instead of giving every user the same permissions, we can assign roles and control access accordingly.

In this project:

- Users can register
- Each user has a role
- Admin users get special privileges
- Normal users have limited access
- Role-based access control is introduced

---

## 🛠 What I Did

- Added a role field to the User model
- Assigned default roles during registration
- Created Admin and User roles
- Displayed role information on the dashboard
- Restricted admin-only routes
- Implemented role-based authorization

---

## 📂 Folder Structure

```plaintext
flask-user-roles/
│
├── app.py
├── database.db
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── admin.html
│
└── static/
    └── style.css
```

---

## 🧠 Key Concepts Learned

### User Roles

Each user has a role:

```python
role = db.Column(
    db.String(20),
    default="user"
)
```

---

### Role-Based Access Control (RBAC)

Different users have different permissions.

Example:

```plaintext
Admin → Full Access

User → Limited Access
```

---

### Authorization

Authentication answers:

```plaintext
Who are you?
```

Authorization answers:

```plaintext
What are you allowed to do?
```

---

### Protected Routes

Only admins should access:

```plaintext
/admin
```

---

### Session-Based Access

Using:

```python
session["role"]
```

to determine permissions.

---

## 💻 Example Code

### app.py

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

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"
)

db = SQLAlchemy(app)

# User Model
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

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = User(
            username=username,
            password=password,
            role="user"
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration Successful",
            "success"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "register.html"
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
def admin():

    if "user_id" not in session:

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

    return redirect(
        url_for("login")
    )

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

---

### templates/dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>

<h1>Welcome {{ session.username }}</h1>

<p>
Role:
<strong>
{{ session.role }}
</strong>
</p>

<a href="/admin">
Admin Panel
</a>

<br><br>

<a href="/logout">
Logout
</a>

</body>
</html>
```

---

### templates/admin.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Admin Panel</title>
</head>
<body>

<h1>Admin Dashboard</h1>

<p>
Only Admins Can Access This Page
</p>

<a href="/dashboard">
Back
</a>

</body>
</html>
```

---

### static/style.css

```css
body {
    font-family: Arial, sans-serif;
    padding: 40px;
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

## ▶️ Output / Result

Successfully implemented:

- User roles
- Admin role
- User role
- Session-based authorization
- Protected routes
- Access control

Example Workflow:

```plaintext
Register User
      ↓
Role Assigned
      ↓
Login
      ↓
Dashboard
      ↓
Admin Route Check
      ↓
Access Granted / Denied
```

---

## 🔥 Real-World Use Cases

User roles are used in:

- Admin dashboards
- E-commerce websites
- Learning Management Systems
- CRM systems
- Blogging platforms
- Social media apps
- Company portals

---

## ⚠️ Security Note

For learning purposes we used:

```python
password = db.Column(
    db.String(100)
)
```

In production, passwords should NEVER be stored as plain text.

Instead use:

```python
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
```

---

## 🚀 Skills Gained

After completing Day 86, you can:

- Create user roles
- Implement RBAC
- Restrict routes
- Manage permissions
- Protect admin pages
- Build multi-user applications

---

## ✅ Summary

In Day 86, I learned how to implement User Roles in Flask applications.

I built a role-based authentication system where:

- Users have assigned roles
- Admins have special permissions
- Users have restricted access
- Protected routes enforce authorization

This concept is fundamental for building secure and scalable Flask applications and prepares me for the next lesson:

### Day 87 – Flask Protected Admin Dashboard

---
