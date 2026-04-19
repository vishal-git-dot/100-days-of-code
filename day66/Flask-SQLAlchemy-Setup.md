# Day 66 – Flask SQLAlchemy Setup

## 📌 Overview

Today I learned how to **use SQLAlchemy in Flask to manage the database using ORM (Object Relational Mapping)**.

Previously, I used raw SQL queries with SQLite. SQLAlchemy makes database operations cleaner, more scalable, and easier to manage by using Python classes instead of SQL queries.

In this lesson, I added functionality to:
- Configure SQLAlchemy in Flask
- Create database models
- Replace raw SQL with ORM
- Simplify database interactions

---

## 🛠 What I Did

- Installed and configured **Flask-SQLAlchemy**
- Set up database URI
- Created a model class for users
- Used ORM methods instead of raw SQL
- Initialized the database

---

## 📂 Folder Structure

```
Day66/
│
├── app.py
├── database.db
├── templates/
│   ├── form.html
│   └── list.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **SQLAlchemy (ORM)** → Work with database using Python classes
- `db.Model` for defining tables
- `db.Column`, `db.Integer`, `db.String`
- `db.session.add()` and `db.session.commit()`
- Cleaner alternative to raw SQL

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")

        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/")

    users = User.query.all()
    return render_template("form.html", users=users)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

---

### templates/form.html

```html
<h2>Add User</h2>

<form method="POST">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Add</button>
</form>

<ul>
{% for user in users %}
    <li>{{ user.name }}</li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

1. Open the app:
http://127.0.0.1:5000/

2. Enter a name and submit

3. Data is stored using SQLAlchemy

4. Users are displayed using ORM queries

---

## ✅ Summary

- Integrated **SQLAlchemy with Flask**
- Created database models using Python classes
- Replaced raw SQL with ORM methods
- Simplified database operations

---

✅ **Day 66 Completed**

Today I learned how to **use SQLAlchemy ORM in Flask**, making database handling cleaner, scalable, and more efficient.
