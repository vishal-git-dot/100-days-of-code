# Day 61 – Flask Update Records

## 📌 Overview

Today I learned how to **update existing records in a Flask application using SQLite**.

After implementing **Create and Read**, the next step in CRUD is **Update**, which allows users to modify existing data.

In this lesson, I added functionality to:
- Edit existing user data
- Update records in the database
- Reflect changes in the UI

---

## 🛠 What I Did

- Created an **edit route with dynamic ID**
- Fetched a specific record from the database
- Pre-filled the form with existing data
- Updated the record using SQL `UPDATE`
- Redirected back to the list page after update

---

## 📂 Folder Structure

```
Day61/
│
├── app.py
├── database.db
├── templates/
│   ├── form.html
│   ├── list.html
│   └── edit.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Update (CRUD)** → Modify existing records
- `UPDATE table SET column=? WHERE id=?`
- Dynamic routes using `<int:id>`
- Pre-filling form fields with existing data
- Redirect after updating

---

## 💻 Example Code

### app.py

```python
import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Fetch all users
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("list.html", users=users)


# Edit user
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form.get("name")

        cursor.execute("UPDATE users SET name=? WHERE id=?", (name, id))
        conn.commit()
        conn.close()

        return redirect("/")

    cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    user = cursor.fetchone()
    conn.close()

    return render_template("edit.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/list.html (Add Edit Link)

```html
<h2>Users</h2>

<a href="/add">Add User</a>

<ul>
{% for user in users %}
    <li>
        {{ user[1] }}
        <a href="/edit/{{ user[0] }}">Edit</a>
    </li>
{% endfor %}
</ul>
```

---

### templates/edit.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit User</title>
</head>
<body>

<h2>Edit User</h2>

<form method="POST">
    <input type="text" name="name" value="{{ user[1] }}">
    <button type="submit">Update</button>
</form>

<a href="/">Back</a>

</body>
</html>
```

---

## ▶️ Output / Result

1. Open user list:
```
http://127.0.0.1:5000/
```

2. Click **Edit** next to a user

3. Form appears with existing data

4. Update name and submit

5. Redirected back to list with updated data

Example:

Before:
```
John
```

After:
```
John Updated
```

---

## ✅ Summary

- Implemented **Update operation in Flask**
- Used dynamic routes to identify records
- Pre-filled form with existing data
- Updated database records using SQL

---

✅ **Day 61 Completed**

Today I learned how to **update existing records in Flask using SQLite and dynamic routes**, completing another step in CRUD operations.
