# Day 34 – Django Simple Model Integration 🚀

---

## 📌 Overview

Today I learned how to create and integrate a simple model in Django.  
Models allow Django applications to interact with databases and store structured data.

---

## 🛠 What I Did

- Created a Django model
- Defined fields for storing user data
- Ran migrations to create database tables
- Registered model in Django admin
- Viewed stored data using Django admin panel

---

## 📂 Folder Structure

```
myapp/
│
├── models.py
├── admin.py
├── views.py
├── urls.py
└── migrations/
```

---

## 🧠 Key Concepts Learned

- Models define the structure of database tables
- Django uses ORM (Object Relational Mapping)
- `makemigrations` creates migration files
- `migrate` applies migrations to the database
- Models can be managed through Django Admin

---

## 💻 Example Code

### models.py

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

---

### admin.py

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

---

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Create Admin User

```bash
python manage.py createsuperuser
```

---

## ▶️ Output

After running the server and opening:

```
http://127.0.0.1:8000/admin/
```

You can log in and add new **Student** records using the admin interface.

---

🔥 Day 34 Complete – Learned how Django models interact with the database!
