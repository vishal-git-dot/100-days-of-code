# Day 33 – Django Simple Form Integration 🚀

---

## 📌 Overview

Today I learned how to create and process a simple form in Django.  
This helps collect user input from the browser and process it in the backend.

---

## 🛠 What I Did

- Created a simple HTML form
- Connected form with Django view
- Used `POST` method to send data
- Retrieved form data using `request.POST`
- Displayed submitted data as response
- Tested form submission in browser

---

## 📂 Folder Structure

```
myapp/
│
├── templates/
│   └── form.html
├── views.py
└── urls.py
```

---

## 🧠 Key Concepts Learned

- HTML forms collect user input
- `POST` method sends form data securely
- `request.POST.get()` retrieves form data
- Django views process form data
- Forms connect frontend input with backend logic

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

def user_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        return HttpResponse(f"Hello {name}, you are {age} years old.")

    return render(request, "form.html")
```

---

### form.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Form</title>
</head>
<body>

<h2>Simple Django Form</h2>

<form method="POST">
    {% csrf_token %}

    <label>Name:</label>
    <input type="text" name="name">

    <br><br>

    <label>Age:</label>
    <input type="number" name="age">

    <br><br>

    <button type="submit">Submit</button>

</form>

</body>
</html>
```

---

## 🔗 urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form, name='user_form'),
]
```

---

## ▶️ Output

When the form is submitted, Django processes the input and displays:

```
Hello John, you are 25 years old.
```

---

🔥 Day 33 Complete – Learned how to handle forms in Django!
