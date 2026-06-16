# Day 91 – Flask REST API Basics

## 📌 Overview

In this project, I learned the fundamentals of building REST APIs using Flask.

So far, all Flask applications returned HTML pages.

Now we move into API development, where Flask returns data instead of webpages.

APIs allow applications to communicate with each other.

Examples:

- Mobile Apps
- React Applications
- Angular Applications
- Vue Applications
- Third-Party Integrations
- Backend Services

In this project:

- Created a REST API
- Returned JSON responses
- Built API endpoints
- Handled HTTP requests
- Introduced API architecture

---

# 🛠 What I Did

- Created API routes
- Returned JSON data
- Built GET endpoints
- Learned REST principles
- Tested APIs in browser and Postman
- Structured API responses
- Created a simple user API

---

# 📂 Folder Structure

```plaintext
flask-rest-api-basics/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Key Concepts Learned

## What is an API?

API stands for:

```plaintext
Application Programming Interface
```

An API allows different applications to communicate.

Example:

```plaintext
Mobile App
      ↓
Flask API
      ↓
Database
```

---

## What is REST?

REST stands for:

```plaintext
Representational State Transfer
```

REST APIs use:

```plaintext
HTTP Methods
```

to perform operations.

---

## HTTP Methods

### GET

Retrieve data.

```http
GET /users
```

---

### POST

Create data.

```http
POST /users
```

---

### PUT

Update data.

```http
PUT /users/1
```

---

### DELETE

Delete data.

```http
DELETE /users/1
```

---

## What is JSON?

JSON stands for:

```plaintext
JavaScript Object Notation
```

Example:

```json
{
    "id": 1,
    "name": "John"
}
```

JSON is the standard format used by APIs.

---

## Flask jsonify()

Flask provides:

```python
jsonify()
```

to return JSON responses.

Example:

```python
return jsonify(data)
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
    jsonify
)

app = Flask(__name__)

users = [

    {
        "id": 1,
        "name": "Vishal",
        "email": "vishal@example.com"
    },

    {
        "id": 2,
        "name": "John",
        "email": "john@example.com"
    },

    {
        "id": 3,
        "name": "Sarah",
        "email": "sarah@example.com"
    }
]

@app.route("/")
def home():

    return jsonify({

        "message":
        "Welcome To Flask REST API"

    })

@app.route("/users")
def get_users():

    return jsonify(users)

@app.route("/users/<int:user_id>")
def get_user(user_id):

    for user in users:

        if user["id"] == user_id:

            return jsonify(user)

    return jsonify({

        "error":
        "User Not Found"

    }), 404

if __name__ == "__main__":

    app.run(debug=True)
```

---

# ▶️ API Endpoints

## Home Endpoint

```http
GET /
```

Response:

```json
{
    "message": "Welcome To Flask REST API"
}
```

---

## Get All Users

```http
GET /users
```

Response:

```json
[
    {
        "id": 1,
        "name": "Vishal",
        "email": "vishal@example.com"
    }
]
```

---

## Get Single User

```http
GET /users/1
```

Response:

```json
{
    "id": 1,
    "name": "Vishal",
    "email": "vishal@example.com"
}
```

---

## User Not Found

```http
GET /users/100
```

Response:

```json
{
    "error": "User Not Found"
}
```

Status Code:

```plaintext
404
```

---

# ▶️ Output / Result

Successfully implemented:

- REST API
- API Endpoints
- JSON Responses
- GET Requests
- Dynamic Routes
- Error Responses

Example Workflow:

```plaintext
Client Request
       ↓
Flask API
       ↓
Process Request
       ↓
Return JSON
       ↓
Client Receives Data
```

---

# 🔥 Real-World Use Cases

REST APIs are used in:

- Mobile Applications
- React Frontends
- Angular Applications
- SaaS Products
- Payment Gateways
- Authentication Systems
- Microservices

---

# ⚠️ Common Mistakes

## Returning Python Objects Directly

❌ Bad:

```python
return users
```

---

✅ Good:

```python
return jsonify(users)
```

---

## Missing Status Codes

❌ Bad:

```python
return jsonify(error)
```

---

✅ Good:

```python
return jsonify(error), 404
```

---

## Mixing HTML and API Responses

API routes should return:

```json
JSON
```

not:

```html
HTML Templates
```

---

# 🚀 Skills Gained

After completing Day 91, you can:

- Build Flask APIs
- Create API endpoints
- Return JSON responses
- Handle GET requests
- Create dynamic routes
- Structure API data
- Build backend services

---

# 📊 REST API Architecture

```plaintext
Frontend
(React / Mobile App)
          ↓
       API Request
          ↓
      Flask API
          ↓
      Database
          ↓
      JSON Response
          ↓
Frontend Updates UI
```

---

# ✅ Summary

In Day 91, I learned the fundamentals of Flask REST APIs.

I implemented:

- API Endpoints
- JSON Responses
- GET Requests
- Dynamic Routes
- Error Handling

This marks the beginning of modern backend development because APIs are the foundation of:

- Mobile Apps
- Single Page Applications
- SaaS Products
- Microservices

This prepares me for:

### Day 92 – JSON Responses in Flask
