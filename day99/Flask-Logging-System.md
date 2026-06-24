# Day 99 – Flask Logging System

## 📌 Overview

In this project, I learned how to implement a professional logging system in Flask applications.

As applications grow, simply using:

```python
print()
```

statements becomes insufficient for debugging and monitoring.

Production applications need a reliable way to record:

- Errors
- User Actions
- Security Events
- Application Activity
- Database Issues
- API Requests

This is where logging becomes essential.

Logging helps developers:

- Track application behavior
- Identify bugs
- Monitor performance
- Audit user activity
- Debug production issues

In this project:

- Configured Flask logging
- Created log files
- Logged application events
- Logged errors and warnings
- Built a production-ready logging system

---

# 🛠 What I Did

- Configured Python logging
- Created log files
- Logged user activity
- Logged application events
- Logged warnings
- Logged errors
- Logged critical failures
- Built structured logging

---

# 📂 Folder Structure

```plaintext
flask-logging-system/
│
├── app.py
│
├── logs/
│   ├── app.log
│   ├── error.log
│   └── access.log
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Key Concepts Learned

## What Is Logging?

Logging is the process of recording application events.

Example:

```plaintext
User Logged In
Database Connected
API Request Received
File Uploaded
Error Occurred
```

Instead of displaying information on screen:

```python
print("User Logged In")
```

we store it permanently:

```python
logging.info(
    "User Logged In"
)
```

---

## Why Logging Is Important

Without logging:

```plaintext
Application Crashes
No Idea Why
```

With logging:

```plaintext
Application Crashes
↓
Check Logs
↓
Find Cause
↓
Fix Issue
```

---

## Logging Levels

Python logging provides multiple levels.

---

### DEBUG

Detailed debugging information.

```python
logging.debug(
    "Debug Message"
)
```

---

### INFO

Normal application events.

```python
logging.info(
    "User Logged In"
)
```

---

### WARNING

Potential problems.

```python
logging.warning(
    "Storage Almost Full"
)
```

---

### ERROR

Errors that affect functionality.

```python
logging.error(
    "Database Connection Failed"
)
```

---

### CRITICAL

Severe failures.

```python
logging.critical(
    "Application Shutdown"
)
```

---

# Logging Hierarchy

```plaintext
DEBUG
   ↓
INFO
   ↓
WARNING
   ↓
ERROR
   ↓
CRITICAL
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
from flask import (
    Flask,
    render_template
)

import logging

app = Flask(__name__)

# -----------------------
# Logging Configuration
# -----------------------

logging.basicConfig(

    filename="logs/app.log",

    level=logging.INFO,

    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    )
)

# -----------------------
# Home Route
# -----------------------

@app.route("/")
def home():

    logging.info(
        "Home Page Visited"
    )

    return render_template(
        "index.html"
    )

# -----------------------
# Login Route
# -----------------------

@app.route("/login")
def login():

    logging.info(
        "Login Page Accessed"
    )

    return "Login Page"

# -----------------------
# Warning Example
# -----------------------

@app.route("/warning")
def warning():

    logging.warning(
        "Warning Route Triggered"
    )

    return "Warning Logged"

# -----------------------
# Error Example
# -----------------------

@app.route("/error")
def error():

    try:

        result = 10 / 0

        return str(result)

    except Exception as err:

        logging.error(
            f"Error: {err}"
        )

        return (
            "Error Logged",
            500
        )

# -----------------------
# Critical Example
# -----------------------

@app.route("/critical")
def critical():

    logging.critical(
        "Critical Failure Triggered"
    )

    return "Critical Event Logged"

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
        Flask Logging
    </title>

</head>

<body>

    <h1>
        Flask Logging System
    </h1>

    <p>
        Logging Demo Application
    </p>

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
```

---

# ▶️ Output / Result

Successfully implemented:

- Application Logging
- Error Logging
- Warning Logging
- Critical Logging
- Structured Log Files
- Production Monitoring

Example Workflow:

```plaintext
User Action
      ↓
Application Event
      ↓
Log Entry Created
      ↓
Stored In Log File
      ↓
Developer Reviews Logs
```

---

# 📄 Sample Log File

## logs/app.log

```plaintext
2026-06-24 10:00:01 INFO Home Page Visited

2026-06-24 10:01:05 INFO Login Page Accessed

2026-06-24 10:03:20 WARNING Warning Route Triggered

2026-06-24 10:04:15 ERROR division by zero

2026-06-24 10:05:40 CRITICAL Critical Failure Triggered
```

---

# 🔥 Multiple Log Files

Production applications often separate logs.

Example:

```plaintext
logs/
│
├── access.log
├── error.log
├── security.log
├── payment.log
└── app.log
```

Benefits:

```plaintext
Better Organization
Faster Debugging
Easier Monitoring
```

---

# Advanced Logging Example

```python
import logging

logger = logging.getLogger(
    "myapp"
)

logger.info(
    "Application Started"
)
```

This approach is commonly used in large applications.

---

# Security Logging

Important events to log:

```plaintext
Login Attempts
Password Resets
Failed Logins
Role Changes
Account Deletions
```

Example:

```python
logging.warning(
    "Failed Login Attempt"
)
```

---

# API Logging

For APIs:

```plaintext
Request Method
Request URL
Response Code
Execution Time
```

Example:

```python
logging.info(
    "GET /users - 200"
)
```

---

# ⚠️ Common Mistakes

## Using print() Instead Of Logging

❌ Bad

```python
print(
    "User Logged In"
)
```

---

✅ Good

```python
logging.info(
    "User Logged In"
)
```

---

## Logging Sensitive Data

❌ Never Log

```plaintext
Passwords
Credit Cards
API Secrets
Tokens
```

Example:

```python
logging.info(
    password
)
```

Never do this.

---

## Ignoring Errors

❌ Bad

```python
except:
    pass
```

---

✅ Good

```python
except Exception as err:

    logging.error(err)
```

---

## Using Only One Log Level

Use:

```plaintext
INFO
WARNING
ERROR
CRITICAL
```

appropriately.

---

# 🚀 Skills Gained

After completing Day 99, you can:

- Configure Flask logging
- Create log files
- Log application activity
- Log warnings and errors
- Monitor production systems
- Debug applications efficiently
- Build maintainable backend systems

---

# 📊 Logging Architecture

```plaintext
User Request
      │
      ▼
Flask Application
      │
      ▼
Event Occurs
      │
      ▼
Logger
      │
      ├── INFO
      ├── WARNING
      ├── ERROR
      └── CRITICAL
      │
      ▼
Log Files
      │
      ▼
Developer Monitoring
```

---

# 🌍 Real-World Logging Tools

Professional applications often integrate logging with:

- ELK Stack (Elasticsearch, Logstash, Kibana)
- Grafana
- Prometheus
- Sentry
- Datadog
- New Relic

These tools provide:

```plaintext
Real-Time Monitoring
Error Tracking
Performance Analytics
```

---

# ✅ Summary

In Day 99, I learned how to build a professional logging system in Flask.

I implemented:

- Logging Configuration
- Log Files
- Error Logging
- Warning Logging
- Critical Logging
- Activity Tracking

Logging is one of the most important production skills because it helps developers monitor, debug, and maintain applications efficiently.

This prepares me for:

### Day 100 – Flask Production Deployment Basics
