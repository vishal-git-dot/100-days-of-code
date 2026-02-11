# Day 18 – Inheritance in Python (Parent & Child Classes)

## 📌 What is Inheritance?
**Inheritance** allows one class (**child/subclass**) to reuse attributes and methods from another class (**parent/superclass**).  
This helps avoid repeating code and makes programs easier to expand.

- **Parent class** → base/shared features  
- **Child class** → inherits + can add/override features

---

## ✅ Part 1: Inheriting Without Changes (`pass`)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name, self.age)


class Student(Person):
    pass


p1 = Student("John", 25)
p1.show_details()
```

### 🧠 Explanation (Line by Line)
- `class Person:` creates a parent class with `name`, `age`, and `show_details()`.
- `class Student(Person):` makes **Student** inherit from **Person**.
- `pass` means: “don’t add anything new yet”.
- `Student("John", 25)` works because Student inherits `__init__()` from Person.
- `p1.show_details()` works because Student inherits that method too.

---

## ✅ Part 2: Child Class With Its Own Method (and its own `__init__`)

Your code shows that:
- A `Person` object can **not** call student-only methods.
- A `Student` object can call both parent methods and student-only methods.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name, "Age:", self.age)

class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    def show_details_stu(self):
        print("Name in students :", self.name, "Age:", self.age)


x = Person("John", 25)
x.show_details()

try:
    x.show_details_stu()
except Exception as e:
    print(e)

print()

x1 = Student("Roy", 25)
x1.show_details()
x1.show_details_stu()
```

### 🧠 What’s happening?
- `x = Person(...)` → has only **Person** methods, so `show_details_stu()` causes an error.
- `x1 = Student(...)` → inherits from Person, so it can call:
  - `show_details()` (parent method)
  - `show_details_stu()` (child method)

### ✅ Best practice upgrade (optional)
Instead of:
```python
Person.__init__(self, name, age)
```
Use:
```python
super().__init__(name, age)
```
`super()` is the modern + preferred way.

---

## ✅ Part 3: Book and Publisher Example

```python
class Book:
    def __init__(self, title, author, price, pub):
        self.title = title
        self.author = author
        self.price = price
        self.pub = pub

    def book_info(self):
        print(self.title, self.author, self.price, self.pub)

class Publisher(Book):
    def __init__(self, title, author, price, pub):
        Book.__init__(self, title, author, price, pub)

    def show_publisher(self):
        print(f"{self.title} is published by: {self.pub}")


book1 = Publisher("Harry Potter", "JK Rowling", "1500", "DC Books")
book2 = Book("Book1", "Authorr", "1500", "Mango Books")

book2.book_info()

book1.show_publisher()
book1.book_info()

try:
    book2.show_publisher()
except Exception as e:
    print(e)

book2.book_info()
```

### 🧠 Explanation
- `Publisher` inherits everything from `Book`.
- `Publisher` adds a new method: `show_publisher()`.
- `book2` is a `Book`, so it doesn’t have `show_publisher()` → that’s why it errors.

---

## ✅ Key Learnings
- Inheritance lets child classes reuse parent code
- `pass` is useful for an empty subclass
- Child classes can add new methods
- Parent objects cannot access child-only methods
- Prefer `super().__init__()` for constructor inheritance

---

## 🧾 Mini Challenge (optional)
Try adding **discount** support to `Book`:
- add a method `apply_discount(percent)`
- update `price`
- print the new price
