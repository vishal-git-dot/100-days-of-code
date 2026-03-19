# Day 46 – File Uploads in Django

## 📌 Overview

Today I learned how to **upload files (especially images) in Django**.

File uploads are essential for many applications such as:
- Profile pictures 👤
- Blog images 🖼️
- Documents 📄

Django provides built-in support for handling file uploads using **FileField** and **ImageField**, along with proper media configuration.

---

## 🛠 What I Did

- Added an **ImageField** to the model
- Configured **MEDIA settings** in Django
- Created a form to upload files
- Handled file uploads in views using `request.FILES`
- Displayed uploaded images in templates
- Tested file upload functionality

---

## 📂 Folder Structure

```
Day46/
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
├── media/
│   └── images/
│
├── templates/
│   └── upload.html
│
└── manage.py
```

---

## 🧠 Key Concepts Learned

- **FileField / ImageField** → Used for file uploads
- `request.FILES` → Handles uploaded files
- `MEDIA_ROOT` → Directory where files are stored
- `MEDIA_URL` → URL to access uploaded files
- Forms must include `enctype="multipart/form-data"`

---

## 💻 Example Code

### models.py

```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
```

---

### forms.py

```python
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'image']
```

---

### views.py

```python
from django.shortcuts import render
from .forms import ProfileForm

def upload_file(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()

    return render(request, "upload.html", {"form": form})
```

---

### settings.py (Important)

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
```

---

### urls.py (project level)

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### upload.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>

<h2>Upload Profile Image</h2>

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">Upload</button>
</form>

</body>
</html>
```

---

## ▶️ Output / Result

- A form appears with:
  - Name field
  - Image upload option
- User selects an image and submits the form
- Image is stored inside the **media/images/** folder
- File upload works successfully

Example:

```
Name: John
Image: profile.jpg
```

The uploaded image is saved and can be displayed later in templates.

---

✅ **Day 46 Completed**

Today I learned how to **handle file uploads in Django using ImageField, forms, and media configuration**, enabling support for images and files in web applications.
