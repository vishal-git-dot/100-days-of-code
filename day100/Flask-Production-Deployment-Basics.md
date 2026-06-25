# Day 100 – Flask Production Deployment Basics

## 📌 Overview

Today marks **Day 100** of the Flask Learning Journey.

Over the previous 99 days, I learned:

- Flask Fundamentals
- Routing
- Templates
- Forms
- Validation
- Sessions
- Authentication
- CRUD Applications
- Databases
- Search / Sort / Filter
- Relationships
- File Uploads
- Security
- REST APIs
- Blueprints
- Application Factory Pattern
- Logging
- Error Handling

Now it's time to learn how Flask applications are deployed in production.

A Flask application running with:

```bash
python app.py
```

is suitable for development only.

Production environments require:

- WSGI Servers
- Reverse Proxies
- Environment Variables
- Security Configuration
- Deployment Platforms

In this project:

- Learned production deployment concepts
- Configured Gunicorn
- Used environment variables
- Prepared Flask applications for production
- Explored deployment platforms

---

# 🛠 What I Did

- Learned deployment architecture
- Installed Gunicorn
- Created production configuration
- Used environment variables
- Disabled debug mode
- Prepared application for hosting
- Explored deployment options

---

# 📂 Folder Structure

```plaintext
flask-production-deployment/
│
├── run.py
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── config.py
│
├── requirements.txt
│
├── .env
│
├── Procfile
│
└── README.md
```

---

# 🧠 Key Concepts Learned

## Development vs Production

### Development

```bash
python app.py
```

Features:

```plaintext
Debug Mode
Auto Reload
Developer Friendly
```

---

### Production

Uses:

```plaintext
Gunicorn
uWSGI
Nginx
Cloud Platforms
```

Features:

```plaintext
Secure
Fast
Scalable
Stable
```

---

# Why Not Use Flask Development Server?

Flask's built-in server is designed only for development.

Example:

```python
app.run(debug=True)
```

Problems:

```plaintext
Not Secure
Single Process
Not Optimized
```

Therefore production applications use:

```plaintext
WSGI Servers
```

---

# What Is WSGI?

WSGI means:

```plaintext
Web Server Gateway Interface
```

It connects:

```plaintext
Web Server
      ↓
Flask Application
```

Common WSGI Servers:

- Gunicorn
- uWSGI
- Waitress

---

# What Is Gunicorn?

Gunicorn is a production WSGI server.

Install:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn run:app
```

Where:

```plaintext
run = run.py
app = Flask Instance
```

---

# Environment Variables

Never store secrets directly inside code.

❌ Bad

```python
SECRET_KEY = "123456"
```

---

✅ Good

```python
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
```

Store inside:

```plaintext
.env
```

---

# Production Workflow

```plaintext
User Request
       ↓
Nginx
       ↓
Gunicorn
       ↓
Flask App
       ↓
Database
       ↓
Response
```

---

# 💻 Example Code

## requirements.txt

```txt
Flask
gunicorn
python-dotenv
```

---

## .env

```env
SECRET_KEY=my-super-secret-key

FLASK_ENV=production
```

---

## app/config.py

```python
import os

from dotenv import (
    load_dotenv
)

load_dotenv()

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY"
    )

    DEBUG = False
```

---

## app/routes.py

```python
from flask import (
    Blueprint
)

main = Blueprint(
    "main",
    __name__
)

@main.route("/")
def home():

    return (
        "Production Ready Flask App"
    )
```

---

## app/__init__.py

```python
from flask import Flask

from app.config import Config

from app.routes import main

def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    app.register_blueprint(
        main
    )

    return app
```

---

## run.py

```python
from app import create_app

app = create_app()

if __name__ == "__main__":

    app.run()
```

---

## Procfile

```plaintext
web: gunicorn run:app
```

Used by:

```plaintext
Render
Railway
Heroku
```

deployment platforms.

---

# ▶️ Running In Development

```bash
python run.py
```

---

# ▶️ Running In Production

Install Gunicorn:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn run:app
```

Example:

```bash
gunicorn -w 4 run:app
```

Meaning:

```plaintext
4 Worker Processes
```

---

# 🌍 Deployment Platforms

## Render

Features:

- Free Tier
- GitHub Integration
- Easy Deployment

---

## Railway

Features:

- Fast Setup
- GitHub Deployment
- Automatic Builds

---

## Heroku

Features:

- Popular Platform
- Easy Deployment
- Production Ready

---

## DigitalOcean

Features:

- VPS Hosting
- Full Control
- Scalable

---

## AWS

Features:

- Enterprise Hosting
- High Scalability
- Cloud Infrastructure

---

# 🚀 Example Deployment Process

```plaintext
GitHub Repository
          ↓
Push Code
          ↓
Connect To Render
          ↓
Automatic Build
          ↓
Install Requirements
          ↓
Run Gunicorn
          ↓
Deploy Flask App
```

---

# 🔒 Production Security Checklist

## Disable Debug Mode

❌ Bad

```python
DEBUG = True
```

---

✅ Good

```python
DEBUG = False
```

---

## Use Environment Variables

Never hardcode:

```plaintext
Passwords
API Keys
Secret Keys
```

---

## Use HTTPS

Always enable:

```plaintext
SSL Certificates
```

---

## Validate Inputs

Protect against:

```plaintext
SQL Injection
XSS
CSRF
```

---

## Secure Authentication

Use:

```plaintext
Password Hashing
JWT
Secure Sessions
```

---

# 📊 Deployment Architecture

```plaintext
Internet
    │
    ▼
Nginx
    │
    ▼
Gunicorn
    │
    ▼
Flask Application
    │
    ▼
Database
```

---

# 🔥 Real-World Production Stack

A professional Flask application often uses:

```plaintext
Flask
SQLAlchemy
PostgreSQL
Gunicorn
Nginx
Redis
Docker
GitHub Actions
AWS / Render
```

This stack powers many SaaS and enterprise applications.

---

# ⚠️ Common Mistakes

## Leaving Debug Mode Enabled

❌ Bad

```python
DEBUG = True
```

in production.

---

## Hardcoding Secrets

❌ Bad

```python
SECRET_KEY = "123"
```

---

## Using Flask Dev Server

❌ Bad

```bash
python app.py
```

for production hosting.

---

## Not Logging Errors

Always configure:

```python
logging
```

before deployment.

---

## Ignoring Environment Variables

Production apps should load:

```plaintext
Secrets
API Keys
Database URLs
```

from environment variables.

---

# 🚀 Skills Gained

After completing Day 100, you can:

- Understand deployment architecture
- Configure production Flask apps
- Use Gunicorn
- Manage environment variables
- Prepare applications for hosting
- Follow deployment best practices
- Deploy Flask applications professionally

---

# 🏆 Flask Journey Completed

Over 100 days, I learned:

### Flask Fundamentals

- Routing
- Templates
- Static Files

### Forms & Authentication

- WTForms
- Sessions
- Login Systems
- Validation

### Database Development

- SQLite
- SQLAlchemy
- CRUD Operations
- Relationships

### Advanced Features

- Search
- Sorting
- Filtering
- File Uploads

### Security

- Roles
- Protected Routes
- Environment Variables

### API Development

- REST APIs
- JSON Responses
- CRUD APIs
- API Authentication

### Architecture

- Blueprints
- Application Factory Pattern
- Modular Structure

### Production Skills

- Error Handling
- Logging
- Deployment Basics

---

# ✅ Summary

In Day 100, I learned the fundamentals of deploying Flask applications to production environments.

I implemented:

- Gunicorn
- Environment Variables
- Production Configuration
- Deployment Architecture
- Security Best Practices

This completes the Flask Learning Journey and provides a strong foundation for building and deploying professional Flask applications.

---

# 🎯 What's Next?

After Day 100, begin building real-world projects:

### Project 1 – Blog CMS

- Authentication
- CRUD Posts
- Admin Dashboard

### Project 2 – Task Manager

- User Accounts
- Tasks
- Categories

### Project 3 – Inventory System

- Products
- Stock Management
- Reports

### Project 4 – CRM System

- Customers
- Leads
- Notes
- Analytics

### Project 5 – Full REST API Backend

- JWT Authentication
- CRUD APIs
- PostgreSQL
- Production Deployment

---
