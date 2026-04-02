# Day 55 – Template Inheritance in Flask

## 📌 Overview

Today I learned about **Template Inheritance in Flask using Jinja2**, which helps in creating a consistent layout across multiple pages.

Instead of repeating the same HTML structure (like header, navbar, footer), we can create a **base template** and reuse it in other pages.

This makes code:
- Cleaner 🧹
- Reusable ♻️
- Easier to maintain 🔧

---

## 🛠 What I Did

- Created a `base.html` template
- Used `{% block %}` to define dynamic sections
- Used `{% extends %}` in child templates
- Built multiple pages using a shared layout
- Reduced code duplication

---

## 📂 Folder Structure

```
Day55/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── home.html
│   └── about.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Template Inheritance** → Reusing common layout
- `{% extends "base.html" %}` → Inherit base template
- `{% block content %}` → Define replaceable sections
- Avoids repeating HTML structure
- Makes large projects manageable

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/base.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>

<h1>My Website</h1>

<nav>
    <a href="/">Home</a> |
    <a href="/about">About</a>
</nav>

<hr>

{% block content %}
{% endblock %}

</body>
</html>
```

---

### templates/home.html

```html
{% extends "base.html" %}

{% block content %}
<h2>Home Page</h2>
<p>Welcome to the home page.</p>
{% endblock %}
```

---

### templates/about.html

```html
{% extends "base.html" %}

{% block content %}
<h2>About Page</h2>
<p>This is the about page.</p>
{% endblock %}
```

---

## ▶️ Output / Result

Run the app:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

Output:
- Displays **Home Page** with shared layout

Visit:

```
http://127.0.0.1:5000/about
```

Output:
- Displays **About Page** using same layout

---

## ✅ Summary

- Learned how to reuse layouts using template inheritance
- Created a base template (`base.html`)
- Used blocks to insert dynamic content
- Reduced code duplication across pages

---

✅ **Day 55 Completed**

Today I learned how to **use template inheritance in Flask**, making my HTML structure reusable and clean.
