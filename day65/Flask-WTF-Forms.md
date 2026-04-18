# Day 65 – Flask-WTF Forms

## 📌 Overview

Today I learned how to **use Flask-WTF to handle forms in a cleaner and more structured way**.

Previously, I handled forms manually using `request.form`. Flask-WTF simplifies this by providing built-in form classes, validation, and CSRF protection.

In this lesson, I added functionality to:
- Create forms using Flask-WTF
- Add built-in validation
- Replace manual form handling
- Improve form security with CSRF protection

---

## 🛠 What I Did

- Installed and configured **Flask-WTF**
- Created a form class using `FlaskForm`
- Used built-in validators like `DataRequired()`
- Replaced manual form handling with Flask-WTF
- Rendered forms using Jinja2

---

## 📂 Folder Structure

```
Day65/
│
├── app.py
├── forms.py
├── database.db
├── templates/
│   ├── form.html
│   └── list.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Flask-WTF** → Simplifies form handling
- `FlaskForm` class
- Validators like `DataRequired()`
- CSRF protection
- Cleaner and structured code

---

## 💻 Example Code

### forms.py

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Add User")
```

---

### app.py

```python
import sqlite3
from flask import Flask, render_template, redirect
from forms import UserForm

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()

    if form.validate_on_submit():
        name = form.name.data

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        return redirect("/")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("form.html", form=form, users=users)


if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/form.html

```html
<h2>Add User</h2>

<form method="POST">
    {{ form.hidden_tag() }}

    {{ form.name.label }}
    {{ form.name() }}

    {{ form.submit() }}
</form>

<ul>
{% for user in users %}
    <li>{{ user[1] }}</li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

1. Open the app:
http://127.0.0.1:5000/

2. Enter name and submit

3. Form validates automatically

4. Data is stored in database

---

## ✅ Summary

- Implemented **Flask-WTF for form handling**
- Used built-in validation instead of manual checks
- Added CSRF protection for security
- Made form handling cleaner and more scalable

---

✅ **Day 65 Completed**

Today I learned how to **use Flask-WTF to handle forms with validation and security**, improving the structure and quality of my Flask application.
