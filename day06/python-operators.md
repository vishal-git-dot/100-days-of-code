# 🐍 Day 6 – Python Operators (Comparison, Logical, Identity, Bitwise & Membership)

This document covers advanced Python operators with clear examples and
line-by-line explanations for easy understanding.

---

## 1️⃣ Comparison Operators

```python
xc = 5
yc = 3

print(xc == yc)
print(xc != yc)
print(xc > yc)
print(xc < yc)
print(xc >= yc)
print(xc <= yc)
print()
```

### Explanation
- `==` checks equality
- `!=` checks inequality
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

---

## 2️⃣ Logical Operators

```python
xl = 4
yl = 3

print(xl > 0 and xl < 10)
print(yl > 0 or yl < 1)
print(not(xl > 0 and xl < 10))
print()
```

### Explanation
- `and` → True if both conditions are true
- `or` → True if one condition is true
- `not` → reverses the condition

---

## 3️⃣ Identity Operators

```python
xi = ["arun", "anu"]
yi = ["arun", "anu"]
zi = xi

print(xi is yi)
print(xi is zi)
print(xi == yi)
print(xi is not yi)
print()
```

### Explanation
- `is` compares memory location
- `==` compares values

---

## 4️⃣ Bitwise Operators

```python
print(6 & 2)
print(6 | 2)
print(6 ^ 2)
print(~2)
print()
```

### Explanation
- `&` AND
- `|` OR
- `^` XOR
- `~` NOT

---

## 5️⃣ Membership Operators

```python
xmem = ["hai", "hello", "world"]
print(xmem)
print()

xmember = input("Enter anything: ")

if xmember in xmem:
    print(f"{xmember} is present in xmem")
else:
    print(f"{xmember} is not present in xmem")
```

### Explanation
- `in` checks membership
- `not in` checks absence

---

✅ End of Day 6 – Python Operators
