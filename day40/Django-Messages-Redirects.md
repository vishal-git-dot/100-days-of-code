# Day 40 – Django Messages & Redirects

## 📌 Overview

Today I learned how to **display feedback messages to users and redirect them to another page after an action** in Django.

When users submit a form, update data, or delete records, it is good practice to **show confirmation messages** such as "Data saved successfully" or "Record deleted".

Django provides a built-in **Messages Framework** that allows developers to easily display notifications like **success, error, warning, or info messages**.

---

## 🛠 What I Did

- Enabled Django **Messages Framework**
- Added success messages after form submission
- Used `redirect()` to send users to another page
- Displayed messages inside HTML templates
- Tested message display after saving data

---

## 📂 Folder Structure

```
Day40/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── views.py
│   ├── models.py
│
├── templates/
│   └── contact_list.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Django Messages Framework** → Displays notifications to users
- `messages.success()` → Shows success messages
- `redirect()` → Redirects users to another page
- Messages can be **displayed dynamically in templates**
- Improves **user experience and application feedback**

Common message types:

- `messages.success`
- `messages.error`
- `messages.warning`
- `messages.info`

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact

def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()

    messages.success(request, "Contact deleted successfully!")

    return redirect('contact_list')
```

---

### Template (contact_list.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact List</title>
</head>
<body>

<h2>Contacts</h2>

{% if messages %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endif %}

<ul>
{% for contact in contacts %}
    <li>
        {{ contact.name }} - {{ contact.email }}
    </li>
{% endfor %}
</ul>

</body>
</html>
```

---

## ▶️ Output / Result

When a user performs an action such as **deleting a contact**, they are redirected to the contact list page and see a message like:

```
Contact deleted successfully!
```

Example workflow:

1. User clicks **Delete**
2. Record is removed from the database
3. User is redirected to `/contacts/`
4. A **success message appears on the page**

This improves user experience by clearly informing users about the result of their actions.

---

✅ **Day 40 Completed**

Today I learned how to **use Django Messages Framework and redirects to provide feedback to users after performing actions like saving or deleting data**.
