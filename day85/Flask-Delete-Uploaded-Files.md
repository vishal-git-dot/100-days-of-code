# Day 85 – Flask Delete Uploaded Files

## 📌 Overview

In this project, I learned how to delete uploaded files in Flask applications.

After learning how to upload files and preview images in previous lessons, the next logical step is file management. Real-world applications must allow users to remove files they no longer need.

This feature is commonly used in:

- Social media platforms
- Blogging systems
- Portfolio websites
- Content Management Systems (CMS)
- User profile management
- Document storage applications

In this project:

- Users can upload files
- View uploaded files
- Delete uploaded files
- Manage uploaded content dynamically

---

## 🛠 What I Did

- Created a file upload system
- Saved uploaded files into an uploads folder
- Displayed uploaded files dynamically
- Created a delete route
- Removed files using Python
- Updated the file list automatically after deletion
- Improved file management workflow

---

## 📂 Folder Structure

```plaintext
flask-delete-files/
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

### Flask File Uploads

Uploading files using:

```python
request.files
```

---

### Secure File Names

Using:

```python
secure_filename()
```

to safely store uploaded files.

---

### Listing Files

Using:

```python
os.listdir()
```

to display uploaded files.

---

### File Deletion

Using:

```python
os.remove()
```

to permanently remove files.

---

### Route Parameters

Using:

```python
@app.route('/delete/<filename>')
```

to dynamically delete selected files.

---

### Redirecting Users

Using:

```python
redirect(url_for('index'))
```

to refresh the page after actions.

---

## 💻 Example Code

### app.py

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.secret_key = "secret-key"

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["file"]

        if file and file.filename:

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            flash(
                f"{filename} uploaded successfully!",
                "success"
            )

        return redirect(url_for("index"))

    files = os.listdir(
        app.config["UPLOAD_FOLDER"]
    )

    return render_template(
        "index.html",
        files=files
    )


@app.route("/delete/<filename>")
def delete_file(filename):

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    if os.path.exists(filepath):

        os.remove(filepath)

        flash(
            f"{filename} deleted successfully!",
            "danger"
        )

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Flask File Manager</title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='style.css') }}"
    >

</head>

<body>

<div class="container">

    <h1>Flask File Manager</h1>

    {% with messages = get_flashed_messages(with_categories=true) %}

        {% if messages %}

            {% for category, message in messages %}

                <div class="alert {{ category }}">
                    {{ message }}
                </div>

            {% endfor %}

        {% endif %}

    {% endwith %}

    <form
        method="POST"
        enctype="multipart/form-data"
    >

        <input
            type="file"
            name="file"
            required
        >

        <button type="submit">
            Upload File
        </button>

    </form>

    <h2>Uploaded Files</h2>

    {% if files %}

        <ul>

            {% for file in files %}

                <li>

                    <span>
                        {{ file }}
                    </span>

                    <a
                        href="{{ url_for('delete_file', filename=file) }}"
                        class="delete-btn"
                    >
                        Delete
                    </a>

                </li>

            {% endfor %}

        </ul>

    {% else %}

        <p>No files uploaded yet.</p>

    {% endif %}

</div>

</body>
</html>
```

---

### static/style.css

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #f4f4f4;
    font-family: Arial, sans-serif;
}

.container {
    width: 80%;
    max-width: 900px;
    margin: 40px auto;
}

h1 {
    text-align: center;
    margin-bottom: 30px;
}

form {
    background: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
}

input[type="file"] {
    margin-bottom: 15px;
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

.alert {
    padding: 12px;
    margin-bottom: 15px;
    border-radius: 5px;
}

.success {
    background: #d4edda;
    color: #155724;
}

.danger {
    background: #f8d7da;
    color: #721c24;
}

ul {
    list-style: none;
}

li {
    background: white;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.delete-btn {
    text-decoration: none;
    color: white;
    background: crimson;
    padding: 8px 12px;
    border-radius: 5px;
}

.delete-btn:hover {
    background: darkred;
}
```

---

## ▶️ Output / Result

Successfully implemented:

- File upload system
- Dynamic file listing
- File deletion functionality
- Flash messages
- Upload folder management
- Responsive file manager UI

### Example Workflow

```plaintext
Upload File
     ↓
File Saved to uploads/
     ↓
File Appears in List
     ↓
Click Delete
     ↓
File Removed
     ↓
Success Message Displayed
```

---

## 🔥 Real-World Use Cases

This functionality is used in:

- Google Drive-like applications
- CMS systems
- Blog dashboards
- Portfolio websites
- Profile picture management
- Resume upload systems
- Admin dashboards

---

## ⚠️ Common Mistakes

### Forgetting secure_filename()

Bad:

```python
file.save(file.filename)
```

Good:

```python
filename = secure_filename(file.filename)
```

---

### Deleting Non-Existing Files

Always check:

```python
if os.path.exists(filepath):
```

before deleting.

---

### Missing Upload Folder

Always create:

```python
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)
```

---

## 🚀 Skills Gained

After completing Day 85, you can:

- Upload files
- Store files
- List files
- Delete files
- Manage upload directories
- Build simple file managers
- Create CMS-style file systems

---

## ✅ Summary

In Day 85, I learned how to manage uploaded files in Flask applications.

I built a complete file management system that allows users to:

- Upload files
- View uploaded files
- Delete files
- Maintain clean storage

This project introduced important backend concepts such as:

- File system operations
- Dynamic route parameters
- Upload management
- File deletion workflows

These concepts are widely used in production Flask applications and prepare me for more advanced backend development.

---
