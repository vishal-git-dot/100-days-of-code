# Day 58 – Flask Redirects & URL Handling

## 📌 Overview

Today I learned how to **redirect users and handle URLs in Flask** using `redirect()` and `url_for()`.

These are important for:
- Navigating between pages 🔄  
- Avoiding duplicate form submissions 🚫  
- Writing clean and maintainable URL logic  

Instead of hardcoding URLs, Flask encourages using **`url_for()`** to dynamically generate routes.

---

## 🛠 What I Did

- Used `redirect()` to move users between pages
- Used `url_for()` to generate dynamic URLs
- Redirected after form submission
- Avoided hardcoding URLs
- Improved navigation flow in the app

---

## 📂 Folder Structure

```
Day58/
│
├── app.py
├── templates/
│   ├── form.html
│   └── success.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **redirect()** → Redirects user to another route
- **url_for()** → Generates URL using function name
- Helps avoid hardcoded URLs
- Improves code maintainability
- Commonly used after form submission

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("success", username=name))

    return render_template("form.html")


@app.route("/success/<username>")
def success(username):
    return render_template("success.html", name=username)


if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/form.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Form</title>
</head>
<body>

<h2>Enter Your Name</h2>

<form method="POST">
    <input type="text" name="name" placeholder="Enter name">
    <button type="submit">Submit</button>
</form>

</body>
</html>
```

---

### templates/success.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>

<h2>Form Submitted Successfully!</h2>
<p>Hello, {{ name }}!</p>

</body>
</html>
```

---

## ▶️ Output / Result

1. Open:
```
http://127.0.0.1:5000/
```

2. Enter name and submit form

3. Automatically redirected to:
```
/success/YourName
```

Output:
```
Form Submitted Successfully!
Hello, YourName!
```

---

## ✅ Summary

- Learned to use `redirect()` for navigation
- Used `url_for()` to dynamically generate URLs
- Improved form handling workflow
- Avoided hardcoding URLs

---

✅ **Day 58 Completed**

Today I learned how to **handle redirects and manage URLs in Flask**, making applications more dynamic and maintainable.
