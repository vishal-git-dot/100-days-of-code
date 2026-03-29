# Day 52 – Flask App Structure

## 📌 Overview

Today I learned about the **basic structure of a Flask application** and how Flask apps are organized.

Unlike Django, Flask does not enforce a strict project structure. It gives developers the **flexibility to organize files as needed**, starting from a simple single-file app and scaling to larger structures.

I also explored **debug mode** and how Flask handles application execution.

---

## 🛠 What I Did

- Understood the minimal Flask app structure
- Explored how `app.py` acts as the main file
- Learned about **debug mode**
- Ran the Flask app with debug enabled
- Observed automatic server reload on code changes

---

## 📂 Folder Structure

```
Day52/
│
├── app.py
└── README.md
```

---

## 🧠 Key Concepts Learned

- Flask apps can start with a **single file (`app.py`)**
- `__name__` helps Flask locate resources
- `debug=True` enables:
  - Auto-reload on changes
  - Error debugging in browser
- Flask structure is **flexible and customizable**

---

## 💻 Example Code

### app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask App Structure!"

@app.route("/about")
def about():
    return "This is the About Page"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ▶️ Output / Result

Run the app:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

Output:
```
Welcome to Flask App Structure!
```

Visit another route:

```
http://127.0.0.1:5000/about
```

Output:
```
This is the About Page
```

### 🔥 Debug Mode Feature

- When you change code and save:
  - Server reloads automatically
- Errors are displayed in the browser for easy debugging

---

## ✅ Summary

- Understood Flask’s flexible project structure
- Created multiple routes in a single file
- Learned how debug mode works
- Observed auto-reload feature

---

✅ **Day 52 Completed**

Today I learned how Flask applications are structured and how to run them efficiently using debug mode.
