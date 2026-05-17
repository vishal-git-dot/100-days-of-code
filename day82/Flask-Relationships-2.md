# Day 82 – Flask Relationships (Many-to-Many)

## 📌 Overview

In this project, I learned how to create Many-to-Many relationships in Flask using SQLAlchemy.

A Many-to-Many relationship means:

- One post can have many tags
- One tag can belong to many posts
- One student can enroll in many courses
- One course can have many students

This type of relationship is widely used in real-world backend applications.

In this project:

- Posts can have multiple Tags
- Tags can belong to multiple Posts

---

## 🛠 What I Did

- Created Post and Tag models
- Built an association table
- Connected models using Many-to-Many relationships
- Inserted relational sample data
- Displayed related records dynamically
- Learned advanced ORM concepts

---

## 📂 Folder Structure

```plaintext
flask-many-to-many/
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

## 🧠 Key Concepts Learned

- Many-to-Many relationships
- Association tables
- SQLAlchemy relationship()
- Secondary tables
- ORM relational mapping
- Linked database records
- Advanced SQLAlchemy relationships

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Association Table
post_tags = db.Table(
    'post_tags',

    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

    tags = db.relationship(
        'Tag',
        secondary=post_tags,
        backref='posts'
    )

# Tag Model
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/')
def index():

    posts = Post.query.all()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

        if not Post.query.first():

            flask_tag = Tag(name='Flask')
            python_tag = Tag(name='Python')
            database_tag = Tag(name='Database')

            post1 = Post(
                title='Learning Flask Relationships',
                tags=[flask_tag, python_tag]
            )

            post2 = Post(
                title='SQLAlchemy Database Guide',
                tags=[python_tag, database_tag]
            )

            db.session.add_all([
                flask_tag,
                python_tag,
                database_tag,
                post1,
                post2
            ])

            db.session.commit()

    app.run(debug=True)
```

---

### templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Many To Many Relationship</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="container">

    <h1>Posts and Tags</h1>

    {% for post in posts %}

        <div class="post-card">

            <h2>{{ post.title }}</h2>

            <div class="tags">

                {% for tag in post.tags %}
                    <span>{{ tag.name }}</span>
                {% endfor %}

            </div>

        </div>

    {% endfor %}

</div>

</body>
</html>
```

---

### static/style.css

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

.post-card {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.tags {
    margin-top: 15px;
}

.tags span {
    display: inline-block;
    background: #333;
    color: white;
    padding: 6px 12px;
    border-radius: 5px;
    margin-right: 10px;
}
```

---

## ▶️ Output / Result

Successfully implemented:

- Many-to-Many relationships
- Association table linking
- Posts connected to multiple tags
- Tags connected to multiple posts
- Dynamic relational rendering

Example Output:

```plaintext
Learning Flask Relationships
 - Flask
 - Python

SQLAlchemy Database Guide
 - Python
 - Database
```

---

## ✅ Summary

In Day 82, I learned how Many-to-Many relationships work in Flask using SQLAlchemy.

This project introduced association tables and advanced ORM relationship handling used in real-world applications like:

- Blogging systems
- E-learning platforms
- Inventory systems
- Tagging systems
- CMS applications

I also learned:

- Association tables
- Secondary relationships
- ORM relational mapping
- Advanced database structures

---

