# Day 94 – Flask API Authentication

## 📌 Overview

In this project, I learned how API Authentication works in Flask applications.

In previous lessons, we built APIs that anyone could access.

However, real-world APIs often contain sensitive data and must verify the identity of users before granting access.

Examples:

- GitHub API
- Stripe API
- PayPal API
- Twitter API
- OpenAI API
- Banking APIs

Authentication ensures that only authorized users can access protected resources.

In this project:

- Built login API endpoints
- Generated authentication tokens
- Protected API routes
- Verified user identity
- Restricted unauthorized access

---

# 🛠 What I Did

- Created user login API
- Implemented token-based authentication
- Protected API endpoints
- Validated user credentials
- Generated access tokens
- Verified tokens on requests
- Returned authentication responses

---

# 📂 Folder Structure

```plaintext
flask-api-authentication/
│
├── app.py
├── requirements.txt
│
└── README.md
```

---

# 🧠 Key Concepts Learned

## What is API Authentication?

API Authentication verifies:

```plaintext
Who is making the request?
```

Without authentication:

```plaintext
Anyone Can Access Data
```

With authentication:

```plaintext
Only Authorized Users
```

can access protected resources.

---

## Authentication vs Authorization

### Authentication

```plaintext
Who are you?
```

Example:

```plaintext
Login
Username
Password
```

---

### Authorization

```plaintext
What can you access?
```

Example:

```plaintext
Admin Dashboard
User Profile
Reports
```

---

## Token-Based Authentication

Instead of storing sessions, APIs commonly use:

```plaintext
Access Tokens
```

Workflow:

```plaintext
Login
   ↓
Generate Token
   ↓
Send Token To Client
   ↓
Client Stores Token
   ↓
Token Sent With Requests
   ↓
Server Verifies Token
```

---

## API Headers

Tokens are typically sent in request headers.

Example:

```http
Authorization: Bearer token123
```

---

## Protected Endpoints

Example:

```http
GET /profile
```

Requires:

```plaintext
Valid Token
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
    jsonify,
    request
)

import secrets

app = Flask(__name__)

users = [

    {
        "id": 1,
        "username": "admin",
        "password": "123456"
    }
]

tokens = {}

# -------------------
# HOME
# -------------------

@app.route("/")
def home():

    return jsonify({

        "message":
        "Flask API Authentication"

    })


# -------------------
# LOGIN
# -------------------

@app.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    username = data.get(
        "username"
    )

    password = data.get(
        "password"
    )

    for user in users:

        if (
            user["username"] == username
            and
            user["password"] == password
        ):

            token = secrets.token_hex(16)

            tokens[token] = user

            return jsonify({

                "success": True,

                "token": token

            }), 200

    return jsonify({

        "success": False,

        "message":
        "Invalid Credentials"

    }), 401


# -------------------
# PROTECTED PROFILE
# -------------------

@app.route(
    "/profile",
    methods=["GET"]
)
def profile():

    auth_header = request.headers.get(
        "Authorization"
    )

    if not auth_header:

        return jsonify({

            "success": False,

            "message":
            "Token Required"

        }), 401

    token = auth_header.replace(
        "Bearer ",
        ""
    )

    if token not in tokens:

        return jsonify({

            "success": False,

            "message":
            "Invalid Token"

        }), 401

    user = tokens[token]

    return jsonify({

        "success": True,

        "user": {

            "id": user["id"],

            "username":
            user["username"]
        }

    })


if __name__ == "__main__":

    app.run(debug=True)
```

---

# ▶️ API Endpoints

## Login Endpoint

```http
POST /login
```

Request:

```json
{
    "username": "admin",
    "password": "123456"
}
```

Response:

```json
{
    "success": true,
    "token": "abc123xyz..."
}
```

---

## Protected Profile Endpoint

```http
GET /profile
```

Header:

```http
Authorization: Bearer abc123xyz...
```

Response:

```json
{
    "success": true,
    "user": {
        "id": 1,
        "username": "admin"
    }
}
```

---

## Missing Token

Response:

```json
{
    "success": false,
    "message": "Token Required"
}
```

Status:

```plaintext
401 Unauthorized
```

---

## Invalid Token

Response:

```json
{
    "success": false,
    "message": "Invalid Token"
}
```

Status:

```plaintext
401 Unauthorized
```

---

# ▶️ Testing With Postman

## Login Request

```http
POST
http://127.0.0.1:5000/login
```

Body:

```json
{
    "username": "admin",
    "password": "123456"
}
```

Copy returned token.

---

## Access Protected Route

```http
GET
http://127.0.0.1:5000/profile
```

Headers:

```http
Authorization: Bearer YOUR_TOKEN
```

---

# 🔐 JWT Authentication (Industry Standard)

The token system above is for learning purposes.

Professional APIs usually use:

```plaintext
JWT
```

Meaning:

```plaintext
JSON Web Token
```

Popular library:

```bash
pip install flask-jwt-extended
```

JWT Workflow:

```plaintext
Login
   ↓
Generate JWT
   ↓
Send JWT
   ↓
Store JWT
   ↓
Protected Requests
   ↓
Verify JWT
```

---

# ▶️ Output / Result

Successfully implemented:

- Login API
- Token Generation
- Token Verification
- Protected Routes
- Authorization Headers
- Authentication Workflow

Example Flow:

```plaintext
User Login
      ↓
Credentials Verified
      ↓
Token Generated
      ↓
Client Stores Token
      ↓
Protected Request
      ↓
Token Verified
      ↓
Access Granted
```

---

# 🔥 Real-World Use Cases

API Authentication is used in:

- GitHub API
- Stripe API
- PayPal API
- OpenAI API
- Banking Systems
- SaaS Platforms
- Mobile Applications
- Cloud Services

---

# ⚠️ Common Mistakes

## Sending Passwords On Every Request

❌ Bad

```plaintext
Username + Password Every Time
```

---

✅ Good

```plaintext
Use Access Token
```

---

## Storing Plain Passwords

❌ Bad

```python
password = "123456"
```

---

✅ Good

```python
generate_password_hash()
```

---

## Missing Token Validation

Always verify:

```python
if token not in tokens:
```

before granting access.

---

## Exposing Sensitive Data

Never return:

```json
{
    "password": "123456"
}
```

in API responses.

---

# 🚀 Skills Gained

After completing Day 94, you can:

- Build authenticated APIs
- Generate access tokens
- Protect API endpoints
- Verify authorization headers
- Implement token-based authentication
- Understand JWT concepts
- Secure backend services

---

# 📊 Authentication Flow

```plaintext
Client
  ↓
Login Request
  ↓
Flask API
  ↓
Verify Credentials
  ↓
Generate Token
  ↓
Return Token
  ↓
Protected Request
  ↓
Verify Token
  ↓
Access Resource
```

---

# ✅ Summary

In Day 94, I learned how API Authentication works in Flask.

I implemented:

- Login API
- Token-Based Authentication
- Protected Routes
- Authorization Headers
- Token Validation

Authentication is one of the most important concepts in backend development because it protects sensitive resources and user data.

This prepares me for:

### Day 95 – Flask Blueprint Structure
