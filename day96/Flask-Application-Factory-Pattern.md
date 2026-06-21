# Day 96 – Flask Application Factory Pattern

## 📌 Overview

In this project, I learned how to use the Application Factory Pattern in Flask.

As Flask applications grow, directly creating the application object inside `app.py` becomes difficult to maintain.

The Application Factory Pattern solves this problem by creating the Flask application through a function instead of creating it globally.

This pattern is widely used in:

- Large Flask Applications
- Production Systems
- SaaS Platforms
- REST APIs
- Enterprise Applications

It also works perfectly with:

- Blueprints
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- Testing Frameworks

In this project:

- Created a Flask application factory
- Separated configuration from application creation
- Registered blueprints dynamically
- Improved project scalability
- Followed production-ready architecture

---

# 🛠 What I Did

- Created a factory function
- Moved app creation into a package
- Registered blueprints inside factory
- Organized configuration files
- Improved maintainability
- Prepared project for larger applications
- Followed Flask best practices

---

# 📂 Folder Structure

```plaintext
flask-application-factory/
│
├── run.py
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   └── auth/
│       ├── __init__.py
│       └── routes.py
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

## Traditional Flask Structure

Small applications often use:

```python
app = Flask(__name__)
```

inside:

```plaintext
app.py
```

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"
```

This becomes difficult to maintain as the project grows.

---

## Application Factory Pattern

Instead of:

```python
app = Flask(__name__)
```

globally,

we create:

```python
def create_app():
```

which returns a Flask application instance.

Example:

```python
def create_app():

    app = Flask(__name__)

    return app
```

---

## Benefits

### Better Organization

```plaintext
Config
Blueprints
Database
Extensions
```

can all be initialized separately.

---

### Easier Testing

You can create multiple app instances.

Example:

```python
app = create_app()
```

for testing environments.

---

### Production Ready

Used in most professional Flask applications.

---

## Factory Workflow

```plaintext
run.py
    ↓
create_app()
    ↓
Load Config
    ↓
Register Blueprints
    ↓
Initialize Extensions
    ↓
Return App
```

---

# 💻 Example Code

## requirements.txt

```txt
Flask
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

def create_app():

    app = Flask(__name__)

    app.config.from_object(
        "app.config.Config"
    )

    from app.main.routes import main

    from app.auth.routes import auth

    app.register_blueprint(
        main
    )

    app.register_blueprint(
        auth,
        url_prefix="/auth"
    )

    return app
```

---

## app/config.py

```python
class Config:

    SECRET_KEY = (
        "my-secret-key"
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

@main.route("/about")
def about():

    return "About Page"
```

---

## app/main/__init__.py

```python
# Main Blueprint Package
```

---

## app/auth/routes.py

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

## app/auth/__init__.py

```python
# Auth Blueprint Package
```

---

## templates/home.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        Flask Application Factory
    </title>

</head>

<body>

    <h1>
        Flask Application Factory Pattern
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

- Application Factory Pattern
- Modular Flask Structure
- Dynamic App Creation
- Blueprint Registration
- Configuration Separation
- Production Architecture

Example Workflow:

```plaintext
run.py
   ↓
create_app()
   ↓
Load Configuration
   ↓
Register Blueprints
   ↓
Create Flask App
   ↓
Run Server
```

---

# 🔥 Real-World Production Structure

```plaintext
project/
│
├── run.py
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── extensions.py
│   │
│   ├── auth/
│   ├── admin/
│   ├── users/
│   ├── api/
│   └── products/
│
├── migrations/
├── tests/
├── static/
└── templates/
```

Most professional Flask applications follow a structure similar to this.

---

# ⚠️ Common Mistakes

## Creating App Globally

❌ Old Approach

```python
app = Flask(__name__)
```

inside a large application.

---

✅ Better

```python
def create_app():
```

Factory Pattern.

---

## Registering Blueprints Outside Factory

Always register blueprints inside:

```python
create_app()
```

---

## Hardcoding Configuration

Avoid:

```python
app.secret_key = "secret"
```

Use:

```python
config.py
```

or environment variables.

---

## Circular Imports

Bad:

```python
from app import app
```

inside blueprints.

---

Use Blueprint imports correctly.

---

# 🚀 Skills Gained

After completing Day 96, you can:

- Use the Application Factory Pattern
- Build scalable Flask applications
- Register blueprints dynamically
- Separate configuration
- Organize large projects
- Follow production-ready architecture
- Prepare applications for deployment

---

# 📊 Application Factory Architecture

```plaintext
run.py
   │
   ▼
create_app()
   │
   ├── Load Config
   │
   ├── Initialize Extensions
   │
   ├── Register Blueprints
   │
   ├── Connect Database
   │
   └── Return App
            │
            ▼
       Flask Server
```

---

# ✅ Summary

In Day 96, I learned how to use the Flask Application Factory Pattern.

I implemented:

- Factory Functions
- Dynamic Application Creation
- Configuration Management
- Blueprint Registration
- Scalable Project Structure

The Application Factory Pattern is one of the most important Flask architecture patterns and is used in most production-level Flask applications.

This prepares me for:

### Day 97 – Flask Modular Project Structure
