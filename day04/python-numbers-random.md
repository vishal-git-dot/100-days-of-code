# 🐍 Python Numbers, Conversion & Random – Day 4 (100 Days of Code)

This document explains Python numeric data types, type conversion, and random number generation
with clear examples and beginner-friendly explanations.

---

## 1️⃣ Integer Numbers

```python
x = 5
y = 34895895985
z = -556444

print(x, type(x)); print(y, type(y)); print(z, type(z))
```

**Explanation:**
- `x`, `y`, and `z` are integers (`int`).
- Python supports very large integers.
- `type()` shows the data type of each variable.

---

## 2️⃣ Floating Point Numbers

```python
a = 1.0
b = 3.567
c = -56.76
print(a, type(a)); print(b, type(b)); print(c, type(c))
```

**Explanation:**
- Float numbers contain decimal points.
- They are represented using the `float` data type.

---

## 3️⃣ Scientific Notation (Float)

```python
q = 12e3
w = 12E6
e = -67.7e34
print(q, type(q)); print(w, type(w)); print(e, type(e))
```

**Explanation:**
- `e` or `E` represents powers of 10.
- `12e3` means `12 × 10³`.
- Scientific notation values are of type `float`.

---

## 4️⃣ Complex Numbers

```python
r = 5j
t = 5 + 7j
y = -7j
print(r, type(r)); print(t, type(t)); print(y, type(y))
```

**Explanation:**
- Complex numbers use `j` as the imaginary part.
- Python stores them as `complex` type.

---

## 🔄 Type Conversion

```python
num_int = 7        # int
num_float = 5.67  # float

print(float(num_int))
print(complex(num_float))
```

**Explanation:**
- `float()` converts an integer to a float.
- `complex()` converts a number into a complex type.
- Python allows easy type conversion.

---

## 🎲 Random Numbers

```python
import random
print("Random Number", random.random())
print("Random With Range [1-10]", random.randrange(1, 10))
```

**Explanation:**
- `random.random()` generates a float between 0 and 1.
- `random.randrange(1, 10)` generates an integer from 1 to 9.
- The `random` module is used for randomness.

---

✅ **End of Day 4 – Python Numbers & Random**
