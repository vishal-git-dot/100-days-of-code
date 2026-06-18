# Day 93 – Flask API CRUD Operations

## 📌 Overview

In this project, I learned how to implement full CRUD Operations in a Flask REST API.

CRUD stands for:

```plaintext
C → Create
R → Read
U → Update
D → Delete
```

CRUD operations form the foundation of almost every backend application.

Examples:

- User Management Systems
- Blog Applications
- Inventory Systems
- Task Managers
- E-Commerce Platforms
- CRM Systems

In this project:

- Created API endpoints
- Added new records
- Retrieved records
- Updated records
- Deleted records
- Returned JSON responses
- Used proper HTTP methods

---

# 🛠 What I Did

- Built a REST API
- Implemented Create operation
- Implemented Read operation
- Implemented Update operation
- Implemented Delete operation
- Used JSON request data
- Returned proper status codes

---

# 📂 Folder Structure

```plaintext
flask-api-crud/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Key Concepts Learned

## What is CRUD?

CRUD represents the four basic database operations.

| Operation | Purpose |
|------------|----------|
| Create | Add new data |
| Read | Retrieve data |
| Update | Modify existing data |
| Delete | Remove data |

---

## HTTP Methods and CRUD

### Create

```http
POST /users
```

---

### Read All

```http
GET /users
```

---

### Read One

```http
GET /users/1
```

---

### Update

```http
PUT /users/1
```

---

### Delete

```http
DELETE /users/1
```

---

## Request Body

When creating or updating data, clients send JSON.

Example:

```json
{
    "name": "Vishal",
    "email": "vishal@example.com"
}
```

---

## request.get_json()

Used to access incoming JSON data.

Example:

```python
data = request.get_json()
```

---

## Status Codes

### 200 OK

```plaintext
Request Successful
```

---

### 201 Created

```plaintext
Resource Created
```

---

### 404 Not Found

```plaintext
Resource Not Found
```

---

### 400 Bad Request

```plaintext
Invalid Data
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
    }
]

# --------------------
# HOME
# --------------------

@app.route("/")
def home():

    return jsonify({

        "message":
        "Flask CRUD API"

    })


# --------------------
# GET ALL USERS
# --------------------

@app.route("/users", methods=["GET"])
def get_users():

    return jsonify({

        "success": True,

        "count": len(users),

        "data": users

    })


# --------------------
# GET SINGLE USER
# --------------------

@app.route(
    "/users/<int:user_id>",
    methods=["GET"]
)
def get_user(user_id):

    for user in users:

        if user["id"] == user_id:

            return jsonify({

                "success": True,

                "data": user

            })

    return jsonify({

        "success": False,

        "message":
        "User Not Found"

    }), 404


# --------------------
# CREATE USER
# --------------------

@app.route(
    "/users",
    methods=["POST"]
)
def create_user():

    data = request.get_json()

    new_user = {

        "id": len(users) + 1,

        "name": data["name"],

        "email": data["email"]
    }

    users.append(
        new_user
    )

    return jsonify({

        "success": True,

        "message":
        "User Created",

        "data": new_user

    }), 201


# --------------------
# UPDATE USER
# --------------------

@app.route(
    "/users/<int:user_id>",
    methods=["PUT"]
)
def update_user(user_id):

    data = request.get_json()

    for user in users:

        if user["id"] == user_id:

            user["name"] = (
                data.get(
                    "name",
                    user["name"]
                )
            )

            user["email"] = (
                data.get(
                    "email",
                    user["email"]
                )
            )

            return jsonify({

                "success": True,

                "message":
                "User Updated",

                "data": user

            })

    return jsonify({

        "success": False,

        "message":
        "User Not Found"

    }), 404


# --------------------
# DELETE USER
# --------------------

@app.route(
    "/users/<int:user_id>",
    methods=["DELETE"]
)
def delete_user(user_id):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return jsonify({

                "success": True,

                "message":
                "User Deleted"

            })

    return jsonify({

        "success": False,

        "message":
        "User Not Found"

    }), 404


if __name__ == "__main__":

    app.run(debug=True)
```

---

# ▶️ API Endpoints

## Get All Users

```http
GET /users
```

Response:

```json
{
    "success": true,
    "count": 2,
    "data": [...]
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
    "data": {
        "id": 1,
        "name": "Vishal"
    }
}
```

---

## Create User

```http
POST /users
```

Request Body:

```json
{
    "name": "Sarah",
    "email": "sarah@example.com"
}
```

Response:

```json
{
    "success": true,
    "message": "User Created"
}
```

Status:

```plaintext
201 Created
```

---

## Update User

```http
PUT /users/1
```

Request Body:

```json
{
    "name": "Updated Vishal"
}
```

Response:

```json
{
    "success": true,
    "message": "User Updated"
}
```

---

## Delete User

```http
DELETE /users/1
```

Response:

```json
{
    "success": true,
    "message": "User Deleted"
}
```

---

# ▶️ Testing With Postman

### Create User

```http
POST
http://127.0.0.1:5000/users
```

Body:

```json
{
    "name": "Alex",
    "email": "alex@example.com"
}
```

---

### Update User

```http
PUT
http://127.0.0.1:5000/users/1
```

Body:

```json
{
    "name": "Updated Name"
}
```

---

### Delete User

```http
DELETE
http://127.0.0.1:5000/users/1
```

---

# ▶️ Output / Result

Successfully implemented:

- Create API
- Read API
- Update API
- Delete API
- JSON Requests
- JSON Responses
- HTTP Status Codes

Example Workflow:

```plaintext
Client Request
       ↓
Flask Route
       ↓
CRUD Operation
       ↓
JSON Response
       ↓
Client Receives Result
```

---

# 🔥 Real-World Use Cases

CRUD APIs power:

- User Management Systems
- Blog Platforms
- Inventory Systems
- Task Managers
- CRM Applications
- Mobile Applications
- SaaS Products

---

# ⚠️ Common Mistakes

## Missing Request Validation

❌ Bad:

```python
data["name"]
```

without checking existence.

---

✅ Better:

```python
data.get("name")
```

---

## Wrong HTTP Method

Creating data should use:

```http
POST
```

not:

```http
GET
```

---

## Missing Status Codes

Always return:

```python
201
```

for created resources.

---

## Not Handling Missing Records

Always return:

```python
404
```

when data doesn't exist.

---

# 🚀 Skills Gained

After completing Day 93, you can:

- Build CRUD APIs
- Create API endpoints
- Handle JSON requests
- Return JSON responses
- Use HTTP methods correctly
- Build backend services
- Develop RESTful APIs

---

# 📊 CRUD API Flow

```plaintext
Frontend / Postman
          ↓
      API Request
          ↓
       Flask API
          ↓
      CRUD Logic
          ↓
      JSON Response
          ↓
Frontend Receives Data
```

---

# ✅ Summary

In Day 93, I learned how to build complete CRUD APIs using Flask.

I implemented:

- Create Operations
- Read Operations
- Update Operations
- Delete Operations
- JSON Requests
- JSON Responses
- HTTP Status Codes

CRUD APIs are the backbone of modern backend development and are used in almost every web and mobile application.

This prepares me for:

### Day 94 – Flask API Authentication
