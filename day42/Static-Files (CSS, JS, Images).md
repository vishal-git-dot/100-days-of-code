# Day 42 – Static Files (CSS, JS, Images)

## 📌 Overview

Today I learned how to **use static files in Django**, such as **CSS, JavaScript, and images**.  

Static files are used to **style and enhance web pages**. Django provides a built-in system to manage these files through a **static directory**.

Using static files allows developers to add **custom styling, scripts, and images** to make the website look professional and interactive.

---

## 🛠 What I Did

- Created a **static folder** inside the Django app
- Added a **CSS file for styling**
- Loaded static files in HTML templates
- Configured static file settings
- Applied CSS styles to a template
- Verified styling changes in the browser

---

## 📂 Folder Structure

```
Day42/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── views.py
│   ├── urls.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   └── contact_list.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Static Files** → Files that do not change dynamically (CSS, JS, images)
- `{% load static %}` → Enables static file usage in templates
- `{% static 'path/to/file' %}` → Generates the correct static file URL
- Static files help improve **design, layout, and user experience**

Common static file types:

- **CSS** → Page styling
- **JavaScript** → Interactivity
- **Images** → Visual content

---

## 💻 Example Code

### settings.py (Important Static Settings)

```python
STATIC_URL = '/static/'
```

---

### base.html

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>Django App</title>

    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<header>
    <h1>My Django Website</h1>
</header>

<hr>

{% block content %}
{% endblock %}

<hr>

<footer>
    <p>© 2026 My Django Project</p>
</footer>

</body>
</html>
```

---

### style.css

```css
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: blue;
}

footer {
    text-align: center;
    margin-top: 20px;
}
```

---

## ▶️ Output / Result

After loading the static CSS file:

- The **website layout becomes styled**
- Header text appears **blue**
- Font style changes
- Footer becomes aligned properly

Example display:

```
My Django Website (Blue Header)

Contact List
John - john@email.com
Sarah - sarah@email.com

© 2026 My Django Project
```

Static files help transform a basic HTML page into a **visually styled web application**.

---

✅ **Day 42 Completed**

Today I learned how to **use static files in Django to add CSS styling and improve the visual appearance of the website**.
