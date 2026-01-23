# 🐍 Python Strings – Indexing, Slicing, Methods & Formatting (Day 4)

This document covers Python **string basics** including:
- printing and multiline strings
- indexing and looping through strings
- `in` keyword checks
- slicing (positive and negative indices)
- common string methods (`upper`, `lower`, `strip`, `replace`, `split`)
- concatenation and f-strings
- escape sequences

---

## 1️⃣ Printing a String

```python
print("HEllO")
```

**Explanation:**
- `print()` displays text on the screen.
- `"HEllO"` is a string value.

---

## 2️⃣ Multiline String Variable

```python
print()
a = '''
this is
a
multiline
variable
'''
print(a)
```

**Explanation (line-by-line):**
- `print()` prints a blank line for spacing.
- `a = ''' ... '''` creates a multiline string stored in variable `a`.
- `print(a)` prints the multiline text.

---

## 3️⃣ String Indexing

```python
x = "hello"
print(x[3])
```

**Explanation:**
- Strings are indexed starting from `0`.
- `x[3]` means the 4th character in `"hello"` → `l`.

---

## 4️⃣ Looping Through a String + Length

```python
print()

y = "banana"
for f in y:
    print(f)
print("length of string: ", y, len(y))
print()
```

**Explanation (line-by-line):**
- `print()` creates a blank line.
- `y = "banana"` stores a string.
- `for f in y:` loops through each character in the string.
- `print(f)` prints each character one by one.
- `len(y)` returns the length of the string.
- Final `print()` adds spacing.

---

## 5️⃣ Checking if a Substring Exists (`in` keyword)

```python
txt = "This is a sample string"
print("is" in txt)

if "is" in txt:
    print("is", "is present in txt")
```

**Explanation (line-by-line):**
- `"is" in txt` returns `True` if the substring exists, otherwise `False`.
- The `if` statement runs only when `"is"` is found inside `txt`.

---

## 6️⃣ String Slicing

```python
slice_text = "hello, wor"
#-------------0123456789
print(slice_text[2:5])
print()
print(slice_text[:5])
print()
print(slice_text[2:])
print()
print(slice_text[-5:-2])
```

**Explanation (line-by-line):**
- `slice_text[2:5]` gets characters from index 2 up to (not including) 5.
- `slice_text[:5]` gets from the start up to index 5 (not included).
- `slice_text[2:]` gets from index 2 to the end.
- `slice_text[-5:-2]` uses negative indexing (from the end).

---

## 7️⃣ Common String Methods

```python
l = "hello, woRld"
print(l.upper())
print()

k = "HELLO , WoRLD"
print(k.lower())
print()

j = "hello, world!      "
print(j.strip())
print()

print(j.replace("h", "j"))
print()

print(j.split(','))
print()
```

**Explanation (line-by-line):**
- `.upper()` converts all characters to uppercase.
- `.lower()` converts all characters to lowercase.
- `.strip()` removes extra spaces from the start/end.
- `.replace("h","j")` replaces all `h` characters with `j`.
- `.split(',')` splits the string into a list using comma as separator.

---

## 8️⃣ Concatenation and f-Strings

```python
txt1 = "hai"
txt2 = 'python'

print(txt1 + txt2)
print()

print(txt1, " ", txt2)
print()

num = 56
print(f"hai my age is {num} years old")
```

**Explanation (line-by-line):**
- `txt1 + txt2` joins strings directly (no space unless you add it).
- `print(txt1, " ", txt2)` prints them with spacing.
- `f"..."` is an f-string that inserts variables using `{}`.

---

## 9️⃣ Escape Sequences

```python
txt3 = "hello \'your name\' and this is the age \"34\" \nthis is the new line\tthis is the tab\f \x56 \110"
print(txt3)
print()
```

**Explanation (line-by-line):**
- `\'` prints a single quote `'` inside the string.
- `\"` prints a double quote `"` inside the string.
- `\n` creates a new line.
- `\t` creates a tab space.
- `\f` is a form-feed character (rarely used).
- `\x56` is a hexadecimal escape code.
- `\110` is an octal escape code.

---

✅ **End of Day 4 – Python Strings**
