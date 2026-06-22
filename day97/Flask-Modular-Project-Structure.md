# Day 97 – Flask Modular Project Structure

## 📌 Overview

In this project, I learned how to organize a Flask application using a fully modular project structure.

In Day 95, we introduced Blueprints.

In Day 96, we implemented the Application Factory Pattern.

Today, we combine those concepts into a professional project architecture used in real-world Flask applications.

Large applications become difficult to maintain when everything is stored inside a few files.

A modular structure separates:

- Routes
- Models
- Forms
- Services
- Extensions
- Configuration
- Templates
- Static Files

This makes applications easier to:

- Maintain
- Scale
- Debug
- Test
- Deploy

In this project:

- Built a modular Flask architecture
- Organized code into reusable components
- Separated application concerns
- Improved maintainability
- Followed production-level project design

---

# 🛠 What I Did

- Created a modular project structure
- Separated models
- Separated routes
- Separated forms
- Separated configuration
- Separated extensions
- Organized templates and static files
- Followed production architecture

---

# 📂 Folder Structure

```plaintext
flask-modular-project/
│
├── run.py
│
├── app/
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   └── api/
│       ├── __init__.py
│       └── routes.py
│
├── templates/
│   ├── home.html
│   └── login.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│
├── instance/
│   └── app.db
│
├── migrations/
│
├── tests/
│
├── requirements.txt
│
└── .env
```

---

# 🧠 Key Concepts Learned

## What Is a Modular Project?

A modular project separates application features into independent modules.

Instead of:

```plaintext
app.py
 ├── Routes
 ├── Models
 ├── Forms
 ├── APIs
 ├── Config
 └── Everything Else
```

We create:

```plaintext
auth/
main/
api/
```

Each module handles its own functionality.

---

## Why Use Modular Structure?

Benefits:

### Better Maintainability

```plaintext
Easy To Understand
```

---

### Easier Debugging

```plaintext
Locate Problems Faster
```

---

### Team Collaboration

```plaintext
Multiple Developers
Can Work Independently
```

---

### Scalability

Add new features without touching existing modules.

---

# Application Components

## Configuration

Stores:

```plaintext
Secret Keys
Database URLs
API Keys
Settings
```

File:

```plaintext
config.py
```

---

## Extensions

Stores Flask extensions.

Examples:

```python
SQLAlchemy
LoginManager
Migrate
```

File:

```plaintext
extensions.py
```

---

## Models

Stores database models.

Example:

```python
User
Post
Category
```

File:

```plaintext
models.py
```

---

## Blueprints

Each feature gets its own blueprint.

Example:

```plaintext
auth/
main/
api/
```

---

## Forms

Forms stay inside their module.

Example:

```plaintext
auth/forms.py
```

---

# 💻 Example Code

## requirements.txt

```txt
Flask
Flask-SQLAlchemy
Flask-WTF
```

---

## run.py

```python
from app import create_app

app = create_app()

if __name__ == "__main__":

    app.run(debug=True)
```

---

## app/__init__.py

```python
from flask import Flask

from app.config import Config

from app.extensions import db

def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    db.init_app(app)

    from app.main.routes import main

    from app.auth.routes import auth

    from app.api.routes import api

    app.register_blueprint(
        main
    )

    app.register_blueprint(
        auth,
        url_prefix="/auth"
    )

    app.register_blueprint(
        api,
        url_prefix="/api"
    )

    return app
```

---

## app/config.py

```python
class Config:

    SECRET_KEY = (
        "secret-key"
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///app.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = (
        False
    )
```

---

## app/extensions.py

```python
from flask_sqlalchemy import (
    SQLAlchemy
)

db = SQLAlchemy()
```

---

## app/models.py

```python
from app.extensions import db

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True
    )

    email = db.Column(
        db.String(120),
        unique=True
    )
```

---

## app/main/routes.py

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
```

---

## app/auth/forms.py

```python
from flask_wtf import (
    FlaskForm
)

from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

class LoginForm(
    FlaskForm
):

    username = StringField(
        "Username"
    )

    password = PasswordField(
        "Password"
    )

    submit = SubmitField(
        "Login"
    )
```

---

## app/auth/routes.py

```python
from flask import (
    Blueprint,
    render_template
)

from app.auth.forms import (
    LoginForm
)

auth = Blueprint(
    "auth",
    __name__
)

@auth.route("/login")
def login():

    form = LoginForm()

    return render_template(
        "login.html",
        form=form
    )
```

---

## app/api/routes.py

```python
from flask import (
    Blueprint,
    jsonify
)

api = Blueprint(
    "api",
    __name__
)

@api.route("/users")
def users():

    return jsonify({

        "message":
        "Users API"

    })
```

---

## templates/home.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        Flask Modular Project
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

<h1>Login Form</h1>

<form>

    {{ form.username }}

    <br><br>

    {{ form.password }}

    <br><br>

    {{ form.submit }}

</form>

</body>

</html>
```

---

# ▶️ Output / Result

Successfully implemented:

- Modular Structure
- Application Factory Pattern
- Blueprints
- Forms
- Models
- Extensions
- API Module

Example Workflow:

```plaintext
Request
   ↓
Blueprint
   ↓
Route
   ↓
Business Logic
   ↓
Template/API
   ↓
Response
```

---

# 🔥 Real-World Enterprise Structure

```plaintext
project/
│
├── app/
│   ├── auth/
│   ├── users/
│   ├── admin/
│   ├── products/
│   ├── orders/
│   ├── payments/
│   ├── notifications/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── forms/
│   └── utils/
│
├── migrations/
├── tests/
├── docs/
├── static/
└── templates/
```

This is similar to how production SaaS applications are structured.

---

# ⚠️ Common Mistakes

## Huge app.py Files

❌ Bad

```plaintext
2000+ Lines
```

inside one file.

---

## Mixing Features

❌ Bad

```plaintext
Auth Routes
Product Routes
API Routes
```

inside the same file.

---

## No Extensions File

Extensions should be centralized.

Good:

```plaintext
extensions.py
```

---

## Hardcoded Config

Avoid:

```python
SECRET_KEY = "123"
```

Use:

```python
.env
```

files.

---

# 🚀 Skills Gained

After completing Day 97, you can:

- Build modular Flask applications
- Organize large projects
- Separate concerns properly
- Use Application Factory Pattern
- Manage extensions
- Create scalable architectures
- Follow industry standards

---

# 📊 Modular Architecture Flow

```plaintext
Client Request
      │
      ▼
Blueprint
      │
      ▼
Route Handler
      │
      ▼
Models / Services
      │
      ▼
Database
      │
      ▼
Response
```

---

# ✅ Summary

In Day 97, I learned how to structure Flask applications using a modular architecture.

I implemented:

- Application Factory Pattern
- Blueprints
- Models
- Forms
- Extensions
- API Modules
- Config Separation

This architecture is widely used in professional Flask projects because it makes applications easier to scale, maintain, test, and deploy.

This prepares me for:

### Day 98 – Flask Error Handling
