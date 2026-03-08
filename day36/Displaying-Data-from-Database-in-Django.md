# Day 36 – Displaying Data from Database in Django

## 📌 Overview

After learning how to **save form data into the database**, today I learned how to **retrieve and display stored data in a web page using Django templates**.

Django allows us to fetch records from the database using **Model queries** and send them to HTML templates through **views**. The template can then display the data using **template loops**.

This is an important concept because most web applications need to **show stored data to users**, such as blog posts, user profiles, comments, or product lists.

---

## 🛠 What I Did

- Retrieved saved data from the database using Django ORM
- Used `Model.objects.all()` to get all records
- Passed database records from **view → template**
- Displayed the records in an HTML page
- Used Django template **for loop** to show multiple records
- Verified that submitted form data appears on the webpage

---

## 📂 Folder Structure

```
Day36/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   └── contact_list.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Django ORM** → Used to interact with the database
- `Model.objects.all()` → Retrieves all records from the table
- **Context dictionary** → Sends data from views to templates
- **Django Template Loop (`{% for %}`)** → Used to display multiple records
- Templates dynamically render database data in HTML

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

### views.py

```python
from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    
    return render(request, "contact_list.html", {"contacts": contacts})
```

---

### urls.py (app)

```python
from django.urls import path
from .views import contact_list

urlpatterns = [
    path("contacts/", contact_list, name="contact_list"),
]
```

---

### contact_list.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact List</title>
</head>
<body>

<h2>Saved Contacts</h2>

<ul>
    {% for contact in contacts %}
        <li>
            <strong>{{ contact.name }}</strong> -
            {{ contact.email }} -
            {{ contact.message }}
        </li>
    {% endfor %}
</ul>

</body>
</html>
```

---

## ▶️ Output / Result

- When visiting `/contacts/`, the browser displays all saved contact records.
- Each record shows:
  - Name
  - Email
  - Message

Example display in browser:

```
Saved Contacts

John - john@email.com - Hello Django
Sarah - sarah@email.com - Testing contact form
```

Now the application can **store user data and display it dynamically from the database**.

---

✅ **Day 36 Completed**

Today I learned how to **retrieve and display database records in Django using the ORM and templates**, completing the basic **Save → Retrieve → Display workflow** in a Django application.
