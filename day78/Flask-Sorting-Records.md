
# Day 78 – Flask Sorting Records

## 📌 Overview

Today I learned how to **implement sorting functionality in a Flask application using SQLAlchemy**.

After adding search and pagination features, sorting records is another essential functionality used in real-world applications. Sorting helps users organize and view data in a meaningful order.

In this lesson, I added functionality to:
- Sort records alphabetically
- Sort records in ascending and descending order
- Use SQLAlchemy `order_by()`
- Dynamically sort records using query parameters

---

## 🛠 What I Did

- Created sorting links in template
- Retrieved sorting option using `request.args`
- Used SQLAlchemy `order_by()` method
- Implemented ascending and descending sorting
- Displayed sorted records dynamically

---

## 📂 Folder Structure

```text
Day78/
│
├── app.py
├── database.db
├── templates/
│   └── list.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- Sorting records in Flask
- SQLAlchemy `order_by()`
- Ascending and descending sorting
- Dynamic query parameters
- Organizing database records

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def index():
    sort = request.args.get("sort", "asc")

    if sort == "desc":
        users = User.query.order_by(User.email.desc()).all()
    else:
        users = User.query.order_by(User.email.asc()).all()

    return render_template("list.html", users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

### templates/list.html

```html
<h2>User List</h2>

<a href="/?sort=asc">Sort Ascending</a>
<a href="/?sort=desc">Sort Descending</a>

<ul>
{% for user in users %}
    <li>{{ user.email }}</li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

1. Open:
http://127.0.0.1:5000/

2. Click Sort Ascending

3. Records sorted A → Z

4. Click Sort Descending

5. Records sorted Z → A

---

## ✅ Summary

- Implemented sorting functionality in Flask
- Used SQLAlchemy `order_by()`
- Added ascending and descending sorting
- Improved record organization and usability

---

✅ **Day 78 Completed**

Today I learned how to **sort database records in Flask using SQLAlchemy**, improving user experience and data organization.
