# Day 25 – Finding the Largest Number in a List (With Dry Run)

## 📌 Problem
Find the largest number in a list without using built-in functions like `max()`.

---

## ✅ Code

```python
mylist = [1,2,3,4,5,6,7,8,9,0]

small = mylist[0]

for num in mylist:
    if num > small:
        small = num

print(small)
```

---

## ⚠️ Small Naming Note
Variable name `small` is misleading because we are actually storing the **largest value**.

Better name:

```python
largest = mylist[0]
```

---

# 🔎 Dry Run Explanation (Step-by-Step)

### Initial State:

```
mylist = [1,2,3,4,5,6,7,8,9,0]
small = 1
```

---

### Iteration 1:
```
num = 1
1 > 1 → False
small = 1
```

### Iteration 2:
```
num = 2
2 > 1 → True
small = 2
```

### Iteration 3:
```
num = 3
3 > 2 → True
small = 3
```

### Iteration 4:
```
num = 4
4 > 3 → True
small = 4
```

### Iteration 5:
```
num = 5
5 > 4 → True
small = 5
```

### Iteration 6:
```
num = 6
6 > 5 → True
small = 6
```

### Iteration 7:
```
num = 7
7 > 6 → True
small = 7
```

### Iteration 8:
```
num = 8
8 > 7 → True
small = 8
```

### Iteration 9:
```
num = 9
9 > 8 → True
small = 9
```

### Iteration 10:
```
num = 0
0 > 9 → False
small = 9
```

---

## ✅ Final Output

```
9
```

---

## 🧠 What’s Happening?

- Start by assuming the first element is the largest.
- Compare each element with the current largest.
- If a bigger number is found, update it.
- At the end of the loop, you have the maximum value.

---

## ✅ Time Complexity

- O(n) → We check each element once.

---

## 🧠 Better Version (Cleaner)

```python
mylist = [1,2,3,4,5,6,7,8,9,0]

largest = mylist[0]

for num in mylist:
    if num > largest:
        largest = num

print(largest)
```

---

## 🧠 Pro Tip
Python already provides:

```python
max(mylist)
```

But learning the manual logic builds strong algorithm skills.
