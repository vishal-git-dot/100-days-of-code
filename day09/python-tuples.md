# 🐍 Day 9 – Python Tuples (100 Days of Code)

This document explains Python tuples with clear examples and beginner-friendly,
line-by-line explanations. Tuples are ordered, immutable collections used to store multiple values.

---

## 1️⃣ Creating and Printing Tuples

```python
this_tuple = ("apple", "banana", "cherry", "orange")
print(this_tuple)
```

**Explanation:**
- A tuple is created using parentheses `()`.
- Tuples can store multiple values of different types.

---

## 2️⃣ Length of a Tuple

```python
print("Length of tuple: ", len(this_tuple))
```

**Explanation:**
- `len()` returns the number of elements in the tuple.

---

## 3️⃣ Single-Item Tuple

```python
this_tuple1 = ("hai")
print(type(this_tuple1))

this_tuple2 = ("hello",)
print(type(this_tuple2))
```

**Explanation:**
- `("hai")` is treated as a string, not a tuple.
- A single-item tuple must include a comma.

---

## 4️⃣ Tuple with Numbers

```python
tuple1 = (1, 2, 3)
print(type(tuple1))
```

**Explanation:**
- Tuples can store numbers.
- `tuple1` is of type `tuple`.

---

## 5️⃣ Tuple Constructor

```python
con_tuple = tuple((1, 2, 3))
print(type(con_tuple))
print(con_tuple)
```

**Explanation:**
- `tuple()` converts another iterable into a tuple.

---

## 6️⃣ Accessing Tuple Items

```python
print(this_tuple[1])
```

**Explanation:**
- Tuples use zero-based indexing.

---

## 7️⃣ Checking if Item Exists

```python
if "apple" in this_tuple:
    print("success")
```

**Explanation:**
- `in` checks if a value exists inside the tuple.

---

## 8️⃣ Changing Tuple Values (Workaround)

```python
change_tuple = tuple((1, 2, 3, 9))

y = list(change_tuple)
y[1] = "apple"
change_tuple = tuple(y)
print(change_tuple)
```

**Explanation:**
- Tuples are immutable.
- Convert tuple → list → modify → convert back.

---

## 9️⃣ Tuple Unpacking

```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
```

**Explanation:**
- Tuple unpacking assigns values to variables.

---

## 🔟 Using Asterisk (*) in Unpacking

```python
fruits1 = ("papaya", "apple", "banana", "cherry", "orange")
(green1, *hai) = fruits1
print(green1)
print(hai)
```

**Explanation:**
- `*` collects remaining values into a list.

---

## 1️⃣1️⃣ Looping Through a Tuple

```python
for i in fruits1:
    print("--> ", i)
```

---

## 1️⃣2️⃣ Loop Using Index

```python
for i in range(len(fruits1)):
    print(f"index [{i}] = {fruits1[i]}")
```

---

## 1️⃣3️⃣ While Loop

```python
i = 0
while i < len(fruits1):
    print(f"index [{i}] = {fruits1[i]}")
    i += 1
```

---

## 1️⃣4️⃣ Joining Tuples

```python
join1 = ("apple", "banana", "cherry")
join2 = (1, 2, 3)

join = join1 + join2
print("after join : ", join)
```

---

## 1️⃣5️⃣ Multiplying Tuples

```python
print("multi : ", join1 * 2)
```

---

## 1️⃣6️⃣ Tuple Methods

```python
multi = join1 * 2
print("number of apple in tuple : ", multi.count("apple"))
print(join1.index("apple"))
```

---

✅ **End of Day 9 – Python Tuples**
