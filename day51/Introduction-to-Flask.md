# Day 51 – Introduction to Flask & Installation

## 📌 Overview

Today I started learning **Flask**, a lightweight Python web framework used to build web applications quickly and easily.

Unlike Django, Flask is a **micro-framework**, meaning it provides only the essentials and gives developers more control and flexibility.

In this lesson, I learned how to:
- Install Flask
- Create a basic Flask application
- Run a development server
- Display output in the browser

---

## 🛠 What I Did

- Installed Flask using pip
- Created a simple Flask application (`app.py`)
- Defined a basic route (`/`)
- Returned a simple response from the server
- Ran the Flask development server
- Viewed output in the browser

---

## 📂 Folder Structure

```
Day51/
│
├── app.py
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Flask** → A lightweight web framework for Python
- **Micro-framework** → Minimal features, more flexibility
- `Flask(__name__)` → Creates the Flask application
- `@app.route()` → Defines URL routes
- `app.run()` → Starts the development server

---

## 💻 Example Code

### app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ▶️ Output / Result

- Run the app using:

```bash
python app.py
```

- Open browser and visit:

```
http://127.0.0.1:5000/
```

- Output displayed:

```
Hello, Flask!
```

The Flask development server runs locally and responds to requests from the browser.

---

## ✅ Summary

- Successfully installed Flask
- Created and ran a basic Flask app
- Understood routing and server basics
- Displayed first Flask output in browser

---

✅ **Day 51 Completed**

Today I learned the basics of **Flask setup and created my first web application using Flask**, marking the beginning of my Flask journey.
