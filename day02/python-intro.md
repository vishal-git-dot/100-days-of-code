# 🐍 Python Introduction – Day 2 (100 Days of Code)

This document covers basic Python concepts with clear examples.
Each section explains what the code does in simple language.

---

## 1️⃣ Printing Text

```python
print("Hello World")
```

**Explanation:**
- `print()` displays output on the screen.
- `"Hello World"` is a string.

---

## 2️⃣ Using Variables

```python
a = "Hello World via Variables"
print(a)
```

**Explanation:**
- A variable stores data.
- `a` stores text and `print(a)` shows it.

---

## 3️⃣ Arithmetic Operations

```python
print("5 + 3 = ", 5 + 3)
print("5 - 3 = ", 5 - 3)
print("5 * 3 = ", 5 * 3)
```

**Explanation:**
- `+` adds numbers
- `-` subtracts numbers
- `*` multiplies numbers

---

## 4️⃣ Multiple Print Statements

```python
print("")
print("Hello"); print(4); print("world")
```

**Explanation:**
- `print("")` prints a blank line.
- Multiple statements can be on one line using `;`.

---

## 5️⃣ Multi-line Comments

```python
'''
This is
a
multi line code
'''
```

```python
"""
This is
a
multi line code
"""
```

**Explanation:**
- Triple quotes are used for multi-line comments or documentation.

---

## 6️⃣ Variable Reassignment

```python
x = 5
x = "hello"
print(x)
```

**Explanation:**
- Variables can change values.
- Python is dynamically typed.

---

## 7️⃣ Type Casting

```python
x = str(3)
y = int(3)
z = float(3)
print(x); print(y); print(z)
```

**Explanation:**
- `str()` converts to string
- `int()` converts to integer
- `float()` converts to decimal

---

## 8️⃣ Checking Data Type

```python
print(type(z))
```

**Explanation:**
- `type()` tells the data type of a variable.

---

## 9️⃣ Assigning Multiple Variables

```python
j = k = l = "orange"
print("j", j); print("k", k); print("l", l)
```

**Explanation:**
- Same value can be assigned to multiple variables.

---

## 🔟 Unpacking a List

```python
fruits = ["apple", "banana", "cherry"]
index1, index2, index3 = fruits
print(index1, index2, index3)
```

**Explanation:**
- List values are assigned to variables in order.

---

## 1️⃣1️⃣ Global vs Local Variable

```python
global_variable = "global"

def myfunction():
    global_variable = "inside"
    print(global_variable)

myfunction()
print(global_variable)
```

**Explanation:**
- Variables inside a function are local.
- The global variable remains unchanged.

---

✅ **End of Day 2 – Python Basics**
