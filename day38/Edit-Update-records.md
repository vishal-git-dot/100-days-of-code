# Day 38 – Editing / Updating Records in Django

## 📌 Overview

Today I learned how to **edit and update existing database records using Django views and forms**.  

Previously, I could **save and display data**, and also manage it via the admin panel. Now, I learned how to **let users update their data through the website itself** using forms tied to existing database entries.

This is an important concept because most web applications need a way to **edit user profiles, posts, or any dynamic content**.

---

## 🛠 What I Did

- Created a **view to edit existing records**
- Passed the **instance** of the model to a form
- Pre-filled the form with existing data
- Allowed users to submit updates via POST
- Saved changes back to the database
- Verified that updated data appears in the template

---

## 📂 Folder Structure

```
Day38/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   └── contact_edit.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Instance in ModelForm** → Pre-fills a form with existing database data
- `form.is_valid()` → Validates updated input
- `form.save()` → Saves updates to the database
- URL patterns with **dynamic parameters** (e.g., record ID)
- User-friendly **edit pages** for web applications

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact_edit.html', {'form': form})
```

---

### urls.py (app)

```python
from django.urls import path
from .views import edit_contact

urlpatterns = [
    path('contacts/edit/<int:contact_id>/', edit_contact, name='edit_contact'),
]
```

---

### contact_edit.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Contact</title>
</head>
<body>

<h2>Edit Contact</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>

</body>
</html>
```

---

## ▶️ Output / Result

- Visiting `/contacts/edit/1/` shows a form **pre-filled with data** for the contact with ID 1
- Updating fields and submitting saves changes to the database
- After submission, the user is redirected to the contact list page
- The updated information is displayed in the list

Example:

Before edit:

```
John - john@email.com - Hello Django
```

After editing message:

```
John - john@email.com - Updated message
```

---

✅ **Day 38 Completed**

Today I learned how to **allow users to edit and update existing records using Django forms and views**, completing the **basic CRUD workflow: Create, Read, Update, Delete**.
