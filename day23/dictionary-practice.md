# Day 23 – Python Dictionaries Practice

## 📌 Focus of Today
Today you practiced working with **Python dictionaries**:
- Creating dictionaries
- Accessing items
- Modifying values
- Checking data types
- Copying and deleting keys

---

## ✅ Student Dictionary

```python
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 22,
    "marital_status": "Unmarried",
    "skills": ["Python", "C++", "Java"],
    "country": "India",
    "city": "Kottayam",
    "address": "new address",
}
```

---

## ✅ 1) Return Each Item

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

- `.items()` returns key–value pairs.

---

## ✅ 2) Get Dictionary Length

```python
len(student)
```

- Returns total number of keys.

---

## ✅ 3) Access Specific Values + Check Type

```python
print(student["skills"], student["country"], student["age"])
print(type(student["skills"]))
```

- `skills` is a **list**
- `country` is a **string**
- `age` is an **integer**

---

## ✅ 4) Modify Skills

```python
student.update({"skills": ["Python", "C++", "Java", "C#"]})
```

Better approach (recommended):
```python
student["skills"].append("C#")
```

---

## ✅ 5) Get Keys and Values

```python
student.keys()
student.values()
```

- `.keys()` returns dictionary keys
- `.values()` returns dictionary values

---

## ✅ 6) Remove Items

```python
student.pop("age")
```

- Removes key `"age"` from dictionary.

---

## ✅ 7) Copy Dictionary

```python
students = student.copy()
```

- Creates a shallow copy.

---

## ✅ 8) Remove City from Copied Dictionary

```python
students.pop("city")
```

- Original dictionary remains unchanged.

---

## ✅ Key Learnings
- Dictionaries store data using key–value pairs
- `.items()`, `.keys()`, `.values()` are essential methods
- `.update()` modifies dictionary values
- `.pop()` removes keys safely
- `.copy()` creates a separate dictionary
- Lists inside dictionaries can be modified independently

---

## 🧠 Pro Tip
Instead of replacing the entire skills list, prefer:
```python
student["skills"].append("New Skill")
```
This keeps existing data intact.
