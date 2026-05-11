# Day 80 – Combining Search + Filter + Sort in Flask

## 📌 Overview

In this project, I learned how to combine search, filtering, and sorting functionalities in a Flask application using SQLAlchemy.

This type of system is commonly used in:

- Admin dashboards
- E-commerce websites
- Product management systems
- CRM applications
- Inventory systems

Users can:

- Search products by name
- Filter products by category
- Sort products alphabetically

This creates a more realistic dashboard-like experience.

---

# 🛠 What I Did

- Created a Flask application with SQLite
- Added product records to the database
- Implemented search functionality
- Added category filtering
- Added ascending/descending sorting
- Combined all queries dynamically
- Built a clean UI for interactions

---

# 📂 Folder Structure

```plaintext
flask-search-filter-sort/
│
├── app.py
├── products.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# 🧠 Key Concepts Learned

- Combining SQLAlchemy queries
- Using `filter()`
- Using `order_by()`
- Dynamic query building
- Handling GET parameters
- Search systems in Flask
- Filtering records dynamically
- Sorting database results

---

# 💻 Example Code

## app.py

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))

@app.route('/')
def index():

    search = request.args.get('search', '')
    category = request.args.get('category', '')
    sort = request.args.get('sort', 'asc')

    products = Product.query

    if search:
        products = products.filter(Product.name.contains(search))

    if category:
        products = products.filter_by(category=category)

    if sort == 'asc':
        products = products.order_by(Product.name.asc())
    else:
        products = products.order_by(Product.name.desc())

    products = products.all()

    return render_template(
        'index.html',
        products=products,
        search=search,
        category=category,
        sort=sort
    )

if __name__ == '__main__':

    with app.app_context():

        db.create_all()

        if not Product.query.first():

            sample_products = [
                Product(name='Laptop', category='Electronics'),
                Product(name='Phone', category='Electronics'),
                Product(name='Shoes', category='Fashion'),
                Product(name='T-Shirt', category='Fashion'),
                Product(name='Python Book', category='Education')
            ]

            db.session.add_all(sample_products)
            db.session.commit()

    app.run(debug=True)
```

---

## templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Search Filter Sort System</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="container">

    <h1>Flask Search + Filter + Sort</h1>

    <form method="GET">

        <input
            type="text"
            name="search"
            placeholder="Search product..."
            value="{{ search }}"
        >

        <select name="category">
            <option value="">All Categories</option>

            <option value="Electronics"
                {% if category == 'Electronics' %}selected{% endif %}>
                Electronics
            </option>

            <option value="Fashion"
                {% if category == 'Fashion' %}selected{% endif %}>
                Fashion
            </option>

            <option value="Education"
                {% if category == 'Education' %}selected{% endif %}>
                Education
            </option>
        </select>

        <select name="sort">
            <option value="asc"
                {% if sort == 'asc' %}selected{% endif %}>
                A-Z
            </option>

            <option value="desc"
                {% if sort == 'desc' %}selected{% endif %}>
                Z-A
            </option>
        </select>

        <button type="submit">Apply</button>

    </form>

    <div class="products">

        {% for product in products %}
            <div class="card">
                <h2>{{ product.name }}</h2>
                <p>{{ product.category }}</p>
            </div>
        {% endfor %}

    </div>

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
    width: 85%;
    margin: auto;
    padding: 30px;
}

h1 {
    text-align: center;
    margin-bottom: 30px;
}

form {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 30px;
    flex-wrap: wrap;
}

input,
select,
button {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

button {
    background: #333;
    color: white;
    cursor: pointer;
}

button:hover {
    background: #555;
}

.products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
```

---

# ▶️ Output / Result

Successfully implemented:

- Product searching
- Category filtering
- Product sorting
- Combined query system
- Dynamic dashboard behavior
- Responsive UI

Example URLs:

```plaintext
/?search=Phone
```

```plaintext
/?category=Fashion
```

```plaintext
/?search=Book&category=Education&sort=asc
```

---

# ✅ Summary

In Day 80, I learned how to combine search, filter, and sort operations in Flask using SQLAlchemy.

This project helped me understand how real-world dashboard systems work by dynamically building database queries based on user inputs.

I also learned:

- Dynamic query chaining
- Search systems using SQLAlchemy
- Sorting records
- Combining multiple filters
- Building scalable query logic

---
