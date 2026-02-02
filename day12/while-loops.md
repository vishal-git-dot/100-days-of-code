# 🔁 Day 12 – Python While Loops (100 Days of Code)

This markdown file covers basic usage of `while` loops in Python, including control flow with `break` and `continue` statements.

---

## 🔹 Basic While Loop

```python
i = 0
while i <= 5:
    print(i)
    i = i + 1
```

- Starts at `i = 0`, runs as long as `i <= 5`.
- Prints `i` and increments it by 1 in each loop.

---

## 🔹 While Loop with `break`

```python
x = 0
while x <= 10:
    print(x)
    if x == 3:
        break
    x = x + 1
```

- Prints numbers from 0 to 3.
- When `x` becomes 3, `break` exits the loop.
- Note: `x = x + 1` must be **outside** the `if` block or it will be skipped.

---

## 🔹 While Loop with `continue`

```python
y = 0
while y <= 10:
    print(y)
    if y == 3:
        continue
    y = y + 1
```

⚠️ **Bug Warning**: This loop will become infinite when `y == 3` because `continue` skips `y = y + 1`. To fix it:

```python
y = 0
while y <= 10:
    if y == 3:
        y += 1
        continue
    print(y)
    y += 1
```

- `continue` skips printing for `y = 3` and continues to next loop iteration.
- Corrected version ensures the increment isn't skipped.

---

✅ **End of Day 12 – While Loops**
