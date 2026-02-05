# 🧩 Day 13 – Python Functions, Arguments, and Scope (100 Days of Code)

In this session, we cover creating and calling functions, using parameters, `*args`, `**kwargs`, and working with variable scope.

---

## 🔹 Defining and Calling a Basic Function

```python
def my_function():
    print("Hello World")

my_function()
```

- Defines a function called `my_function` and calls it immediately.
- Output: `Hello World`

---

## 🔹 Function with Parameters and Return

```python
def summ(a, b):
    result = f"The sum of {a} and {b} is {a+b}"
    return result

print(summ(1, 2))
```

- Accepts 2 arguments and returns a formatted sum string.

---

## 🔹 Default Arguments

```python
def callme(name="friend"):
    print("Hello " + name)

callme()
callme("John")
callme("Roy")
```

- Uses `"friend"` as default if no argument is passed.

---

## 🔹 Keyword Arguments

```python
def para(animal, name):
    print(f"Animal is {animal}, name is {name}")

para(animal="Dog", name="Bruno")
```

- Allows passing arguments in any order using keys.

---

## 🔹 *args: Variable-Length Positional Arguments

```python
def example(*kids):
    print("Hello " + kids[0])

example("tobi", "simon", "harry")
```

```python
def example2(*kids):
    for k in kids:
        print("Hello " + k)
```

```python
def example3(greet, *kids):
    for i in kids:
        print(f"{greet} : {i}")
```

- `*args` allows passing multiple values that are treated as a tuple.

---

## 🔹 **kwargs: Variable-Length Keyword Arguments

```python
def example4(**fruits):
    for fruit in fruits:
        print(fruits[fruit])

example4(apple="apple", banana="banana")
example4(apple="apple", age=30)
```

- `**kwargs` lets you handle named arguments as a dictionary.

---

## 🔹 Variable Scope

```python
def scopee():
    x = 300
    print(x)

x = 200
scopee()
print(x)
```

- `x` inside `scopee()` is local and does not affect global `x`.

```python
def scopee2():
    global z
    z = 500
    print(z)

scopee2()
print(z)
```

- `global` allows modifying or creating a global variable from inside a function.

---

✅ **End of Day 13 – Functions, Parameters, and Scope**
