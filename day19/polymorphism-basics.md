# Day 19 – Polymorphism in Python (Same Method, Different Behavior)

## 📌 What is Polymorphism?
**Polymorphism** means *many forms*.  
In Python, it allows different classes to have methods with the **same name** but **different behavior**.

---

## ❌ Error in Original Code

Your original line:
```python
x.teeth() [fix errors]
```
This causes a **syntax error** because `[fix errors]` is not valid Python code.

---

## ✅ Fixed & Working Code

```python
class NewBorn:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def teeth(self):
        print("I am born")


class MiddleAge:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def teeth(self):
        print("I am full")


class Adult:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def teeth(self):
        print("Partial")


newborn1 = NewBorn("John", 1)
middleAge1 = MiddleAge("John", 20)
adult1 = Adult("John", 80)

for x in (newborn1, middleAge1, adult1):
    print(x.name)
    print(x.age)
    x.teeth()
```

---

## 🧠 Explanation

- All three classes define a method named **`teeth()`**
- The method name is the same, but the behavior is different
- Python decides **which method to call at runtime**
- This is **polymorphism without inheritance**
- Python uses **duck typing** (if it behaves like a duck, it is a duck)

---

## ✅ Key Learnings
- Same method name across different classes
- Objects can be looped together if they share behavior
- Method execution depends on object type
- Polymorphism improves flexibility and clean design

---

## 🧠 Pro Tip
You can later combine polymorphism **with inheritance** for even cleaner designs.
