# Day 62 – Flask Delete Records

## 📌 Overview

Today I learned how to **delete records in a Flask application using SQLite**.

After implementing Create, Read, and Update operations, the final step in CRUD is **Delete**, which allows users to remove data from the database.

In this lesson, I added functionality to:
- Delete existing user data
- Remove records from the database
- Reflect changes instantly in the UI

---

## 🛠 What I Did

- Created a **delete route with dynamic ID**
- Selected a specific record using its ID
- Deleted the record using SQL `DELETE`
- Redirected back to the list page after deletion

---

## 📂 Folder Structure

```
Day62/
│
├── app.py
├── database.db
├── templates/
│   ├── list.html
│   └── confirm_delete.html
└── README.md
```

---

## 🧠 Key Concepts Learned

- **Delete (CRUD)** → Remove existing records
- `DELETE FROM table WHERE id=?`
- Dynamic routes using `<int:id>`
- Redirect after deleting data
- Handling user actions safely

---

## 💻 Example Code

### app.py

```python
import sqlite3
from flask import Flask, render_template, redirect

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


# Delete user
@app.route("/delete/<int:id>")
def delete_user(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
```

---

### templates/list.html

```html
<h2>Users</h2>

<a href="/add">Add User</a>

<ul>
{% for user in users %}
    <li>
        {{ user[1] }}
        <a href="/edit/{{ user[0] }}">Edit</a>
        <a href="/delete/{{ user[0] }}">Delete</a>
    </li>
{% endfor %}
</ul>
```

---

## ▶️ Output / Result

1. Open user list:
http://127.0.0.1:5000/

2. Click **Delete** next to a user

3. Record is removed from the database

4. Page refreshes automatically

Example:

Before:
John
Alice

After:
Alice

---

## ✅ Summary

- Implemented **Delete operation in Flask**
- Used dynamic routes to identify records
- Removed data using SQL `DELETE`
- Updated UI instantly after deletion

---

✅ **Day 62 Completed**

Today I learned how to **delete records in Flask using SQLite**, completing the full CRUD cycle.
