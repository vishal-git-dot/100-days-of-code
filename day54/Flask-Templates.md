# Day 54 – Flask Templates (Jinja2 Basics)

## 📌 Overview

Today I learned how to use **Flask Templates** with **Jinja2**, which allows us to separate Python code from HTML.

Templates make web pages dynamic by letting us:
- Display variables
- Loop through lists
- Render HTML content dynamically

This is the first step toward **dynamic web pages** in Flask.

---

## 🛠 What I Did

- Created a `templates/` folder
- Added an HTML file `home.html`
- Used `render_template()` to render HTML
- Passed variables from Flask view to template
- Used **Jinja2 syntax** to display dynamic data

---

## 📂 Folder Structure

```
Day54/
│
├── app.py
├── templates/
│   └── home.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Templates** → HTML files that Flask can render dynamically
- `render_template()` → Renders a template file
- **Jinja2 Syntax**:
  - `{{ variable }}` → Display variables
  - `{% for item in list %} ... {% endfor %}` → Loop
  - `{% if condition %} ... {% endif %}` → Conditional rendering
- Separates Python logic from HTML

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "John"
    skills = ["Python", "Flask", "HTML"]
    return render_template("home.html", name=name, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/home.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>

<h1>Welcome, {{ name }}!</h1>

<h3>Your Skills:</h3>
<ul>
{% for skill in skills %}
    <li>{{ skill }}</li>
{% endfor %}
</ul>

</body>
</html>
```

---

## ▶️ Output / Result

Open in browser:

```
http://127.0.0.1:5000/
```

Output:

```
Welcome, John!

Your Skills:
- Python
- Flask
- HTML
```

Dynamic content is displayed using variables and loops from Flask.

---

## ✅ Summary

- Learned to use **templates with Flask**
- Rendered HTML dynamically using `render_template()`
- Passed variables and lists from Python to HTML
- Used Jinja2 syntax for loops and variables

---

✅ **Day 54 Completed**

Today I learned how to **use Flask templates and Jinja2 to render dynamic HTML content**, separating backend logic from frontend.
