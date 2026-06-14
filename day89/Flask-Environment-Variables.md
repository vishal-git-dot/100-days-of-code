# Day 89 – Flask Environment Variables

## 📌 Overview

In this project, I learned how to use Environment Variables in Flask applications.

As applications grow, sensitive information should never be hardcoded into source code.

Examples of sensitive information:

- Secret Keys
- Database URLs
- API Keys
- SMTP Credentials
- Cloud Storage Keys

Environment Variables allow us to separate configuration from code and improve application security.

In this project:

- Moved secret values outside source code
- Used `.env` files
- Loaded environment variables in Flask
- Protected sensitive application settings

---

# 🛠 What I Did

- Installed python-dotenv
- Created a `.env` file
- Stored sensitive values securely
- Loaded environment variables
- Configured Flask using environment variables
- Removed hardcoded secrets
- Improved application security

---

# 📂 Folder Structure

```plaintext
flask-environment-variables/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# 🧠 Key Concepts Learned

## What Are Environment Variables?

Environment Variables store configuration values outside the application code.

Example:

```plaintext
SECRET_KEY=mysecretkey
```

---

## Why Use Environment Variables?

Instead of:

```python
app.secret_key = "my-secret-key"
```

Use:

```python
app.secret_key = os.getenv("SECRET_KEY")
```

Benefits:

- More secure
- Easier deployment
- Better project organization

---

## The .env File

Stores configuration values.

Example:

```env
SECRET_KEY=mysecretkey123

DATABASE_URL=sqlite:///database.db

API_KEY=sampleapikey
```

---

## Loading Variables

Using:

```python
from dotenv import load_dotenv
```

and

```python
load_dotenv()
```

---

## Accessing Variables

Using:

```python
os.getenv()
```

Example:

```python
secret_key = os.getenv("SECRET_KEY")
```

---

# 💻 Example Code

## .env

```env
SECRET_KEY=my-super-secret-key

DATABASE_URL=sqlite:///database.db

APP_NAME=Flask Environment Demo

API_KEY=sample-api-key
```

---

## .gitignore

```gitignore
.env

__pycache__/

instance/

*.pyc

venv/
```

---

## requirements.txt

```txt
Flask

python-dotenv
```

---

## app.py

```python
from flask import (
    Flask,
    render_template
)

from dotenv import load_dotenv

import os

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Get values from .env

app.config["SECRET_KEY"] = (
    os.getenv("SECRET_KEY")
)

app.config["DATABASE_URL"] = (
    os.getenv("DATABASE_URL")
)

APP_NAME = os.getenv(
    "APP_NAME"
)

API_KEY = os.getenv(
    "API_KEY"
)

@app.route("/")
def home():

    return render_template(
        "index.html",
        app_name=APP_NAME,
        database_url=app.config["DATABASE_URL"]
    )

if __name__ == "__main__":

    app.run(debug=True)
```

---

## templates/index.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        Flask Environment Variables
    </title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='style.css') }}"
    >

</head>

<body>

<div class="container">

    <h1>
        {{ app_name }}
    </h1>

    <p>
        Environment Variables Loaded Successfully
    </p>

    <p>
        Database:
        {{ database_url }}
    </p>

</div>

</body>

</html>
```

---

## static/style.css

```css
body {

    background: #f4f4f4;

    font-family: Arial, sans-serif;
}

.container {

    width: 80%;

    margin: auto;

    margin-top: 100px;

    text-align: center;
}

h1 {

    margin-bottom: 20px;
}

p {

    font-size: 18px;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Environment Variables
- .env file support
- Secret key protection
- Config management
- Externalized application settings

Example Workflow:

```plaintext
Create .env
      ↓
Store Secrets
      ↓
Load Variables
      ↓
Use In Flask App
      ↓
Secure Configuration
```

---

# 🔥 Real-World Use Cases

Environment Variables are used in:

- Production Flask Apps
- SaaS Platforms
- Cloud Deployments
- APIs
- E-Commerce Systems
- Authentication Systems
- Docker Containers

---

# ⚠️ Common Mistakes

## Committing .env to GitHub

Bad:

```plaintext
GitHub Repository
     └── .env
```

Anyone can see your secrets.

Always add:

```gitignore
.env
```

to `.gitignore`.

---

## Hardcoding Secrets

Bad:

```python
app.secret_key = "my-secret-key"
```

Good:

```python
app.secret_key = os.getenv(
    "SECRET_KEY"
)
```

---

## Missing Variables

Always provide fallback values:

```python
os.getenv(
    "SECRET_KEY",
    "default-key"
)
```

---

# 🚀 Skills Gained

After completing Day 89, you can:

- Use environment variables
- Secure application secrets
- Configure Flask applications
- Manage deployment settings
- Use python-dotenv
- Prepare applications for production

---

# ✅ Summary

In Day 89, I learned how to manage application configuration using Environment Variables.

I implemented:

- `.env` files
- `python-dotenv`
- Secure secret storage
- Flask configuration management

This is a critical production skill because professional applications should never expose sensitive information in source code.

This prepares me for:

### Day 90 – Flask Security Best Practices
