# Day 98 – Flask Error Handling

## 📌 Overview

In this project, I learned how to handle errors properly in Flask applications.

No application is perfect. Users can enter invalid data, request pages that do not exist, or trigger unexpected server errors.

Without proper error handling:

- Applications crash
- Users see confusing messages
- APIs return inconsistent responses
- Debugging becomes difficult

Error handling allows applications to:

- Recover gracefully
- Show friendly error pages
- Return meaningful API responses
- Improve user experience
- Simplify debugging

In this project:

- Created custom error pages
- Handled common HTTP errors
- Built API error responses
- Logged exceptions
- Improved application reliability

---

# 🛠 What I Did

- Handled 404 errors
- Handled 500 errors
- Created custom error pages
- Built API error responses
- Used try-except blocks
- Logged exceptions
- Improved debugging workflow

---

# 📂 Folder Structure

```plaintext
flask-error-handling/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── 404.html
│   └── 500.html
│
├── static/
│   └── style.css
│
├── logs/
│   └── app.log
│
└── requirements.txt
```

---

# 🧠 Key Concepts Learned

## What Is Error Handling?

Error handling allows applications to manage failures without crashing.

Example:

```plaintext
User Requests Page
        ↓
Page Doesn't Exist
        ↓
404 Error
        ↓
Custom Error Page
```

---

## Types of Errors

### Client Errors

Problems caused by user requests.

Examples:

```plaintext
404 Not Found
401 Unauthorized
403 Forbidden
400 Bad Request
```

---

### Server Errors

Problems caused by the application.

Examples:

```plaintext
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
```

---

## Common HTTP Status Codes

| Code | Meaning |
|--------|----------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## Custom Error Handlers

Flask provides:

```python
@app.errorhandler()
```

Example:

```python
@app.errorhandler(404)
def not_found(error):
    return render_template(
        "404.html"
    ), 404
```

---

## Try-Except Blocks

Used to catch exceptions.

Example:

```python
try:
    result = 10 / 0

except Exception as e:
    print(e)
```

---

## Logging Errors

Instead of printing errors:

```python
print(error)
```

Use:

```python
logging.error(error)
```

This creates permanent logs.

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
    render_template,
    jsonify
)

import logging

app = Flask(__name__)

# -------------------
# Logging Setup
# -------------------

logging.basicConfig(

    filename="logs/app.log",

    level=logging.ERROR,

    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    )
)

# -------------------
# Home Route
# -------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# -------------------
# Example Error Route
# -------------------

@app.route("/crash")
def crash():

    try:

        result = 10 / 0

        return str(result)

    except Exception as error:

        logging.error(error)

        return jsonify({

            "success": False,

            "message":
            "Something Went Wrong"

        }), 500

# -------------------
# 404 Handler
# -------------------

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404

# -------------------
# 500 Handler
# -------------------

@app.errorhandler(500)
def internal_error(error):

    return render_template(
        "500.html"
    ), 500

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
        Flask Error Handling
    </title>

</head>

<body>

    <h1>
        Home Page
    </h1>

    <p>
        Flask Error Handling Demo
    </p>

</body>

</html>
```

---

## templates/404.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        404 Not Found
    </title>

</head>

<body>

    <h1>
        404
    </h1>

    <p>
        Page Not Found
    </p>

    <a href="/">
        Go Home
    </a>

</body>

</html>
```

---

## templates/500.html

```html
<!DOCTYPE html>
<html>

<head>

    <title>
        Server Error
    </title>

</head>

<body>

    <h1>
        500
    </h1>

    <p>
        Internal Server Error
    </p>

    <a href="/">
        Go Home
    </a>

</body>

</html>
```

---

## static/style.css

```css
body {

    font-family: Arial, sans-serif;

    text-align: center;

    margin-top: 100px;
}

h1 {

    font-size: 60px;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- 404 Error Handling
- 500 Error Handling
- Custom Error Pages
- API Error Responses
- Logging System
- Exception Handling

Example Workflow:

```plaintext
User Request
      ↓
Error Occurs
      ↓
Error Handler
      ↓
Log Error
      ↓
Friendly Response
```

---

# 🔥 API Error Handling Example

Professional APIs return structured errors.

Example:

```json
{
    "success": false,
    "message": "User Not Found"
}
```

Status Code:

```plaintext
404
```

---

Example:

```json
{
    "success": false,
    "message": "Internal Server Error"
}
```

Status Code:

```plaintext
500
```

---

# 📄 Log File Example

```plaintext
2026-06-01 ERROR division by zero

2026-06-01 ERROR database connection failed

2026-06-01 ERROR invalid request
```

Log files help developers diagnose problems quickly.

---

# ⚠️ Common Mistakes

## Showing Raw Errors To Users

❌ Bad

```plaintext
Traceback (most recent call last)
...
```

Users should never see internal errors.

---

## Not Logging Errors

❌ Bad

```python
except:
    pass
```

---

✅ Good

```python
logging.error(error)
```

---

## Returning HTML In APIs

API endpoints should return:

```json
{
    "error": "Not Found"
}
```

instead of HTML pages.

---

## Ignoring Exceptions

Never silently ignore:

```python
except:
    pass
```

Always handle errors properly.

---

# 🚀 Skills Gained

After completing Day 98, you can:

- Handle Flask errors
- Create custom error pages
- Use try-except blocks
- Return API error responses
- Log application errors
- Improve debugging
- Build reliable applications

---

# 📊 Error Handling Flow

```plaintext
User Request
      │
      ▼
Application
      │
      ▼
Error Occurs
      │
      ▼
Error Handler
      │
      ├── Log Error
      │
      ├── Return HTML Page
      │
      └── Return JSON Error
      │
      ▼
User Receives Response
```

---

# ✅ Summary

In Day 98, I learned how to handle errors professionally in Flask applications.

I implemented:

- 404 Error Pages
- 500 Error Pages
- Exception Handling
- Logging
- API Error Responses

Error handling is critical for building stable, maintainable, and production-ready Flask applications.

This prepares me for:

### Day 99 – Flask Logging System

---
