# Day 24 – Different Ways to Clear a List in Python

## 📌 Focus of Today
Today you explored multiple ways to **clear (empty) a list** in Python.

---

## ✅ Method 1: Using `.clear()` (Best & Cleanest)

```python
mylist = [1,2,3,4,5,6,7,8,9]
print(mylist)

mylist.clear()
print("After Cleared :", mylist)
```

### 🧠 Explanation
- `.clear()` removes **all elements** from the list.
- The list still exists, but it becomes empty: `[]`
- ✅ Recommended method.

---

## ✅ Method 2: Using `pop()` in a Loop

```python
mylist1 = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(mylist1)):
    mylist1.pop()

print("Cleared using pop :", mylist1)
```

### 🧠 Explanation
- `pop()` removes the last element each time.
- Loop runs until list becomes empty.
- ⚠️ Not efficient compared to `.clear()`.

---

## ✅ Method 3: Using `remove()` in a Loop

```python
mylist2 = [4,5,6,7,8,9]

for i in mylist2[:]:
    mylist2.remove(i)

print("Using remove:", mylist2)
```

### 🧠 Explanation
- `mylist2[:]` creates a **copy of the list**
- Loop removes each element one by one
- ⚠️ Slower and not recommended for large lists

---

# ➕ Additional Ways to Clear a List

## ✅ Method 4: Reassign to Empty List

```python
mylist = []
```

- Creates a new empty list.
- ⚠️ If other variables reference the old list, they will not be cleared.

---

## ✅ Method 5: Using `del`

```python
del mylist[:]
```

- Deletes all elements using slicing.
- Similar effect to `.clear()`.

---

## 🧠 Comparison Summary

| Method | Recommended | Notes |
|--------|------------|-------|
| `.clear()` | ✅ Yes | Cleanest and fastest |
| `pop()` loop | ❌ No | Unnecessary looping |
| `remove()` loop | ❌ No | Slow for big lists |
| `mylist = []` | ⚠️ Depends | Creates new list |
| `del mylist[:]` | ✅ Yes | Good alternative |

---

## ✅ Key Learnings
- `.clear()` is the best and most readable way
- Multiple approaches exist, but not all are efficient
- Reassigning creates a new list object
- `del` with slicing removes all elements

---

## 🧠 Pro Tip
In real-world code, prefer:

```python
mylist.clear()
```

It is clean, readable, and efficient.
