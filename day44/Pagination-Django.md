# Day 44 – Pagination in Django

## 📌 Overview

Today I learned how to implement **Pagination in Django**, which helps display large amounts of data in **smaller, manageable pages**.

Instead of showing all records at once, pagination divides data into multiple pages, improving:
- Performance ⚡
- User experience 😊
- Page loading speed 🚀

This is commonly used in **blogs, product listings, and search results**.

---

## 🛠 What I Did

- Imported Django’s **Paginator class**
- Divided database records into multiple pages
- Retrieved the current page number from the URL
- Passed paginated data to the template
- Added navigation links (Next / Previous)
- Tested pagination in the browser

---

## 📂 Folder Structure

```
Day44/
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

- **Paginator** → Splits data into pages
- `get_page()` → Safely retrieves a page number
- `has_next()` / `has_previous()` → Navigation checks
- Pagination improves **performance and usability**

---

## 💻 Example Code

### views.py

```python
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()

    paginator = Paginator(contacts, 2)  # Show 2 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "contact_list.html", {"page_obj": page_obj})
```

---

### contact_list.html

```html
<h2>Contact List</h2>

<ul>
{% for contact in page_obj %}
    <li>{{ contact.name }} - {{ contact.email }}</li>
{% endfor %}
</ul>

<div>
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}

    <span>Page {{ page_obj.number }}</span>

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}
</div>
```

---

## ▶️ Output / Result

- Only a limited number of records (e.g., 2 per page) are displayed
- Navigation links appear:

```
Previous | Page 1 | Next
```

- Clicking **Next** loads the next set of records
- URL changes dynamically:

```
/contacts/?page=2
```

This makes the application more **organized and user-friendly** when handling large datasets.

---

✅ **Day 44 Completed**

Today I learned how to **implement pagination in Django using the Paginator class**, allowing efficient display of large datasets across multiple pages.
