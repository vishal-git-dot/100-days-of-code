# Day 76 – Flask Pagination (List Records Efficiently)

## 📌 Overview

Today I learned how to **implement pagination in a Flask application**.

As the number of records grows, displaying everything on a single page becomes inefficient. Pagination helps divide data into smaller chunks, improving performance and user experience.

In this lesson, I added functionality to:
- Limit number of records per page
- Navigate between pages
- Improve UI for large datasets
- Handle page numbers dynamically

---

## 🛠 What I Did

- Used SQLAlchemy `paginate()` method
- Limited records per page
- Created dynamic page navigation
- Passed pagination object to template
- Displayed next/previous controls

---

## 📂 Folder Structure

```
Day76/
│
├── app.py
├── database.db
├── templates/
│   ├── list.html
│   └── login.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- Pagination in Flask
- `query.paginate(page, per_page)`
- Handling large datasets
- Page navigation logic
- Improving performance

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
    page = request.args.get("page", 1, type=int)
    users = User.query.paginate(page=page, per_page=5)

    return render_template("list.html", users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

### templates/list.html

```html
<h2>User List</h2>

<ul>
{% for user in users.items %}
    <li>{{ user.email }}</li>
{% endfor %}
</ul>

<div>
    {% if users.has_prev %}
        <a href="?page={{ users.prev_num }}">Previous</a>
    {% endif %}

    {% if users.has_next %}
        <a href="?page={{ users.next_num }}">Next</a>
    {% endif %}
</div>
```

---

## ▶️ Output / Result

1. Open:
http://127.0.0.1:5000/

2. Only limited users shown per page

3. Click Next / Previous

4. Data loads page-wise

---

## ✅ Summary

- Implemented pagination feature
- Improved performance for large data
- Added navigation controls
- Enhanced user experience

---

✅ **Day 76 Completed**

Today I learned how to **implement pagination in Flask**, making applications scalable and efficient.
