# Day 57 – Flask Form Validation

## 📌 Overview

Today I learned how to **validate form data in Flask** to ensure users enter correct and meaningful input.

Form validation helps:
- Prevent empty submissions ❌  
- Ensure correct data format ✅  
- Improve user experience 👍  

Since Flask is a micro-framework, validation is usually done **manually using Python logic**.

---

## 🛠 What I Did

- Added validation checks for form inputs
- Prevented empty form submission
- Displayed error messages in the template
- Passed validation feedback from backend to frontend
- Improved form reliability

---

## 📂 Folder Structure

```
Day57/
│
├── app.py
├── templates/
│   └── form.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Form Validation** → Checking user input before processing
- `request.form.get()` → Get form values
- Conditional checks in Python
- Sending error messages to templates
- Basic validation (empty fields, simple checks)

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    error = ""
    name = ""

    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            error = "Name is required!"
        else:
            return render_template("form.html", name=name)

    return render_template("form.html", error=error, name=name)

if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/form.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Form Validation</title>
</head>
<body>

<h2>Enter Your Name</h2>

<form method="POST">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Submit</button>
</form>

{% if error %}
    <p style="color:red;">{{ error }}</p>
{% endif %}

{% if name %}
    <h3>Hello, {{ name }}!</h3>
{% endif %}

</body>
</html>
```

---

## ▶️ Output / Result

- If user submits empty form:
```
Name is required!
```

- If valid input is entered:
```
Hello, John!
```

Validation ensures only proper input is processed.

---

## ✅ Summary

- Learned how to validate form inputs in Flask
- Prevented empty submissions
- Displayed error messages to users
- Improved form handling logic

---

✅ **Day 57 Completed**

Today I learned how to **implement basic form validation in Flask**, making user input handling more reliable and user-friendly.
