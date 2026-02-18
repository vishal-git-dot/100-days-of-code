# Day 22 – Multiple Class Practice (OOP Reinforcement)

## 📌 Focus of Today
Today you practiced creating multiple independent classes:
- Person
- Car
- Book
- Area of Circle
- Area of Rectangle

This reinforces **Object-Oriented Programming fundamentals**.

---

## ✅ 1) Person Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"My name is {self.name} and my age is {self.age}")

p1 = Person("John", 22)
p1.myfunc()
```

### 🧠 What You Learned
- How to store attributes using `self`
- How to define and call object methods

---

## ✅ 2) Car Class

```python
class Cars:
    def __init__(self, name, model, year):
        self.make = name
        self.model = model
        self.year = year

    def mycar(self):
        print(f"My car is {self.make}, model {self.model}, year {self.year}")

car1 = Cars("Toyota", 26, 19)
car1.mycar()
```

### 🧠 Improvement Tip
Class names should follow **PascalCase** (`Cars`, not `cars`).

---

## ✅ 3) Books Class

```python
class Books:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def mybook(self):
        print(f"My book is {self.name}, author {self.author}, year {self.year}")

book1 = Books("Harry Potter", "JK Rowling", 19)
book1.mybook()
```

---

## ✅ 4) Area of Circle

```python
class AreaOfCircle:
    def __init__(self, radius):
        self.radius = radius

    def myareaofcircle(self):
        return 3.14 * self.radius ** 2

circle1 = AreaOfCircle(4)
print(circle1.myareaofcircle())
```

### 🧠 Better Practice
For better accuracy:
```python
import math
math.pi
```

---

## ✅ 5) Area of Rectangle

```python
class AreaOfRectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def myareaofrectangle(self):
        return self.a * self.b

rectangle1 = AreaOfRectangle(2, 5)
print(rectangle1.myareaofrectangle())
```

---

## ✅ Key Learnings
- Classes encapsulate related data and behavior
- `self` refers to the current object
- Methods can return values or print values
- Naming conventions matter (PascalCase for classes)
- OOP improves structure and readability

---

## 🧠 Pro Tip
When writing calculation classes:
- Prefer returning values instead of printing
- Use built-in modules like `math` for precision
