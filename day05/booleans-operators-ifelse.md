# 🐍 Day 5 – Booleans, Operators & If/Else Menu Program (100 Days of Code)

This Day 5 note covers:
- **Boolean truthy/falsy values**
- **Arithmetic operators**
- **Assignment operators (including bitwise assignments)**
- A small **menu-driven if/else program** that compares two numbers

Each code block is followed by easy explanations.

---

## 1️⃣ Boolean Values (Truthy / Falsy)

```python
print(bool("Hai"))
print(bool(34))
print()

print(bool(0))
print(bool(""))
print(bool(['name','name2']))
print()
```

### Explanation (line-by-line)
- `bool("Hai")` → `True` because a **non-empty string** is truthy.
- `bool(34)` → `True` because a **non-zero number** is truthy.
- `print()` → prints a **blank line** for spacing.
- `bool(0)` → `False` because **0 is falsy**.
- `bool("")` → `False` because an **empty string** is falsy.
- `bool(['name','name2'])` → `True` because a **non-empty list** is truthy.
- Final `print()` → spacing.

---

## 2️⃣ Arithmetic Operators

```python
xa = 15
ya = 2

print(" + ", xa + ya)
print(" - ", xa - ya)
print(" * ", xa * ya)
print(" / ", xa / ya)
print(" % ", xa % ya)
print(" ** ", xa ** ya)
print(" // ", xa // ya)
print()
```

### Explanation (line-by-line)
- `xa = 15` and `ya = 2` store two numbers.
- `xa + ya` → addition
- `xa - ya` → subtraction
- `xa * ya` → multiplication
- `xa / ya` → division (result is usually a float)
- `xa % ya` → modulus (remainder)
- `xa ** ya` → power (exponentiation)
- `xa // ya` → floor division (drops the decimal part)
- `print()` → spacing

---

## 3️⃣ Assignment Operators

```python
xas = 15

print("xas = ", xas)
xas += 3
print(" += ", xas)
xas -= 3
print(" -= ", xas)
xas *= 3
print(" *= ", xas)
xas /= 3
print(" /= ", xas)
xas %= 3
print(" %= ", xas)
xas **= 3
print(" **= ", xas)
xas //= 3
print(" //= ", xas)
xas &= 3
print(" &= ", xas)
xas |= 3
print(" |= ", xas)
xas ^= 3
print(" ^= ", xas)
xas >>= 3
print(" >>= ", xas)
xas <<= 3
print(" <<= ", xas)
print()
```

### Explanation (line-by-line)
- `xas = 15` sets the starting value.
- `xas += 3` → add 3 and store back in `xas`
- `xas -= 3` → subtract 3 and store back
- `xas *= 3` → multiply by 3 and store back
- `xas /= 3` → divide by 3 and store back
- `xas %= 3` → remainder when divided by 3 and store back
- `xas **= 3` → raise to the power 3 and store back
- `xas //= 3` → floor divide by 3 and store back
- `xas &= 3` → bitwise AND with 3 and store back
- `xas |= 3` → bitwise OR with 3 and store back
- `xas ^= 3` → bitwise XOR with 3 and store back
- `xas >>= 3` → right shift bits by 3 and store back
- `xas <<= 3` → left shift bits by 3 and store back
- Final `print()` → spacing

---

## 4️⃣ Menu Program: Compare Two Numbers (If/Else)

### ✅ Full Program

```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("----------------------------")
print("| 1 : Check if equal       |")
print("| 2 : Greater or lesser    |")
print("----------------------------")
print()

option = int(input("Enter your option: "))

if option == 1:
    if num1 == num2:
        print(f"{num1} equals {num2}")
    else:
        print(f"{num1} does not equal {num2}")
elif option == 2:
    if num1 > num2:
        print(f"{num1} is greater")
    else:
        print(f"{num2} is greater")
```

### Explanation (line-by-line)
- `num1 = int(input(...))` asks the user for a number and converts it to an integer.
- `num2 = int(input(...))` asks for another number and converts it to an integer.
- The `print("-----")` lines display a simple menu.
- `option = int(input(...))` asks the user to choose menu option 1 or 2.

**Option 1: Check equality**
- `if option == 1:` runs this block when the user selects 1.
- `if num1 == num2:` checks if both numbers are the same.
- If equal → prints "`num1 equals num2`"
- Else → prints "`num1 does not equal num2`"

**Option 2: Compare greater**
- `elif option == 2:` runs when the user selects 2.
- `if num1 > num2:` checks if `num1` is bigger.
- If true → prints "`num1 is greater`"
- Else → prints "`num2 is greater`" (this includes the equal case too)

---

## ✅ Suggested Improvements (Optional)
If you want the program to handle **invalid option** (like 3, 4, etc.), add:

```python
else:
    print("Invalid option. Please choose 1 or 2.")
```

---

✅ **End of Day 5 – Booleans, Operators & If/Else**
