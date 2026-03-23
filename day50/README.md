# Day 50 – Mini Project: Contact Manager

## 📌 Overview

Today I built a **mini project – Contact Manager** combining everything I learned so far in Django.

Features included:  
- Add new contacts 📝  
- View all contacts 📋  
- Edit contacts ✏️  
- Delete contacts ❌  
- Search contacts 🔍  
- Login required for managing contacts 🔐  

This project demonstrates a **full CRUD application with authentication, search, and user-friendly features**.

---

## 🛠 What I Did

- Created models for contacts
- Implemented **CRUD operations** (Create, Read, Update, Delete)
- Added **search functionality**
- Applied **login required** to protect pages
- Used **template inheritance** and static files for layout and styling
- Tested all features in the browser

---

## 📂 Folder Structure

```
Day50/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
├── templates/
│   ├── base.html
│   ├── contact_list.html
│   ├── contact_edit.html
│   ├── login.html
│
├── static/
│   └── css/style.css
│
└── manage.py
```

---

## ▶️ Result / Output

- Logged-in users can manage contacts  
- Add, edit, delete, and search contacts  
- Pages use a **consistent layout** with base template  
- Static files applied for **better styling**  
- Full **user authentication flow** is functional  

This project serves as a **portfolio-ready mini application** demonstrating key Django concepts.

---

✅ **Day 50 Completed**

I completed my first **mini Django project**, integrating CRUD, authentication, search, template inheritance, and static files.
