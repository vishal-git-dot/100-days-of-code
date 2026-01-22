# 🐍 Python Data Types – Day 3 (100 Days of Code)

This document demonstrates all major built-in Python data types using simple functions.
Each section includes clear explanations for beginners.

---

## Integer (Number Type)

```python
def numbertype():
    x = 1
    print(x, type(x))
```

- `x = 1` assigns an integer value.
- `type(x)` shows that `x` is of type `int`.

---

## String (Text Type)

```python
def texttype():
    x = "Hello"
    print(x, type(x))
```

- Strings store text.
- `x` is of type `str`.

---

## Float

```python
def floattype():
    x = 3.79
    print(x, type(x))
```

- Floats store decimal numbers.
- Type is `float`.

---

## Complex

```python
def comtype():
    x = 1j
    print(x, type(x))
```

- Complex numbers use `j`.
- Type is `complex`.

---

## List

```python
def listtype():
    x = [1, 2, 'apple']
    print(x, type(x))
```

- Lists are ordered and mutable.
- Can store multiple data types.

---

## Tuple

```python
def tupletype():
    x = (1, 2, 'apple')
    print(x, type(x))
```

- Tuples are ordered but immutable.

---

## Range

```python
def rangetype():
    x = range(1)
    print(x, type(x))
```

- Range generates number sequences.

---

## Dictionary

```python
def dicttype():
    x = {'name': 'arun', 'age': 18}
    print(x, type(x))
```

- Stores key-value pairs.

---

## Set

```python
def settype():
    x = {'apple', 'banana', 'lemon'}
    print(x, type(x))
```

- Stores unique values.

---

## Frozen Set

```python
def frozentype():
    x = frozenset({'apple', 'banana', 'lemon'})
    print(x, type(x))
```

- Immutable set.

---

## Boolean

```python
def booltype():
    x = True
    print(x, type(x))
```

- Boolean values are True/False.

---

## Bytes

```python
def bytetype():
    x = b'apple'
    print(x, type(x))
```

- Stores binary data.

---

## Bytearray

```python
def bytearraytype():
    x = bytearray(6)
    print(x, type(x))
```

- Mutable version of bytes.

---

## Memory View

```python
def memortytype():
    x = memoryview(bytes(4))
    print(x, type(x))
```

- Access memory without copying.

---

## None Type

```python
def nonetype():
    x = None
    print(x, type(x))
```

- Represents no value.

---

## Function Calls

```python
numbertype()
texttype()
floattype()
comtype()
listtype()
tupletype()
rangetype()
dicttype()
settype()
frozentype()
booltype()
bytetype()
bytearraytype()
memortytype()
nonetype()
```

---

✅ End of Day 3 – Python Data Types
