# Day 47 – User Authentication in Django

## 📌 Overview

Today I learned how to implement **User Authentication in Django**, which allows users to **log in and log out of the application**.

Authentication is a core feature in most web applications, enabling:
- Secure access 🔐
- User-specific data 👤
- Protected pages 🚫

Django provides a built-in authentication system that handles **user login, logout, and session management**.

---

## 🛠 What I Did

- Used Django’s built-in **authentication system**
- Created a **login view**
- Used `authenticate()` to verify user credentials
- Logged users in using `login()`
- Logged users out using `logout()`
- Created login and logout URLs
- Built a simple login form template

---

## 📂 Folder Structure

```
Day47/
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
│   ├── login.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Authentication** → Verifying user identity
- `authenticate()` → Checks username and password
- `login()` → Logs the user into the session
- `logout()` → Logs the user out
- Django manages sessions automatically

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('contact_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
```

---

### urls.py (app)

```python
from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
```

---

### login.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>

<h2>Login</h2>

<form method="POST">
    {% csrf_token %}

    <input type="text" name="username" placeholder="Username"><br><br>
    <input type="password" name="password" placeholder="Password"><br><br>

    <button type="submit">Login</button>
</form>

{% if error %}
<p>{{ error }}</p>
{% endif %}

</body>
</html>
```

---

## ▶️ Output / Result

- A login page is displayed
- User enters:
  - Username
  - Password
- If credentials are correct:
  - User is logged in
  - Redirected to another page (e.g., contact list)
- If incorrect:
  - Error message: **Invalid credentials**

After login:
- Django maintains a **session**
- User stays logged in until logout

---

✅ **Day 47 Completed**

Today I learned how to **implement user authentication in Django using login, logout, and authenticate functions**, enabling secure access to the application.
