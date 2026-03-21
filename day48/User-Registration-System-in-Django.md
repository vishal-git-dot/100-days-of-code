# Day 48 – User Registration System in Django

## 📌 Overview

Today I learned how to implement a **User Registration System in Django**, allowing new users to **create accounts**.

After learning login and logout, registration is the next step to make a complete **authentication system**. Django provides a built-in form called **UserCreationForm** that simplifies user registration.

This feature is essential for applications where users need personal accounts.

---

## 🛠 What I Did

- Used Django’s built-in **UserCreationForm**
- Created a **registration view**
- Saved new users to the database
- Displayed registration form in template
- Redirected users after successful registration
- Tested user creation and login

---

## 📂 Folder Structure

```
Day48/
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
│   ├── register.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **UserCreationForm** → Built-in Django form for user registration
- Automatically handles:
  - Username
  - Password validation
- `form.save()` → Creates a new user
- Registration + Login = complete authentication system

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
```

---

### urls.py (app)

```python
from django.urls import path
from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
]
```

---

### register.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>

<h2>Register</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">Register</button>
</form>

</body>
</html>
```

---

## ▶️ Output / Result

- A registration form appears with:
  - Username
  - Password
  - Password confirmation
- User fills in details and submits the form
- If valid:
  - New user is created in the database
  - Redirected to login page

Example:

```
Username: john123
Password: ********
```

After registration:
- User can log in using the created credentials
- Data is stored in Django’s built-in **User model**

---

✅ **Day 48 Completed**

Today I learned how to **create a user registration system using Django’s UserCreationForm**, completing the full authentication flow (Register → Login → Logout).
