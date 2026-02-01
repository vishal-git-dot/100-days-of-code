# 🐍 Day 11 – Python Dictionaries (100 Days of Code)

This file contains explained examples for working with **dictionaries in Python**, which are collections of key-value pairs.

---

## 🔹 Creating and Printing Dictionaries

```python
thisdict = {
    "name" : "john",
    "age" : 22,
    "place" : "kottayam",
    "class" : ["plusone","plustwo"],
}

print(thisdict)
print()
print(type(thisdict))
print()
print("Length", len(thisdict))
print()
```

- Dictionaries are created using `{}` with key-value pairs.
- Values can be of any data type, including lists.
- `type()` confirms it's a dictionary.
- `len()` returns number of key-value pairs.

---

## 🔹 Using the `dict()` Constructor

```python
dict_const = dict(name="john", age=22)
print(dict_const)
```

- `dict()` is another way to create a dictionary.

---

## 🔹 Accessing Dictionary Elements

```python
print('thisdict["name"] : ', thisdict["name"])
print("thisdict.get('name') : ", thisdict.get("name"))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
```

- Access values using square brackets or the `get()` method.
- `keys()` returns all keys.
- `values()` returns all values.
- `items()` returns list of key-value pairs.

---

## 🔹 Modifying Values

```python
x = dict_const.values()
print(x)
dict_const["name"] = "varun"
print(x)

dict_const.update({"age": 55})
print(x)
```

- `dict.values()` returns a dynamic view, updated on change.
- Direct assignment or `update()` modifies dictionary values.

---

## 🔹 Checking Key Existence

```python
if "name" in thisdict:
    print("'name' exists in thisdict")
```

- Use `in` keyword to check if a key exists.

---

✅ **End of Day 11 – Python Dictionaries**
