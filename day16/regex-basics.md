# Day 16 – Regular Expressions (re) in Python

## 📌 What are Regular Expressions?
**Regular Expressions (Regex)** are patterns used to search, match, and manipulate text.  
Python’s built-in **`re`** module gives you tools like:

- `re.findall()` → find all matches
- `re.split()` → split a string by a pattern
- (common next step) `re.sub()` → replace text by pattern

---

## ✅ Your Code (Cleaned + Fixed)

Your original code had a few small quote/parenthesis issues in some `print()` lines.  
Below is the same program with those lines corrected so it runs properly.

```python
import re

txt = "Hello , My name is Robin"
txt1 = "Hello 43, My name is Robin , 34343"
txt2 = "hello"

# 1) Character set: letters a to g
x = re.findall("[a-g]", txt)
print(x)

# 2) Digits \d (find digits in txt1)
y = re.findall(r"\d", txt1)
print(y)

# 3) Wildcard dot . (two dots means "any two characters")
print(re.findall("He..o", txt1))

# 4) Starts-with anchor ^
r = re.findall("^h", txt2)
if r:
    print("String starts with 'h'")
else:
    print("String does not start with 'h'")

# 5) Quantifiers: *, +, ?, {m}
print(re.findall("he.*o", txt2))   # * = 0 or more characters
print(re.findall("he.+o", txt2))   # + = 1 or more characters
print(re.findall("he.?o", txt2))   # ? = 0 or 1 character
print(re.findall("he.{2}o", txt2)) # {2} = exactly 2 characters

# 6) OR operator |
d = re.findall("name|don", txt)
if d:
    print("String contains 'name'")
else:
    print("String does not contain 'name'")

print("-------------------------------------")
new_text = "The rain in Spain"

# 7) Special sequences
ab = re.findall(r"\AThe", new_text)   # \A = beginning of the string
print("Match" if ab else "No match")

bc = re.findall(r"\Bai", new_text)    # \B = not at a word boundary
print("Match" if bc else "No match")

cd = re.findall(r"\d", new_text)      # \d = digits
print("Match" if cd else "No match")

de = re.findall(r"\D", new_text)      # \D = non-digits
print("Match" if de else "No match")

ef = re.findall(r"\s", new_text)      # \s = whitespace
print("Match" if ef else "No match")

fe = re.findall(r"\S", new_text)      # \S = non-whitespace
print("Match" if fe else "No match")

yu = re.findall(r"\w", new_text)      # \w = word characters (letters/digits/_)
print("Match" if yu else "No match")

yo = re.findall(r"\W", new_text)      # \W = non-word characters
print("Match" if yo else "No match")

err = re.findall(r"Spain\Z", new_text)  # \Z = end of string
print("Match" if err else "No match")

# 8) Split by whitespace
dfg = re.split(r"\s", new_text)
print(dfg)
```

---

## 🧠 Explanation (Beginner-Friendly)

### 1) `re.findall(pattern, text)`
Returns a **list** of all matches.

- `"[a-g]"` → finds any character between a and g.
- `"\d"` → finds digits.
- `"He..o"` → matches **He + any 2 chars + o** (example: `Hello` matches).

### 2) Anchors
- `"^h"` → checks if the string **starts** with `h`.
- `"Spain\Z"` → checks if the string **ends** with `Spain`.

### 3) Quantifiers
- `*` → 0 or more
- `+` → 1 or more
- `?` → 0 or 1
- `{2}` → exactly 2 characters

### 4) Special sequences
- `\A` → start of string
- `\B` → not a word boundary
- `\D` → not a digit
- `\s` → whitespace
- `\S` → non-whitespace
- `\w` → word char
- `\W` → non-word char
- `\Z` → end of string

### 5) Splitting
- `re.split("\s", new_text)` splits the sentence wherever there’s whitespace.

---

## ✅ Key Learnings
- Regex helps search and validate text patterns
- `findall()` returns all matches as a list
- Anchors (`^`, `\A`, `\Z`) check start/end positions
- Quantifiers (`*`, `+`, `?`, `{m}`) control how much text matches
- `re.split()` breaks strings using patterns (like spaces)

---

## ⭐ Quick Improvement Tip
When using backslashes in regex, **raw strings** are cleaner:

```python
re.findall(r"\d", text)   # better than "\\d"
```

(That’s why the fixed code uses `r"..."` often.)
