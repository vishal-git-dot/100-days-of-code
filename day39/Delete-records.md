# Day 39 – Deleting Records in Django

## 📌 Overview

Today I learned how to **delete records from the database in Django**.  

After implementing **Create, Read, and Update operations**, the final part of CRUD is **Delete**. This allows users to remove unwanted or outdated records from the application.

Using Django views and URL parameters, we can **identify a specific record and remove it from the database safely**.

---

## 🛠 What I Did

- Created a **view to delete a record**
- Used `get_object_or_404()` to safely retrieve the object
- Called `.delete()` to remove the record from the database
- Added a **delete URL with record ID**
- Redirected users back to the contact list after deletion
- Tested the delete functionality

---

## 📂 Folder Structure

```
Day39/
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

- **Delete operation in CRUD**
- `get_object_or_404()` → Safely retrieves a database object
- `.delete()` → Removes the object from the database
- URL parameters help identify which record should be deleted
- `redirect()` sends the user to another page after deletion

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import get_object_or_404, redirect
from .models import Contact

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_list')
```

---

### urls.py (app)

```python
from django.urls import path
from .views import delete_contact

urlpatterns = [
    path('contacts/delete/<int:contact_id>/', delete_contact, name='delete_contact'),
]
```

---

### contact_list.html (Delete Button Example)

```html
<ul>
{% for contact in contacts %}
    <li>
        {{ contact.name }} - {{ contact.email }}

        <a href="/contacts/delete/{{ contact.id }}/">
            Delete
        </a>
    </li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

- The contact list page shows a **Delete link for each record**
- Clicking **Delete** removes that record from the database
- The page refreshes and the deleted entry is no longer displayed

Example:

Before deletion:

```
John - john@email.com
Sarah - sarah@email.com
```

After deleting Sarah:

```
John - john@email.com
```

---

✅ **Day 39 Completed**

Today I learned how to **delete database records using Django views and URL parameters**, completing the full **CRUD (Create, Read, Update, Delete) functionality** in my Django application.
