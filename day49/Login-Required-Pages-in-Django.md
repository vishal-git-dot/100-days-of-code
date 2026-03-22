# Day 49 – Login Required Pages in Django

## 📌 Overview

Today I learned how to **restrict access to certain pages in Django so that only logged-in users can view them**.

In real-world applications, some pages should only be accessible after login, such as:
- User dashboards 📊
- Profile pages 👤
- Private data 🔒

Django provides a simple way to protect views using the **`login_required` decorator**.

---

## 🛠 What I Did

- Used Django’s **`login_required` decorator**
- Protected a view so only authenticated users can access it
- Redirected unauthenticated users to the login page
- Configured `LOGIN_URL` in settings
- Tested access control in the browser

---

## 📂 Folder Structure

```
Day49/
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
│   └── dashboard.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **login_required decorator** → Restricts access to authenticated users
- Redirects unauthorized users to the login page
- `LOGIN_URL` → Defines where users are redirected if not logged in
- Helps secure **private or sensitive pages**

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "dashboard.html")
```

---

### settings.py

```python
LOGIN_URL = '/login/'
```

---

### urls.py (app)

```python
from django.urls import path
from .views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]
```

---

### dashboard.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>

<h2>Welcome to Dashboard</h2>

<p>This page is only visible to logged-in users.</p>

</body>
</html>
```

---

## ▶️ Output / Result

- If a **logged-in user** visits `/dashboard/`:
  - Page loads normally ✅

- If a **not logged-in user** tries to access `/dashboard/`:
  - Redirected to `/login/` 🔒

Example flow:

```
User not logged in → tries /dashboard/
→ Redirected to /login/
```

This ensures that only authenticated users can access **protected content**.

---

✅ **Day 49 Completed**

Today I learned how to **protect pages in Django using the login_required decorator**, ensuring only authenticated users can access certain views.
