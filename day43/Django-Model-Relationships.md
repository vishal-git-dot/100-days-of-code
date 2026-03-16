# Day 43 – Django Model Relationships

## 📌 Overview

Today I learned about **Django Model Relationships**, which allow different database models to be connected with each other.

In real-world applications, data is often related. For example:
- A **blog post can have many comments**
- A **user can have multiple posts**
- A **profile belongs to one user**

Django provides relationship fields such as **ForeignKey, OneToOneField, and ManyToManyField** to connect models together.

---

## 🛠 What I Did

- Created two models: **Post** and **Comment**
- Used **ForeignKey** to connect Comment to Post
- Learned how relational databases link tables
- Retrieved related data using Django ORM
- Displayed related comments under a post

---

## 📂 Folder Structure

```
Day43/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── views.py
│
├── templates/
│   └── post_detail.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

### 1️⃣ ForeignKey (One-to-Many)

One model can have **many related objects**.

Example:
- One **Post**
- Many **Comments**

```
Post → Comment
```

### 2️⃣ OneToOneField

Creates a **one-to-one relationship** between models.

Example:
- One **User**
- One **Profile**

### 3️⃣ ManyToManyField

Allows **many objects to relate to many others**.

Example:
- Students ↔ Courses

---

## 💻 Example Code

### models.py

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.author
```

---

### views.py

```python
from django.shortcuts import render
from .models import Post

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()

    return render(request, "post_detail.html", {
        "post": post,
        "comments": comments
    })
```

---

### post_detail.html

```html
<h2>{{ post.title }}</h2>
<p>{{ post.content }}</p>

<h3>Comments</h3>

<ul>
{% for comment in comments %}
    <li>{{ comment.author }}: {{ comment.text }}</li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

Example page display:

```
Django Learning

Today I learned about Django models and relationships.

Comments
John: Great post!
Sarah: Very helpful explanation.
```

Each **comment is linked to a specific post**, demonstrating how Django models can **store related data across tables**.

---

✅ **Day 43 Completed**

Today I learned how to **connect models using Django relationships like ForeignKey**, allowing applications to store and manage **related data efficiently**.
