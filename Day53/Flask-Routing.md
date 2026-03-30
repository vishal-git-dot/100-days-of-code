# Day 53 – Flask Routing

## 📌 Overview

Today I learned about **Flask Routing**, which is used to map URLs to specific functions in a Flask application.

Routing allows us to define different pages in a web app. Each URL is connected to a function using the **`@app.route()` decorator**.

I also learned how to create **dynamic routes**, where parts of the URL can be passed as variables.

---

## 🛠 What I Did

- Used `@app.route()` to create multiple routes
- Created different pages (home, about, contact)
- Learned how Flask handles URLs
- Implemented **dynamic routing** using URL parameters
- Displayed dynamic content in the browser

---

## 📂 Folder Structure

```
Day53/
│
├── app.py
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Routing** → Mapping URLs to Python functions
- `@app.route()` → Defines a route
- Each route must have a **unique URL**
- **Dynamic routes** allow passing values via URL
- URL parameters can be used inside functions

---

## 💻 Example Code

### app.py

```python
from flask import Flask

app = Flask(__name__)

# Static Routes
@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/contact")
def contact():
    return "Contact Page"


# Dynamic Route
@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"


# Dynamic Route with Type
@app.route("/age/<int:age>")
def age(age):
    return f"Your age is {age}"


if __name__ == "__main__":
    app.run(debug=True)
```

---

## ▶️ Output / Result

Run the app:

```bash
python app.py
```

Open browser:

### Static Routes

```
/ → Welcome to Home Page
/about → This is About Page
/contact → Contact Page
```

### Dynamic Routes

```
/user/John → Hello, John!
/age/25 → Your age is 25
```

---

## ✅ Summary

- Learned how to define routes using `@app.route()`
- Created multiple pages in Flask
- Implemented dynamic URL routing
- Used variables inside routes

---

✅ **Day 53 Completed**

Today I learned how to **handle URL routing in Flask, including dynamic routes**, allowing creation of multiple pages and dynamic web content.
