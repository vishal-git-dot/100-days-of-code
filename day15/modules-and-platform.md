# Day 15 – Python Modules and Platform Information

## 📌 Importing Modules in Python

Python allows you to reuse code by importing **modules**. Modules can be built-in, external, or custom-created files.

---

## ✅ Code Example
```python
# import Day_12_modules
import platform
from Day_12_modules import person2

# Day_12_modules.greeting("Boney")
# print(Day_12_modules.person["name"])

print(platform.system())
print(person2["name"])
```

---

## 🧠 Explanation (Line by Line)

- `import platform`  
  Imports Python’s built-in **platform** module, which provides information about the operating system.

- `from Day_12_modules import person2`  
  Imports only the `person2` object from your custom module `Day_12_modules`.

- `platform.system()`  
  Returns the name of the operating system (e.g., Windows, Linux, Darwin).

- `person2["name"]`  
  Accesses the value of the `"name"` key from the dictionary imported from another file.

---

## 📦 Why Use Modules?
- Avoid rewriting the same code
- Organize code into reusable files
- Keep projects clean and maintainable

---

## ✅ Key Learnings
- Python supports built-in and custom modules
- `import module` vs `from module import item`
- The `platform` module reveals system information
- Dictionaries can be shared across files using imports
