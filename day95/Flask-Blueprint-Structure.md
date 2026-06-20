# Day 95 – Flask Blueprint Structure

## 📌 Overview

In this project, I learned how to organize large Flask applications using Blueprints.

So far, every Flask application has used a single `app.py` file.

While this works for small projects, real-world applications quickly become difficult to manage when all routes, models, forms, and business logic are stored in one file.

Flask Blueprints solve this problem by allowing applications to be divided into smaller, reusable modules.

Examples:

- Authentication Module
- User Management Module
- Product Module
- Blog Module
- Admin Module
- API Module

In this project:

- Created Flask Blueprints
- Separated routes into modules
- Registered blueprints
- Organized project structure
- Improved application scalability

---

# 🛠 What I Did

- Created a blueprint package
- Added separate route modules
- Registered blueprints
- Organized templates
- Organized project files
- Improved maintainability
- Built a modular Flask application

---

# 📂 Folder Structure

```plaintext
flask-blueprints/
│
├── app.py
│
├── auth/
│   ├── __init__.py
│   └── routes.py
│
├── main/
│   ├── __init__.py
│   └── routes.py
│
├── templates/
│   ├── home.html
│   └── login.html
│
├── static/
│   └── style.css
│
└── requirements.txt
```

---

# 🧠 Key Concepts Learned

## What is a Blueprint?

A Blueprint is a way to organize Flask applications into multiple components.

Instead of:

```plaintext
app.py
 ├── 500+ lines
 ├── All Routes
 ├── All Logic
 └── Difficult To Maintain
```

We can create:

```plaintext
auth/
main/
admin/
api/
```

Each module manages its own routes.

---

## Why Use Blueprints?

Benefits:

- Cleaner code
- Easier maintenance
- Better scalability
- Team collaboration
- Reusable modules

---

## Creating a Blueprint

Example:

```python
from flask import Blueprint

main = Blueprint(
    "main",
    __name__
)
```

---

## Registering a Blueprint

Blueprints must be registered inside the Flask app.

Example:

```python
app.register_blueprint(
    main
)
```

---

## URL Prefixes

Blueprints can have URL prefixes.

Example:

```python
app.register_blueprint(
    auth,
    url_prefix="/auth"
)
```

Routes become:

```plaintext
/auth/login
/auth/logout
/auth/register
```

---

# 💻 Example Code

## requirements.txt

```txt
Flask
```

---

## app.py

```python
from flask import Flask

from auth.routes import auth
from main.routes import main

app = Flask(__name__)

app.secret_key = "secret-key"

app.register_blueprint(
    main
)

app.register_blueprint(
    auth,
    url_prefix="/auth"
)

if __name__ == "__main__":

    app.run(debug=True)
```

---

## auth/routes.py

```python
from flask import (
    Blueprint,
    render_template
)

auth = Blueprint(
    "auth",
    __name__
)

@auth.route("/login")
def login():

    return render_template(
        "login.html"
    )

@auth.route("/register")
def register():

    return "Register Page"
```

---

## auth/__init__.py

```python
# Blueprint Package
```

---

## main/routes.py

```python
from flask import (
    Blueprint,
    render_template
)

main = Blueprint(
    "main",
    __name__
)

@main.route("/")
def home():

    return render_template(
        "home.html"
    )

@main.route("/about")
def about():

    return "About Page"
```

---

## main/__init__.py

```python
# Blueprint Package
```

---

## templates/home.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        Flask Blueprints
    </title>

</head>

<body>

    <h1>
        Home Page
    </h1>

    <a href="/auth/login">
        Login
    </a>

</body>

</html>
```

---

## templates/login.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        Login
    </title>

</head>

<body>

    <h1>
        Login Page
    </h1>

    <form>

        <input
            type="text"
            placeholder="Username"
        >

        <br><br>

        <input
            type="password"
            placeholder="Password"
        >

        <br><br>

        <button>
            Login
        </button>

    </form>

</body>

</html>
```

---

## static/style.css

```css
body {

    font-family: Arial, sans-serif;

    padding: 40px;
}

h1 {

    margin-bottom: 20px;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Blueprint Structure
- Modular Routes
- URL Prefixes
- Route Separation
- Organized Codebase
- Scalable Architecture

Example Workflow:

```plaintext
Request
   ↓
Blueprint
   ↓
Route Handler
   ↓
Template
   ↓
Response
```

---

# 🔥 Real-World Project Structure

Small Project:

```plaintext
app.py
```

Large Project:

```plaintext
project/
│
├── auth/
├── admin/
├── api/
├── products/
├── orders/
├── users/
├── templates/
└── static/
```

This is how production applications are typically organized.

---

# ⚠️ Common Mistakes

## Forgetting To Register Blueprint

❌ Wrong

```python
main = Blueprint(...)
```

but never registering it.

---

✅ Correct

```python
app.register_blueprint(
    main
)
```

---

## Circular Imports

Avoid:

```python
from app import app
```

inside blueprint files.

---

Use:

```python
Blueprint
```

instead.

---

## Keeping Everything In app.py

Blueprints exist to avoid:

```plaintext
1000+ line app.py files
```

---

# 🚀 Skills Gained

After completing Day 95, you can:

- Create Flask Blueprints
- Organize large applications
- Separate routes
- Use URL prefixes
- Build modular Flask projects
- Improve maintainability
- Structure scalable applications

---

# 📊 Blueprint Architecture

```plaintext
Flask App
    │
    ├── Main Blueprint
    │      ├── Home
    │      └── About
    │
    ├── Auth Blueprint
    │      ├── Login
    │      └── Register
    │
    ├── Admin Blueprint
    │      ├── Dashboard
    │      └── Users
    │
    └── API Blueprint
           ├── Users API
           └── Products API
```

---

# ✅ Summary

In Day 95, I learned how Flask Blueprints help organize applications into reusable modules.

I implemented:

- Blueprint Creation
- Blueprint Registration
- Route Separation
- URL Prefixes
- Modular Project Structure

Blueprints are essential for medium and large Flask applications because they improve maintainability, scalability, and developer productivity.

This prepares me for:

### Day 96 – Flask Application Factory Pattern
