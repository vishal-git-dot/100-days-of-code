# Day 67 – Flask SQLAlchemy CRUD Operations

## 📌 Overview

Today I learned how to **perform full CRUD operations using SQLAlchemy in Flask**.

After setting up SQLAlchemy, the next step was to implement **Create, Read, Update, and Delete** using ORM instead of raw SQL queries.

In this lesson, I added functionality to:
- Insert data using SQLAlchemy
- Fetch and display records
- Update existing records
- Delete records from the database

---

## 🛠 What I Did

- Used `db.session.add()` for creating records
- Retrieved data using `Model.query.all()`
- Updated records using ORM objects
- Deleted records using `db.session.delete()`
- Replaced all raw SQL with SQLAlchemy

---

## 📂 Folder Structure

```
Day67/
│
├── app.py
├── database.db
├── templates/
│   ├── form.html
│   ├── edit.html
│   └── list.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **ORM CRUD Operations**
- `Model.query.all()` → Read
- `db.session.add()` → Create
- `db.session.commit()` → Save changes
- `db.session.delete()` → Delete
- Query filtering using `get()` and `filter_by()`

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route("/")
def index():
    users = User.query.all()
    return render_template("list.html", users=users)

@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/")
    return render_template("form.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    user = User.query.get(id)
    if request.method == "POST":
        user.name = request.form.get("name")
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", user=user)

@app.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

### templates/list.html

```html
<h2>Users</h2>

<a href="/add">Add User</a>

<ul>
{% for user in users %}
    <li>
        {{ user.name }}
        <a href="/edit/{{ user.id }}">Edit</a>
        <a href="/delete/{{ user.id }}">Delete</a>
    </li>
{% endfor %}
</ul>
```

---

### templates/edit.html

```html
<h2>Edit User</h2>

<form method="POST">
    <input type="text" name="name" value="{{ user.name }}">
    <button type="submit">Update</button>
</form>

<a href="/">Back</a>
```

---

## ▶️ Output / Result

1. Open app:
http://127.0.0.1:5000/

2. Add a user

3. Edit existing user

4. Delete a user

5. All operations work using SQLAlchemy ORM

---

## ✅ Summary

- Implemented **full CRUD using SQLAlchemy**
- Replaced raw SQL completely
- Used ORM methods for cleaner code
- Built a fully functional database-driven app

---

✅ **Day 67 Completed**

Today I learned how to **perform full CRUD operations using SQLAlchemy in Flask**, making my application more scalable and professional.
