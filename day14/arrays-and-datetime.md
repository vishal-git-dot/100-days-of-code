# Day 14 – Arrays (Lists) and DateTime in Python

## 📌 Arrays (Lists) in Python

In Python, **arrays** are commonly represented using **lists**. Lists are used to store multiple values in a single variable.

### ✅ Code Example
```python
arrays = ["hai", "hello", "goodbye"]

print(arrays[0])
print()

for i in arrays:
    print(i)

arrays[0] = "toyota"
print(arrays)

arrays.append("honda")
print(arrays)
print()

arrays.remove("honda")
print(arrays)
print()
```

### 🧠 Explanation (Line by Line)

- `arrays = ["hai", "hello", "goodbye"]`  
  Creates a list with three string elements.

- `print(arrays[0])`  
  Prints the **first element** of the list (index starts from 0).

- `for i in arrays:`  
  Loops through each element in the list.

- `arrays[0] = "toyota"`  
  Updates the first element of the list.

- `arrays.append("honda")`  
  Adds a new element to the **end** of the list.

- `arrays.remove("honda")`  
  Removes a specific element from the list.

---

## 📌 Date and Time using `datetime` Module

Python provides the `datetime` module to work with dates and times.

### ✅ Code Example
```python
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)

print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("century : %C"))
print(x.strftime("%c"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%M"))
print(x.strftime("%m"))
```

### 🧠 Explanation

- `datetime.datetime.now()`  
  Gets the **current date and time**.

- `x.year`  
  Extracts the year.

- `strftime()`  
  Formats date and time into readable strings.

### 📅 Common Format Codes Used

| Code | Meaning |
|-----|--------|
| %A | Full weekday name |
| %a | Short weekday name |
| %B | Full month name |
| %b | Short month name |
| %C | Century |
| %c | Local date & time |
| %H | Hour (24-hour) |
| %I | Hour (12-hour) |
| %M | Minutes |
| %m | Month number |

---

## ✅ Key Learnings
- Lists allow storing and modifying multiple values
- Indexing starts from 0 in Python
- `append()` and `remove()` modify lists
- `datetime` helps work with real-world date and time
- `strftime()` formats dates into readable strings
