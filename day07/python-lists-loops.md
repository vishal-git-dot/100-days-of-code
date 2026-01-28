# 🐍 Day 7 – Python Lists & Loops

This document covers Python list operations and looping techniques with simple examples.
It also covers advanced list operations like list comprehension and joining lists.

---

## 1️⃣ List Creation and Basic Operations

```python
mylist = ["bmw", "volvo", "audi", "benz"]
print(mylist)
print()
print("Length: ", len(mylist))
print(type(mylist))
```

### Explanation (line-by-line)
- `mylist = ["bmw", "volvo", "audi", "benz"]` creates a list of car brands.
- `len(mylist)` returns the number of elements in the list.
- `type(mylist)` shows that the variable `mylist` is of type `list`.

---

## 2️⃣ Using the `list()` Constructor

```python
thislist = list(("hai", "hello", "world"))
print(thislist)
```

### Explanation:
- `list()` is used to create a list from another iterable (like a tuple).

---

## 3️⃣ Indexing & Slicing Lists

```python
print(mylist[0])
print(mylist[-1])
print(mylist[1:3])
print(mylist[:3])
print(mylist[2:])
print()
```

### Explanation:
- `mylist[0]` accesses the first element (index starts from 0).
- `mylist[-1]` accesses the last element using negative indexing.
- `mylist[1:3]` slices the list from index 1 to 2 (excluding index 3).
- `mylist[:3]` slices the list from the beginning to index 2.
- `mylist[2:]` slices the list from index 2 to the end.

---

## 4️⃣ Modifying a List

```python
thislist[1] = "halo"
print(thislist)
print()
thislist.insert(2, "blackcurrent")
print(thislist)
print()
```

### Explanation:
- `thislist[1] = "halo"` changes the value at index 1.
- `thislist.insert(2, "blackcurrent")` inserts `"blackcurrent"` at index 2.

---

## 5️⃣ Adding, Removing, and Clearing List Items

```python
addlist = ["black", "yellow", "red"]
print(addlist)
addlist.append("white")
print(addlist)
addlist.remove("white")
print(addlist)
addlist.pop()
print(addlist)
addlist.clear()
print(addlist)
print()
```

### Explanation:
- `addlist.append("white")` adds `"white"` to the end of the list.
- `addlist.remove("white")` removes the first occurrence of `"white"`.
- `addlist.pop()` removes the last element.
- `addlist.clear()` removes all elements from the list.

---

## 6️⃣ Looping Through a List

```python
loop_list = ["dog", "cat", "bird"]

for x in loop_list:
    print(x)
print("index loop")

for i in range(len(loop_list)):
    print(f"index {i} : {thislist[i]}")

print()
print("While loop")
i = 0
while i < len(loop_list):
    print(f"index {i} : {thislist[i]}")
    i = i + 1
```

### Explanation:
- `for x in loop_list:` loops through each element in the list.
- `for i in range(len(loop_list)):` uses the index to loop through the list.
- `while i < len(loop_list):` runs a while loop to print each element based on the index.

---

## 7️⃣ List Comprehension

```python
[print(x) for x in thislist]

print()
fruits = ["cherry", "apple", "banana", "kiwi", "mango"]
newfruits = [x for x in fruits if "a" in x]
print(newfruits)
capfruits = [x.upper() for x in fruits]
print(capfruits)
print()
```

### Explanation:
- List comprehension creates a list from an existing one with an optional condition.
- `[x for x in fruits if "a" in x]` filters the list based on whether `"a"` is in each fruit.
- `[x.upper() for x in fruits]` converts each fruit name to uppercase.

---

## 8️⃣ Sorting and Reversing Lists

```python
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
```

### Explanation:
- `fruits.sort()` sorts the list in ascending order.
- `fruits.sort(reverse=True)` sorts the list in descending order.
- `fruits.reverse()` reverses the order of the list.

---

## 9️⃣ Copying a List

```python
copy_of_fruits = fruits.copy()
print(copy_of_fruits)
```

### Explanation:
- `copy_of_fruits = fruits.copy()` creates a shallow copy of the list.

---

## 🔟 Joining Lists

```python
print(fruits)
print(mylist)
print()
join_1 = fruits + mylist
print(join_1)
mylist.extend(fruits)
print(mylist)
```

### Explanation:
- `fruits + mylist` joins the two lists.
- `mylist.extend(fruits)` adds all elements of `fruits` to `mylist`.

---

✅ **End of Day 7 – Python Lists & Loops**
