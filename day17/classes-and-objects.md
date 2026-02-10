# Day 17 – Object-Oriented Programming (Classes & Objects) in Python

## 📌 Introduction to Classes and Objects
Python supports **Object-Oriented Programming (OOP)**, which helps organize code using **classes** and **objects**.

- **Class** → blueprint
- **Object** → instance of a class

---

## ✅ Example 1: Simple Class

```python
class MyClass:
    x = 6
    v = 5

p1 = MyClass()

print(p1.x * 10)
print(p1.v)
```

### 🧠 Explanation
- `MyClass` defines two class variables.
- `p1 = MyClass()` creates an object.
- Variables are accessed using dot notation.

---

## ✅ Example 2: Class with Constructor (`__init__`)

```python
class MyCars:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printcars(self):
        print(f"Name: {self.name} and price: {self.price}")

cars = MyCars("BMW", 100)
cars = MyCars("Alto", 200)

cars.printcars()
```

### 🧠 Explanation
- `__init__()` runs automatically when an object is created.
- `self` refers to the current object.
- Second object overwrites the first (`BMW` is replaced by `Alto`).

---

## ✅ Example 3: Methods Calling Methods

```python
class person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

    def welcome(self):
        message = self.greet()
        print(message, "Welcome to python")

p1 = person("John")
p1.welcome()
```

### 🧠 Explanation
- One method (`welcome`) calls another (`greet`).
- Promotes code reuse.

---

## ✅ Example 4: Calculator Class

```python
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

num = calculator(2, 3)

print(num.add())
print(num.sub())
print(num.mul())
```

### 🧠 Explanation
- Encapsulates operations into a class.
- Easy to reuse and extend.

---

## ✅ Example 5: Movie List Manager

```python
class mymovies:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Movie {movie} was added.")

    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)
        print(f"Movie {movie} was removed.")

    def show_movies(self):
        print(self.name)
        for movie in self.movies:
            print(f" - {movie}")
```

### 🧠 Explanation
- Uses a list inside a class.
- Demonstrates real-world object modeling.

---

## ✅ Key Learnings
- Classes group data and behavior together
- `__init__()` initializes object data
- Methods define object actions
- Objects can manage internal lists and logic
- OOP improves code structure and readability
