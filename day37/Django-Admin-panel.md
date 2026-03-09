# Day 37 – Using the Django Admin Panel

## 📌 Overview

Today I learned how to use the **Django Admin Panel**, a built-in feature that allows developers to **manage database records through a web interface**.

Instead of manually interacting with the database, Django provides an **automatic admin dashboard** where we can **add, edit, view, and delete data** from models.

This feature is extremely useful during development because it allows quick management of application data.

---

## 🛠 What I Did

- Created a **superuser account**
- Logged into the **Django Admin Panel**
- Registered my **Contact model** in `admin.py`
- Viewed stored data in the admin dashboard
- Added new records through the admin interface
- Edited and deleted records using the admin panel

---

## 📂 Folder Structure

```
Day37/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── admin.py
│
├── templates/
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Django Admin** → Built-in interface to manage application data
- **Superuser** → An administrator account with full access
- **admin.py** → File used to register models for admin management
- **Model Registration** → Makes models visible in the admin dashboard
- Admin interface automatically provides **Create, Read, Update, Delete (CRUD)** operations

---

## 💻 Example Code

### models.py

```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
```

---

### admin.py

```python
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
```

---

### Create Superuser

Run the following command in the terminal:

```bash
python manage.py createsuperuser
```

Example prompts:

```
Username: admin
Email: admin@email.com
Password: ********
```

---

### Start Server

```bash
python manage.py runserver
```

---

## ▶️ Output / Result

Open the browser and go to:

```
http://127.0.0.1:8000/admin
```

Login using the **superuser credentials**.

Inside the admin dashboard you will see:

```
Contacts
```

From there you can:

- ➕ Add new contacts
- ✏️ Edit existing records
- ❌ Delete records
- 📋 View all stored entries

The Django admin panel provides a **powerful and ready-to-use interface for managing database data without writing extra code**.

---

✅ **Day 37 Completed**

Today I learned how to **enable and use the Django Admin Panel to manage database records easily through a web interface**.
