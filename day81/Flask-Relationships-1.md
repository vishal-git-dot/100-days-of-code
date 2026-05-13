# Day 81 – Flask Relationships (One-to-Many)

## 📌 Overview

In this project, I learned how to create One-to-Many relationships in Flask using SQLAlchemy.

A One-to-Many relationship means:

- One user can have many posts
- One category can contain many products
- One author can write many articles

This is one of the most important database concepts in backend development.

In this project:

- One User can create multiple Posts

---

# 🛠 What I Did

- Created User and Post models
- Connected models using relationships
- Used Foreign Keys
- Displayed posts linked to users
- Inserted sample relational data
- Rendered related records dynamically

---

# 📂 Folder Structure

```plaintext
flask-one-to-many/
│
├── app.py
├── database.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# 🧠 Key Concepts Learned

- One-to-Many relationships
- Foreign Keys
- SQLAlchemy relationship()
- SQLAlchemy db.ForeignKey
- Linked database records
- Relational database structure
- Accessing related objects

---

# 💻 Example Code

## app.py

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    posts = db.relationship('Post', backref='author', lazy=True)

# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')
def index():

    users = User.query.all()

    return render_template('index.html', users=users)

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

        if not User.query.first():

            user1 = User(name='John')
            user2 = User(name='Sarah')

            db.session.add_all([user1, user2])
            db.session.commit()

            posts = [
                Post(title='Flask Basics', author=user1),
                Post(title='Learning SQLAlchemy', author=user1),
                Post(title='Frontend Tips', author=user2),
                Post(title='Database Design', author=user2)
            ]

            db.session.add_all(posts)
            db.session.commit()

    app.run(debug=True)
```

---

## templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>One to Many Relationship</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="container">

    <h1>Users and Their Posts</h1>

    {% for user in users %}

        <div class="user-card">

            <h2>{{ user.name }}</h2>

            <ul>

                {% for post in user.posts %}
                    <li>{{ post.title }}</li>
                {% endfor %}

            </ul>

        </div>

    {% endfor %}

</div>

</body>
</html>
```

---

## static/style.css

```css
body {
    margin: 0;
    padding: 0;
    background: #f4f4f4;
    font-family: Arial, sans-serif;
}

.container {
    width: 80%;
    margin: auto;
    padding: 30px;
}

h1 {
    text-align: center;
    margin-bottom: 40px;
}

.user-card {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.user-card h2 {
    color: #333;
}

ul {
    padding-left: 20px;
}

li {
    margin: 10px 0;
}
```

---

# ▶️ Output / Result

Successfully implemented:

- User and Post relationship
- One user having multiple posts
- Dynamic relational data rendering
- Foreign Key connections
- SQLAlchemy relationship system

Example Output:

```plaintext
John
 - Flask Basics
 - Learning SQLAlchemy

Sarah
 - Frontend Tips
 - Database Design
```

---

# ✅ Summary

In Day 81, I learned how One-to-Many relationships work in Flask using SQLAlchemy.

This project introduced relational database structures, which are essential for real-world backend applications like:

- Blogs
- CRM systems
- Social media apps
- E-commerce systems

I also learned:

- Foreign Keys
- SQLAlchemy relationships
- Linked data handling
- Accessing child records from parent models

---
