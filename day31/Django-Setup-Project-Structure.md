# Day 31 -- Django Setup & Project Structure 🚀

------------------------------------------------------------------------

## 📌 Objective

Learn how to:

-   Install Django
-   Create a Django project
-   Understand project structure
-   Run development server
-   Create first Django app

------------------------------------------------------------------------

## 🐍 What is Django?

Django is a high-level Python web framework used to build secure and
scalable web applications.

It follows the **MVT Pattern**:

-   Model → Database\
-   View → Logic\
-   Template → Frontend (HTML)

------------------------------------------------------------------------

## 🛠 Step 1 -- Install Django

``` bash
pip install django
```

Check installation:

``` bash
django-admin --version
```

------------------------------------------------------------------------

## 🏗 Step 2 -- Create a Django Project

``` bash
django-admin startproject myproject
cd myproject
```

Run server:

``` bash
python manage.py runserver
```

Open in browser:

    http://127.0.0.1:8000/

If setup is correct, Django welcome page will appear 🎉

------------------------------------------------------------------------

## 📂 Project Structure

    myproject/
    │
    ├── manage.py
    └── myproject/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py

------------------------------------------------------------------------

## 📖 Important Files Explanation

### manage.py

Command line utility to run project commands.

### settings.py

Main configuration file: - Installed apps - Database settings -
Middleware - Templates

### urls.py

Handles URL routing.

### wsgi.py / asgi.py

Used for deployment.

------------------------------------------------------------------------

## 🧩 Step 3 -- Create an App

Create app:

``` bash
python manage.py startapp myapp
```

App structure:

    myapp/
    │
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── tests.py
    └── migrations/

------------------------------------------------------------------------

## 📝 Step 4 -- Register App

Open `settings.py`

Add inside INSTALLED_APPS:

``` python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

------------------------------------------------------------------------

## 🌍 Step 5 -- Create First View

Inside `views.py`:

``` python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django Day 31!")
```

------------------------------------------------------------------------

## 🔗 Step 6 -- Configure URLs

### Create `urls.py` inside myapp:

``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### Connect to main project `urls.py`:

``` python
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
]
```

------------------------------------------------------------------------

## ▶️ Run Server Again

``` bash
python manage.py runserver
```

Visit:

    http://127.0.0.1:8000/

Output:

    Hello Django Day 31!

------------------------------------------------------------------------

## 🎯 What I Learned Today

-   Installed Django\
-   Created Django project\
-   Understood project structure\
-   Created app\
-   Connected URL to view\
-   Ran development server successfully

------------------------------------------------------------------------

🔥 Day 31 Complete -- Entering Backend Development World!
