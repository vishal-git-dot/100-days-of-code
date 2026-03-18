# Day 45 – Search Functionality in Django

## 📌 Overview

Today I learned how to implement **search functionality in Django**, allowing users to **search and filter data from the database**.

Search is a common feature in web applications such as:
- Blogs 📝
- E-commerce sites 🛒
- Contact lists 📇

Using Django ORM, we can filter data based on user input and display matching results dynamically.

---

## 🛠 What I Did

- Created a **search input form**
- Captured user query using GET request
- Used Django ORM `filter()` method
- Applied `icontains` for case-insensitive search
- Displayed filtered results in template
- Tested search functionality in browser

---

## 📂 Folder Structure

```
Day45/
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

- **GET Request** → Used to send search data via URL
- `request.GET.get()` → Retrieves search input
- `filter()` → Filters database records
- `icontains` → Case-insensitive matching
- Dynamic filtering improves **user experience**

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render
from .models import Contact

def contact_list(request):
    query = request.GET.get('q')
    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(name__icontains=query)

    return render(request, "contact_list.html", {
        "contacts": contacts,
        "query": query
    })
```

---

### contact_list.html

```html
<h2>Search Contacts</h2>

<form method="GET">
    <input type="text" name="q" placeholder="Search by name" value="{{ query }}">
    <button type="submit">Search</button>
</form>

<ul>
{% for contact in contacts %}
    <li>{{ contact.name }} - {{ contact.email }}</li>
{% empty %}
    <li>No results found</li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

- A search bar appears on the page
- User enters a name (e.g., "John")
- Only matching results are displayed

Example:

Search input:
```
John
```

Results:
```
John - john@email.com
```

If no match:
```
No results found
```

URL example:
```
/contacts/?q=John
```

---

✅ **Day 45 Completed**

Today I learned how to **implement search functionality in Django using GET requests and ORM filtering**, making the application more interactive and user-friendly.
