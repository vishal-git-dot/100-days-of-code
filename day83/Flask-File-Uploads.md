# Day 83 – Flask File Uploads

## 📌 Overview

In this project, I learned how to upload files in Flask applications using Flask and Werkzeug utilities.

File uploads are commonly used in:

- User profile systems
- Blog CMS platforms
- Portfolio websites
- Admin dashboards
- Document management systems

In this project:

- Users can upload files/images
- Uploaded files are stored in a local uploads folder
- Flask handles file validation and saving

---

## 🛠 What I Did

- Created a Flask upload form
- Handled file uploads using POST requests
- Used `request.files`
- Saved uploaded files securely
- Created uploads directory
- Displayed upload success messages

---

## 📂 Folder Structure

```plaintext
flask-file-uploads/
│
├── app.py
├── uploads/
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🧠 Key Concepts Learned

- Flask file uploads
- `request.files`
- Handling POST requests
- Upload folders
- `secure_filename()`
- Saving uploaded files
- HTML file forms

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():

    message = ''

    if request.method == 'POST':

        file = request.files['file']

        if file and file.filename != '':

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    filename
                )
            )

            message = 'File uploaded successfully!'

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
```

---

### templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask File Uploads</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="container">

    <h1>Flask File Upload System</h1>

    <form method="POST" enctype="multipart/form-data">

        <input type="file" name="file" required>

        <button type="submit">
            Upload File
        </button>

    </form>

    {% if message %}
        <p class="success">{{ message }}</p>
    {% endif %}

</div>

</body>
</html>
```

---

### static/style.css

```css
body {
    margin: 0;
    padding: 0;
    background: #f4f4f4;
    font-family: Arial, sans-serif;
}

.container {
    width: 80%;
    margin: auto;
    padding: 40px;
    text-align: center;
}

h1 {
    margin-bottom: 30px;
}

form {
    background: white;
    padding: 30px;
    border-radius: 10px;
    display: inline-block;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

input {
    margin-bottom: 20px;
}

button {
    padding: 10px 20px;
    border: none;
    background: #333;
    color: white;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background: #555;
}

.success {
    margin-top: 20px;
    color: green;
    font-weight: bold;
}
```

---

## ▶️ Output / Result

Successfully implemented:

- File upload system
- Upload form handling
- File saving functionality
- Secure file naming
- Dynamic success messages

Example Upload Flow:

```plaintext
Select File → Upload → Saved in uploads/ folder
```

---

## ✅ Summary

In Day 83, I learned how file uploads work in Flask applications.

This project introduced:

- Upload forms
- Handling uploaded files
- Saving files securely
- Upload directories
- Flask request handling

These concepts are important for building real-world applications like:

- Social media apps
- Portfolio sites
- Admin dashboards
- Blogging systems
- CMS platforms

---
