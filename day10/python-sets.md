# 🐍 Day 10 – Python Sets (100 Days of Code)

This file includes explained examples of working with **sets in Python** — an unordered, unindexed, and mutable collection with no duplicate items.

---

## 🔹 Creating Sets

```python
iset = {6,7,8,9,10}
print(iset)
print(type(iset))

isset = set((1,2,3,4,5))
print(isset)
print("Type of isset : ", type(isset))
```

- Curly braces `{}` create a set.
- `set()` constructor can convert other iterables into a set.

---

## 🔹 Adding and Removing Elements

```python
iset.add("hello")
print(iset)

iset.remove(6)
print(iset)
```

- `add()` adds a new item to the set.
- `remove()` deletes an item; raises an error if it doesn’t exist.

```python
print(f"the length of iset is {len(iset)}")
```

- `len()` gets the number of elements.

```python
iset.pop()
```

- `pop()` removes a random element from the set.

```python
iset.discard(5)
print(iset)
```

- `discard()` removes an item **without error** if it doesn’t exist.

---

## 🔹 Accessing Items in a Set

```python
for x in iset:
    print(x)

if "hello" in iset:
    print("true")
else:
    print("false")
```

- Use a loop to iterate.
- Use `in` keyword to check for membership.

---

## 🔹 Updating Sets

```python
iset.update(isset)
print(iset)
```

- `update()` adds elements from another set.

---

## 🔹 Joining Sets

```python
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9,10}

set3 = set1.union(set2)
print(set3)
```

- `union()` joins sets (removes duplicates).

```python
set5 = set1.intersection(set2)
print(set5)
```

- `intersection()` returns items present in both sets.

```python
set4 = set1.difference(set2)
print(set4)
```

- `difference()` returns items only in the first set.

```python
set1.intersection_update(set2)
print(set1)
```

- `intersection_update()` keeps only items found in both sets and modifies the set in-place.

---

✅ **End of Day 10 – Python Sets**
