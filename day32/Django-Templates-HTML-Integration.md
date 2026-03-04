# Day 32 – Django Templates & HTML Integration 🚀

---

## 📌 Overview

Today I learned how to connect Django backend with HTML frontend using the Django Template system.

---

## 🛠 What I Did

- Created `templates` folder inside Django app  
- Created `home.html` file  
- Replaced `HttpResponse` with `render()`  
- Connected view to template  
- Passed dynamic data using context dictionary  
- Displayed variables using `{{ }}` syntax  
- Tested output in browser  

---

## 📂 Folder Structure

```
myapp/
│
├── templates/
│   └── home.html
├── views.py
└── urls.py
```

---

## 🧠 Key Concepts Learned

- Django uses Template Engine to render HTML  
- `render(request, template_name, context)` returns HTML response  
- Context dictionary sends backend data to frontend  
- `{{ variable }}` displays dynamic data  
- Templates separate business logic from UI  

---

## 💻 Example Code

### views.py

```python
from django.shortcuts import render

def home(request):
    data = {
        "name": "Drc",
        "course": "Django Templates"
    }
    return render(request, 'home.html', data)
```

---

### home.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Template Example</title>
</head>
<body>
    <h1>Hello {{ name }}</h1>
    <p>Welcome to {{ course }}</p>
</body>
</html>
```

---

## ▶️ Output

When running the server and visiting:

```
http://127.0.0.1:8000/
```

The page displays dynamic data rendered from the backend.

---

🔥 Day 32 Complete – Backend Connected to Frontend!
