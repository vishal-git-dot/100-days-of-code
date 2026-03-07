# Day 35 – Saving Form Data to Database in Django

## 📌 Overview

Today I learned how to **save form data into the database using Django Models**.  
Previously, I created simple forms and models separately. In this step, I connected them so that **data entered in the form gets stored in the database automatically**.

This is an important step in building real web applications where users submit information such as **contact forms, registrations, feedback, or blog posts**.

---

## 🛠 What I Did

- Created a Django **Model** to store form data
- Created a **Form based on the Model**
- Connected the **Form with a View**
- Saved submitted data to the **database**
- Displayed the form on an HTML template
- Tested the form submission

---

## 📂 Folder Structure

```
Day35/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
├── app/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   └── contact.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **Django Model** → Defines the database structure
- **ModelForm** → Automatically creates a form from a model
- **POST Request** → Used when submitting form data
- **form.is_valid()** → Validates user input
- **form.save()** → Saves form data into the database
- **CSRF Token** → Protects forms from security attacks

---

## 💻 Example Code

### models.py

```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
```

---

### forms.py

```python
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
```

---

### views.py

```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
```

---

### urls.py (app)

```python
from django.urls import path
from .views import contact_view

urlpatterns = [
    path("contact/", contact_view, name="contact"),
]
```

---

### contact.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
</head>
<body>

<h2>Contact Us</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">Submit</button>
</form>

</body>
</html>
```

---

## ▶️ Output / Result

- A **Contact Form** appears in the browser
- User enters:
  - Name
  - Email
  - Message
- When the form is submitted:
  - Django validates the data
  - Data is **saved to the database automatically**
- The saved entries can be viewed later through the **Django Admin Panel or database**

Example submitted data stored in database:

| Name | Email | Message |
|-----|-----|-----|
| John | john@email.com | Hello Django |

---

✅ **Day 35 Completed**

Today I successfully connected **Forms + Models + Database** in Django, allowing user input to be permanently stored in the database.
