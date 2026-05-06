# Day 77 – Flask Search Functionality

## 📌 Overview

Today I learned how to **implement search functionality in a Flask application**.

As applications grow, finding specific records manually becomes difficult. Search functionality helps users quickly filter and locate data from the database.

In this lesson, I added functionality to:
- Search users dynamically
- Filter records using query parameters
- Use SQLAlchemy filtering
- Display matching results

---

## 🛠 What I Did

- Created search form in template
- Retrieved search input using `request.args`
- Filtered records using `filter()`
- Displayed filtered user list
- Improved user experience

---

## 📂 Folder Structure

```text
Day77/
│
├── app.py
├── database.db
├── templates/
│   ├── list.html
│   └── search.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- Search functionality in Flask
- Using `request.args.get()`
- SQLAlchemy filtering
- Dynamic query handling
- Improving data accessibility

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
    search = request.args.get("search", "")

    if search:
        users = User.query.filter(User.email.contains(search)).all()
    else:
        users = User.query.all()

    return render_template("list.html", users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

### templates/list.html

```html
<h2>User List</h2>

<form method="GET">
    <input type="text" name="search" placeholder="Search email">
    <button type="submit">Search</button>
</form>

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

2. Enter search keyword

3. Click Search

4. Matching users displayed instantly

---

## ✅ Summary

- Implemented search feature in Flask
- Filtered database records dynamically
- Improved usability for large datasets
- Enhanced user interaction

---

✅ **Day 77 Completed**

Today I learned how to **implement search functionality in Flask**, allowing users to quickly find records from the database.
