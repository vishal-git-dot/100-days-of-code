# Day 84 – Flask Image Upload Preview

## 📌 Overview

In this project, I learned how to preview uploaded images in Flask applications using Flask file handling and dynamic rendering.

This feature is commonly used in:

- Social media applications
- User profile systems
- Blogging platforms
- Portfolio websites
- Admin dashboards

In this project:

- Users can upload images
- Uploaded images are stored in an uploads folder
- Uploaded images are previewed dynamically on the webpage

---

# 🛠 What I Did

- Created an image upload form
- Handled image uploads using Flask
- Saved uploaded images securely
- Displayed uploaded images dynamically
- Used Flask routes for serving uploaded files
- Styled the UI with CSS

---

# 📂 Folder Structure

```plaintext
flask-image-upload-preview/
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

# 🧠 Key Concepts Learned

- Flask image uploads
- request.files
- secure_filename()
- send_from_directory()
- Dynamic image rendering
- File storage handling
- Flask routes for uploaded files

---

# 💻 Example Code

## app.py

```python
from flask import (
    Flask,
    render_template,
    request,
    send_from_directory
)

from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():

    filename = None

    if request.method == 'POST':

        file = request.files['image']

        if file and file.filename != '':

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    filename
                )
            )

    return render_template(
        'index.html',
        filename=filename
    )

# Route to display uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename
    )

if __name__ == '__main__':
    app.run(debug=True)
```

---

## templates/index.html

```html
<!DOCTYPE html>
<html>
<head>

    <title>Flask Image Upload Preview</title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='style.css') }}"
    >

</head>
<body>

<div class="container">

    <h1>Flask Image Upload Preview</h1>

    <form method="POST" enctype="multipart/form-data">

        <input
            type="file"
            name="image"
            accept="image/*"
            required
        >

        <button type="submit">
            Upload Image
        </button>

    </form>

    {% if filename %}

        <div class="preview">

            <h2>Uploaded Image</h2>

            <img
                src="{{ url_for('uploaded_file', filename=filename) }}"
                alt="Uploaded Image"
            >

        </div>

    {% endif %}

</div>

</body>
</html>
```

---

## static/style.css

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
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #555;
}

.preview {
    margin-top: 40px;
}

.preview img {
    width: 300px;
    max-width: 100%;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Image upload system
- Dynamic image preview
- Uploaded image serving
- Responsive UI
- File storage handling

Example Workflow:

```plaintext
Select Image → Upload → Image Preview Displayed
```

---

# ✅ Summary

In Day 84, I learned how to build an image upload preview system in Flask.

This project introduced:

- File uploads
- Dynamic image rendering
- Serving uploaded files
- Upload folder handling
- Flask file management

These concepts are important for real-world applications like:

- Social media apps
- Blogging systems
- Portfolio websites
- User dashboards
- CMS platforms

---

