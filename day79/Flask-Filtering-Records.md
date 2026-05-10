# Day 79 – Flask Filtering Records

## 📌 Overview

In this project, I learned how to filter database records in Flask using SQLAlchemy.  
Filtering helps users display only the data they need based on selected conditions.

This is a very important feature used in:

- Admin dashboards
- E-commerce websites
- Search systems
- Product filtering
- User management panels

In this project, users can filter products by category dynamically.

---

# 🛠 What I Did

- Created a Flask app with SQLite database
- Added product records
- Implemented filtering using `filter_by()`
- Displayed filtered products dynamically
- Used query parameters in URLs
- Built a simple filter navigation UI

---

# 📂 Folder Structure

```plaintext
flask-filtering-records/
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

- SQLAlchemy filtering
- `filter_by()` usage
- Dynamic URL query parameters
- Retrieving GET request values
- Rendering filtered database results
- Conditional database queries

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

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))

# Home Route
@app.route('/')
def index():

    category = request.args.get('category')

    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()

    return render_template('index.html', products=products)

# Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Sample Data
        if not Product.query.first():
            sample_products = [
                Product(name='Laptop', category='Electronics'),
                Product(name='Phone', category='Electronics'),
                Product(name='Shirt', category='Clothing'),
                Product(name='Shoes', category='Clothing'),
                Product(name='Book', category='Education')
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
    <title>Flask Filtering Records</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <div class="container">

        <h1>Product Filtering System</h1>

        <div class="filters">
            <a href="/">All</a>
            <a href="/?category=Electronics">Electronics</a>
            <a href="/?category=Clothing">Clothing</a>
            <a href="/?category=Education">Education</a>
        </div>

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
    font-family: Arial, sans-serif;
    background: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    padding: 30px;
}

h1 {
    text-align: center;
    color: #333;
}

.filters {
    text-align: center;
    margin-bottom: 30px;
}

.filters a {
    text-decoration: none;
    padding: 10px 20px;
    background: #333;
    color: white;
    margin: 5px;
    border-radius: 5px;
}

.filters a:hover {
    background: #555;
}

.products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
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

Features working successfully:

- Display all products
- Filter products by category
- Dynamic filtering using URL parameters
- Responsive product card layout
- Database-driven filtering system

Example URLs:

```plaintext
/
```

```plaintext
/?category=Electronics
```

```plaintext
/?category=Clothing
```

---

# ✅ Summary

In Day 79, I learned how to filter records in Flask using SQLAlchemy’s `filter_by()` method.

This project introduced dynamic querying and category-based filtering, which are commonly used in real-world applications like dashboards, admin panels, and e-commerce websites.

I also learned how to:

- Use query parameters
- Handle GET requests
- Build dynamic filtering systems
- Display filtered database results

---

