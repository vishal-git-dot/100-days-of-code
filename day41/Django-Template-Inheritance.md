# Day 41 – Django Template Inheritance

## 📌 Overview

Today I learned about **Django Template Inheritance**, which helps reuse common HTML layouts across multiple pages.

Instead of repeating the same **header, footer, and navigation code** in every template, Django allows us to create a **base template** and extend it in other templates.

This approach keeps the project **organized, maintainable, and scalable**, especially for larger web applications.

---

## 🛠 What I Did

- Created a **base template (`base.html`)**
- Added common layout elements like header and footer
- Used Django template tag `{% block content %}`
- Extended the base template in another HTML file
- Reused the layout across multiple pages
- Tested that child templates inherit the base layout

---

## 📂 Folder Structure

```
Day41/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   └── contact_list.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Template Inheritance** allows templates to reuse a common layout
- `{% extends "base.html" %}` makes a template inherit another template
- `{% block content %}` defines areas where child templates can insert content
- Helps avoid **duplicate HTML code**
- Makes projects easier to maintain

Common template tags used:

- `{% extends %}`
- `{% block %}`
- `{% endblock %}`

---

## 💻 Example Code

### base.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django App</title>
</head>
<body>

<header>
    <h1>My Django Website</h1>
</header>

<hr>

{% block content %}
<!-- Page content will appear here -->
{% endblock %}

<hr>

<footer>
    <p>© 2026 My Django Project</p>
</footer>

</body>
</html>
```

---

### contact_list.html

```html
{% extends "base.html" %}

{% block content %}

<h2>Contact List</h2>

<ul>
{% for contact in contacts %}
    <li>{{ contact.name }} - {{ contact.email }}</li>
{% endfor %}
</ul>

{% endblock %}
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

## ▶️ Output / Result

When visiting the contact list page, the browser shows a layout like:

```
My Django Website
-----------------

Contact List
John - john@email.com
Sarah - sarah@email.com

-----------------
© 2026 My Django Project
```

The **header and footer come from `base.html`**, while the **contact list content comes from `contact_list.html`**.

This allows all pages to **share the same layout while displaying different content**.

---

✅ **Day 41 Completed**

Today I learned how to **use Django Template Inheritance to create reusable layouts**, making the project cleaner and easier to maintain.
