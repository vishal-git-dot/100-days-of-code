# Day 56 – Flask Forms (GET & POST)

## 📌 Overview

Today I learned how to handle **forms in Flask** using **GET and POST methods**.

Forms allow users to send data from the browser to the server. Flask provides the `request` object to access this data.

I also understood the difference between:
- **GET** → Used to retrieve data
- **POST** → Used to send data securely

---

## 🛠 What I Did

- Created a simple HTML form
- Handled form submission using Flask
- Used `request.form` to get user input
- Worked with both GET and POST methods
- Displayed submitted data in the browser

---

## 📂 Folder Structure

```
Day56/
│
├── app.py
├── templates/
│   └── form.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Forms** → Used to collect user input
- `request.form` → Access POST form data
- `request.args` → Access GET data
- **GET method**:
  - Data visible in URL
  - Used for fetching data
- **POST method**:
  - Data sent in request body
  - More secure for sensitive data

---

## 💻 Example Code

### app.py

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    name = ""

    if request.method == "POST":
        name = request.form.get("name")

    return render_template("form.html", name=name)

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

{% if name %}
    <h3>Hello, {{ name }}!</h3>
{% endif %}

</body>
</html>
```

---

## ▶️ Output / Result

Run the app:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

- Enter a name in the form
- Click **Submit**

Output:
```
Hello, YourName!
```

---

## ✅ Summary

- Learned how to create and handle forms in Flask
- Used GET and POST methods
- Retrieved form data using `request.form`
- Displayed user input dynamically

---

✅ **Day 56 Completed**

Today I learned how to **handle user input using Flask forms with GET and POST methods**, enabling interaction between frontend and backend.
