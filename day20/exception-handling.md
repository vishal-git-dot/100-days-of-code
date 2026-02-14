# Day 20 – Exception Handling in Python (try, except, else, finally, raise)

## 📌 What is Exception Handling?
Exception handling allows your program to **handle runtime errors gracefully** instead of crashing.

Python uses:
- `try`
- `except`
- `else`
- `finally`
- `raise`

---

## ✅ Example 1: try–except–else–finally

```python
try:
    print(x)
except:
    print("error")
else:
    print("no error")
finally:
    print("this is the finally block")
```

### 🧠 Explanation
- `try` → code that might cause an error
- `except` → runs if an error occurs
- `else` → runs if **no error** occurs
- `finally` → runs **always**, whether error occurs or not

---

## ✅ Example 2: Handling ValueError

```python
num = input("Enter a number: ")

try:
    num = int(num)
except ValueError as e:
    print(e)
```

### 🧠 Explanation
- `input()` returns a **string**
- `int(num)` may fail if input is not numeric
- `ValueError` is raised for invalid conversion
- The error message is captured in `e`

---

## ❌ Problem in Original Code (Important)

```python
x = input("Enter a number: ")

if not type(x) is int:
    raise TypeError("Please enter a number")
```

❌ This **always raises an error** because:
- `input()` **always returns a string**
- `type(x)` will never be `int`

---

## ✅ Correct Way to Use `raise`

```python
x = input("Enter a number: ")

try:
    x = int(x)
except ValueError:
    raise TypeError("Please enter a valid number")
```

### 🧠 Explanation
- Convert input first
- Raise a **custom error** only if conversion fails
- This is the correct real-world pattern

---

## ✅ Key Learnings
- Exception handling prevents program crashes
- `else` runs only when no exception occurs
- `finally` always runs (cleanup code)
- `raise` is used to throw custom errors
- `input()` always returns a string

---

## 🧠 Pro Tip
Always **convert first, then validate** user input.
