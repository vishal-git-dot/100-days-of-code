# Day 26 – Finding the Maximum Number (With Dry Run)

## 📌 Problem
Find the maximum number in a list manually (without using `max()`).

---

## ✅ Code

```python
mylist = [1,2,3,4,5,6,7,8,9,77]

val = mylist[0]

for i in mylist:
    if i > val:
        val = i

print(val)
```

---

## 🔎 Dry Run (Step-by-Step)

### Initial State:

```
mylist = [1,2,3,4,5,6,7,8,9,77]
val = 1
```

---

### Iterations:

| Current i | Comparison | Updated val |
|------------|------------|-------------|
| 1 | 1 > 1 → False | 1 |
| 2 | 2 > 1 → True | 2 |
| 3 | 3 > 2 → True | 3 |
| 4 | 4 > 3 → True | 4 |
| 5 | 5 > 4 → True | 5 |
| 6 | 6 > 5 → True | 6 |
| 7 | 7 > 6 → True | 7 |
| 8 | 8 > 7 → True | 8 |
| 9 | 9 > 8 → True | 9 |
| 77 | 77 > 9 → True | 77 |

---

## ✅ Final Output

```
77
```

---

## 🧠 What’s Happening?

- Assume the first element is the largest.
- Compare each element with the current maximum.
- Update when a bigger number is found.
- After the loop ends, `val` contains the largest number.

---

## ✅ Time Complexity

- O(n) → The loop checks each element once.

---

## 🧠 Cleaner Version

```python
largest = mylist[0]

for number in mylist:
    if number > largest:
        largest = number

print(largest)
```

---

## 🧠 Pro Tip
Python shortcut:

```python
max(mylist)
```

But writing it manually improves algorithm skills and interview preparation.
