# Day 92 – JSON Responses in Flask

## 📌 Overview

In this project, I learned how Flask handles JSON responses and why JSON is the most important data format in modern web development.

In Day 91, we created our first REST API.

Today, we focus specifically on JSON responses, JSON objects, JSON arrays, status codes, and API response structures.

Almost every modern application communicates using JSON.

Examples:

- React Applications
- Mobile Apps
- REST APIs
- SaaS Products
- Payment Gateways
- Authentication Systems

In this project:

- Returned JSON data
- Built structured API responses
- Used HTTP status codes
- Created success and error responses
- Learned API response standards

---

# 🛠 What I Did

- Created JSON endpoints
- Returned JSON objects
- Returned JSON arrays
- Added HTTP status codes
- Created success responses
- Created error responses
- Built API-friendly responses

---

# 📂 Folder Structure

```plaintext
flask-json-responses/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Key Concepts Learned

## What is JSON?

JSON stands for:

```plaintext
JavaScript Object Notation
```

JSON is a lightweight format used to exchange data.

Example:

```json
{
    "name": "Vishal",
    "age": 21
}
```

---

## JSON Object

Contains key-value pairs.

Example:

```json
{
    "id": 1,
    "name": "John"
}
```

---

## JSON Array

Contains multiple values.

Example:

```json
[
    {
        "id": 1
    },
    {
        "id": 2
    }
]
```

---

## Flask jsonify()

Flask provides:

```python
jsonify()
```

for converting Python data into JSON.

Example:

```python
return jsonify(data)
```

---

## HTTP Status Codes

### 200 OK

Request successful.

```python
return jsonify(data), 200
```

---

### 201 Created

Resource created successfully.

```python
return jsonify(data), 201
```

---

### 400 Bad Request

Invalid client request.

```python
return jsonify(error), 400
```

---

### 404 Not Found

Resource not found.

```python
return jsonify(error), 404
```

---

### 500 Internal Server Error

Server failure.

```python
return jsonify(error), 500
```

---

## API Response Structure

Professional APIs often return:

```json
{
    "success": true,
    "message": "User Found",
    "data": {}
}
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

        "success": True,

        "message":
        "Welcome To Flask JSON API"

    }), 200


@app.route("/users")
def get_users():

    return jsonify({

        "success": True,

        "count": len(users),

        "data": users

    }), 200


@app.route("/users/<int:user_id>")
def get_user(user_id):

    for user in users:

        if user["id"] == user_id:

            return jsonify({

                "success": True,

                "message":
                "User Found",

                "data": user

            }), 200

    return jsonify({

        "success": False,

        "message":
        "User Not Found"

    }), 404


@app.route("/health")
def health_check():

    return jsonify({

        "status": "UP",

        "server":
        "Running"

    }), 200


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
    "success": true,
    "message": "Welcome To Flask JSON API"
}
```

---

## Get All Users

```http
GET /users
```

Response:

```json
{
    "success": true,
    "count": 3,
    "data": [
        {
            "id": 1,
            "name": "Vishal"
        }
    ]
}
```

---

## Get Single User

```http
GET /users/1
```

Response:

```json
{
    "success": true,
    "message": "User Found",
    "data": {
        "id": 1,
        "name": "Vishal"
    }
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
    "success": false,
    "message": "User Not Found"
}
```

Status:

```plaintext
404
```

---

## Health Check Endpoint

```http
GET /health
```

Response:

```json
{
    "status": "UP",
    "server": "Running"
}
```

---

# ▶️ Output / Result

Successfully implemented:

- JSON Objects
- JSON Arrays
- HTTP Status Codes
- Structured API Responses
- Error Responses
- Health Check API

Example Workflow:

```plaintext
Client Request
       ↓
Flask Route
       ↓
Create JSON
       ↓
Add Status Code
       ↓
Return Response
       ↓
Client Receives JSON
```

---

# 🔥 Real-World Use Cases

JSON responses are used in:

- Mobile Applications
- React Frontends
- Vue Applications
- Angular Applications
- REST APIs
- Payment APIs
- Authentication Systems
- Cloud Services

---

# ⚠️ Common Mistakes

## Returning Python Dictionaries

❌ Bad:

```python
return {
    "message": "Hello"
}
```

---

✅ Better:

```python
return jsonify({
    "message": "Hello"
})
```

---

## Missing Status Codes

❌ Bad:

```python
return jsonify(data)
```

---

✅ Good:

```python
return jsonify(data), 200
```

---

## Inconsistent Response Formats

Bad:

```json
{
    "name": "John"
}
```

then

```json
{
    "user": {}
}
```

Keep responses consistent.

---

## Exposing Sensitive Data

Never return:

```json
{
    "password": "123456"
}
```

or:

```json
{
    "secret_key": "abcd"
}
```

---

# 🚀 Skills Gained

After completing Day 92, you can:

- Return JSON responses
- Use jsonify()
- Build API-friendly responses
- Use status codes correctly
- Create structured API data
- Handle success and error responses

---

# 📊 JSON API Flow

```plaintext
Browser / Mobile App
          ↓
      API Request
          ↓
      Flask Route
          ↓
      Python Data
          ↓
      jsonify()
          ↓
      JSON Response
          ↓
Browser / App Receives Data
```

---

# ✅ Summary

In Day 92, I learned how JSON responses work in Flask APIs.

I implemented:

- JSON Objects
- JSON Arrays
- Status Codes
- Error Handling
- Structured Responses

JSON is the foundation of modern API development and is used by virtually every frontend framework and mobile application.

This prepares me for:

### Day 93 – API CRUD Operations
