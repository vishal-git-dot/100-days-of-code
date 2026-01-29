# 🐍 Day 8 – Python List Exercises

Today’s focus was **practicing list manipulation** with a variety of small problems and building familiarity with list operations, indexing, appending, sorting, slicing, and more.

---

## 🔹 Question 1 — List Creation and Manipulation

```python
# Create a list
mylist = [1, 2, 3, 4, 5, 6, 7]
print("mylist", mylist)
```

Creates a basic list of integers.

```python
# Print 5th item in list (index 4)
print(mylist[4])
```

Indexes are zero-based, so `mylist[4]` is 5.

```python
# Add 8, 9, 10 to the end
mylist.append(8)
mylist.append(9)
mylist.append(10)
```

Appending values one by one.

```python
# Insert 0 at index 3
mylist.insert(3, 0)
```

Insert `0` at 4th position.

```python
# Remove inserted 0
mylist.pop(3)
```

Removes the element at index 3.

```python
# Print sublists using slicing
print(mylist[0:6])  # [1, 2, 3, 4, 5, 6]
print(mylist[2:5])  # [3, 4, 5]
```

```python
# Print even numbers ≤ 6
even = []
for item in mylist:
    if item % 2 == 0 and item <= 6:
        even.append(item)
print(even)  # [2, 4, 6]
```

### 🔸 Negative Indexing

```python
print(mylist[-6])        # 5
print(mylist[-8:-5])     # [3, 4, 5]
print(mylist[:-6])       # [1, 2, 3, 4]
print(mylist[-8:-6])     # [3, 4]
```

Negative indexes start from the end.

```python
# Double the list
mylist.extend(mylist)
```

Duplicates the list by appending itself.

```python
# Sort the list
mylist.sort()
```

---

## 🔹 Question 2 — Modifying Another List

```python
mylist1 = [8, 9, 10]
mylist1.insert(1, 17)
mylist1.extend([4, 5, 6])
mylist1.pop(0)  # Remove first entry (8)
mylist1.sort()
mylist1.extend(mylist1)  # Double it
mylist1.insert(3, 25)
```

Practicing insert, extend, pop, sort, and duplicate.

---

## 🔹 Question 3 — List Algorithms

```python
mylist2 = [1, 2, 3, 4, 5, 6, 7]
```

### Length of list (2 ways)

```python
print("length using len", len(mylist2))

# Manual count using flag
count = 0
for item in mylist2:
    count += 1
print("length using flag", count)
```

### Reversing

```python
mylist2.reverse()
```

### Sum of list

```python
sum = 0
for item in mylist2:
    sum += item
print("sum", sum)
```

### Even & Odd Filtering

```python
for item in mylist2:
    if item % 2 == 0:
        print(item, end=" ")  # Even
for item in mylist2:
    if item % 2 != 0:
        print(item, end=" ")  # Odd
```

---

✅ **End of Day 8 – Hands-on List Practice**
