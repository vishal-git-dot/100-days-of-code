# Day 21 – File Handling in Python (read, write, append)

## 📌 What is File Handling?
File handling allows Python programs to **read from** and **write to files** stored on disk.

Common file modes:
- `"r"` → read
- `"w"` → write (overwrites)
- `"a"` → append
- `"x"` → create file (error if exists)

---

## ❌ Issue in Original Logic (Important)

```python
file = open(f"{filename}.txt","r")
if file:
    print("already exists")
else:
    print("created")
```

❌ Problem:
- `open(..., "r")` **fails if file does not exist**
- `if file:` will always be `True` if `open()` succeeds
- File existence must be checked using `try/except`

---

## ✅ Correct & Working Version

```python
filename = input("Enter a filename: ")
session = f"{filename}.txt"

# 1) Try reading the file
try:
    file = open(session, "r")
    print(f"{session} already exists!")
    print(file.read())
    file.close()
except FileNotFoundError:
    print(f"{session} not found. Creating new file...")
    open(session, "w").close()

# 2) Append new text
print(f"Add new line to {session}")
text = input("Enter a text: ")

file = open(session, "a")
file.write(text + "\n")
file.close()

# 3) Read again
file = open(session, "r")
print("After write:")
print(file.read())
file.close()
```

---

## ✅ Reading Specific Parts of a File

```python
f = open("test.txt", "r")
print(f.read(4))     # Reads first 4 characters
print(f.readline()) # Reads one line
f.close()
```

---

## 🧠 Explanation

### 1) `open(filename, mode)`
Opens a file in a specific mode:
- `"r"` → read existing file
- `"a"` → append content
- `"w"` → overwrite or create

### 2) `read()`
Reads the **entire file** content.

### 3) `read(4)`
Reads **only the first 4 characters**.

### 4) `readline()`
Reads **one line at a time**.

### 5) `FileNotFoundError`
Raised when trying to read a file that doesn’t exist.

---

## ✅ Key Learnings
- Files must exist before opening in `"r"` mode
- Use `try/except` to safely handle missing files
- `"a"` appends data without deleting old content
- Always close files after use
- File handling is essential for real-world programs

---

## 🧠 Pro Tip
Use `with open(...) as file:` to auto-close files (best practice).
