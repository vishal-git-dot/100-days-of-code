
### Day 27 – Simple HTML Form with PHP & MySQL Insert

## 📌 What I Built
- Created a basic HTML signup form
- Connected PHP to MySQL database
- Inserted user data into database table
- Practiced backend form handling

---

## 🖥️ HTML Form (Frontend)

- Form method: POST
- Action file: insert.php
- Fields:
  - Name
  - Email
  - Password
  - Confirm Password
- Buttons:
  - Submit
  - Reset

---

## 🗄️ PHP Backend Logic

### Steps Performed:
1. Collected form data using `$_REQUEST`
2. Connected to MySQL using `mysqli_connect`
3. Checked database connection
4. Executed INSERT query
5. Displayed success/failure alert
6. Closed connection

---

## ⚠️ Important Learning Points

- Database name used: `phpcurd`
- Table name: `users`
- Used basic SQL INSERT query
- Understood frontend ↔ backend connection flow

---

## ✅ What I Learned

- How form data is sent to PHP
- How to connect PHP to MySQL
- How to insert data into database
- Basic backend workflow understanding

# User Table Documentation

## 📌 Overview

This document describes the structure of the `users` table in the database.  
The table is designed to store basic user account information including name, email, and password.

---

## 🗂 Table Name

```
users
```

---

## 🏗 Table Structure

| Column Name | Data Type | Length | Null | Key | Extra | Description |
|------------|-----------|--------|------|-----|-------|------------|
| user_id   | INT       | 4      | NO   | PRI | AUTO_INCREMENT | Unique identifier for each user |
| name      | VARCHAR   | 25     | NO   | —   | — | User's full name |
| mail      | VARCHAR   | 25     | NO   | —   | — | User's email address |
| password  | VARCHAR   | 25     | NO   | —   | — | User's account password |

---

## 🛠 SQL Table Creation Script

```sql
CREATE TABLE users (
    user_id INT(4) NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    mail VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    PRIMARY KEY (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

---

## 📖 Field Descriptions

### 1️⃣ `user_id`
- Type: `INT(4)`
- Primary Key
- Auto-incremented
- Uniquely identifies each user record

### 2️⃣ `name`
- Type: `VARCHAR(25)`
- Required field
- Stores the user's name

### 3️⃣ `mail`
- Type: `VARCHAR(25)`
- Required field
- Stores the user's email address

### 4️⃣ `password`
- Type: `VARCHAR(25)`
- Required field
- Stores the user's password
