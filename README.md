# 100-days-of-code
My 100 Days of Code challenge — daily log and code.


### Day 1: 18 January 2026
- Today I created the repository for my 100 Days of Code challenge.
- Wrote my first simple program (Hello World).
- Learned how to push changes to GitHub.


### Day 2: Python Basics

**What I did:**
- Learned basic Python syntax
- Practiced `print()` statements
- Worked with variables and data types
- Performed arithmetic operations
- Learned type casting (`str`, `int`, `float`)
- Explored lists and unpacking
- Understood local vs global variables

**Files added:**
- `day02/python-intro.md`

**Key Learnings:**
- Python is dynamically typed
- Variables can be reassigned to different data types
- Lists can be unpacked into multiple variables
- Local variables inside functions do not affect global variables


### Day 3 – Python Basics & Data Types

**What I did:**
- Learned basic Python syntax and printing
- Practiced variables and dynamic typing
- Performed arithmetic operations
- Explored Python built-in data types
- Learned about type casting and type checking
- Practiced functions to demonstrate each data type

**File added:**
- `day03/python-data-types.md`

**Key Learnings:**
- Python supports many built-in data types (int, float, str, list, tuple, dict, set, etc.)
- Variables can change type during runtime
- Each data type has specific use cases
- Functions help organize and test different data types
- `type()` is used to identify variable data types


### Day 4 – Python Numbers & Strings

**What I did:**
- Learned Python numeric data types (int, float, complex)
- Worked with scientific notation numbers
- Practiced type conversion between numbers
- Generated random numbers using the `random` module
- Learned Python string basics
- Practiced string indexing, looping, and slicing
- Used common string methods (`upper`, `lower`, `strip`, `replace`, `split`)
- Learned string concatenation and f-strings
- Explored escape characters in strings

**Files added:**
- `day04/python-numbers-random.md`
- `day04/python-strings.md`

**Key Learnings:**
- Python supports multiple numeric types with flexible conversion
- Scientific notation values are treated as floats
- The `random` module helps generate random numbers
- Strings are iterable and support slicing
- String methods simplify text manipulation
- f-strings provide a clean way to format strings


### Day 5 – Python Booleans, Operators & Conditional Statements

**What I did:**
- Learned how Python evaluates truthy and falsy values
- Practiced Boolean expressions using `bool()`
- Worked with arithmetic operators (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
- Practiced assignment operators (`+=`, `-=`, `*=`, `/=`, etc.)
- Learned bitwise assignment operators
- Built a menu-driven program using `if`, `elif`, and `else`
- Compared numbers using equality and greater/lesser conditions

**Files added:**
- `day05/booleans-operators-ifelse.md`

**Key Learnings:**
- Non-empty values evaluate to `True`, empty values evaluate to `False`
- Python supports multiple operator categories
- Assignment operators modify variables in place
- Conditional statements control program flow
- User input can be combined with logic to build interactive programs


### Day 6 – Python Operators

**What I did:**
- Learned comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Practiced logical operators (`and`, `or`, `not`)
- Understood identity operators (`is`, `is not`)
- Worked with bitwise operators (`&`, `|`, `^`, `~`)
- Used membership operators (`in`, `not in`)
- Built a small interactive program to check list membership using user input

**Files added:**
- `day06/python-operators.md`

**Key Learnings:**
- Comparison operators return Boolean values
- Logical operators combine multiple conditions
- Identity operators compare memory references, not values
- Bitwise operators work at the binary level
- Membership operators help check existence in collections


### Day 7 – Python Lists & Loops

**What I did:**
- Learned list operations and methods such as `append`, `remove`, `insert`, and `clear`
- Practiced list slicing and indexing
- Explored looping techniques with `for`, `while`, and list comprehensions
- Built interactive programs that filter and modify lists based on conditions
- Learned how to join and copy lists
- Sorted and reversed lists using built-in methods

**Files added:**
- `day07/python-lists-loops.md`

**Key Learnings:**
- Lists are versatile and support various operations for adding, removing, and modifying elements
- Looping through lists with `for`, `while`, and list comprehension simplifies iteration and modification
- List comprehension allows easy filtering and transformation of data
- Lists can be joined using `+` or `extend()`
- `sort()` and `reverse()` allow efficient sorting and reversing of list items


### Day 8 – Python List Exercises

**What I did:**
- Practiced real-world problems using lists
- Revisited list operations like `append`, `insert`, `extend`, `pop`, and `sort`
- Explored negative indexing and slicing techniques
- Solved exercises involving even/odd filtering, sum, and list reversal
- Implemented list algorithms like finding length manually, copying, and doubling lists

**Files added:**
- `day08/list-exercises.md`

**Key Learnings:**
- List operations become intuitive through repeated practice
- List slicing and negative indexes are powerful tools for data access
- Built logic for detecting even/odd numbers and calculating sum and length without built-ins
- Enhanced understanding of data manipulation by solving real-world style tasks


### Day 9 – Python Tuples

**What I did:**
- Learned what tuples are and how they are immutable
- Created tuples using `()` and the `tuple()` constructor
- Practiced accessing elements using indexing and slicing
- Used tuple unpacking with and without the asterisk `*`
- Learned how to loop through tuples using `for`, `while`, and `range()`
- Explored tuple operations like join, multiply, count, and index

**Files added:**
- `day09/python-tuples.md`

**Key Learnings:**
- Tuples are like lists but immutable, making them suitable for fixed data
- Single-element tuples require a trailing comma (e.g., `("hello",)`)
- Tuple unpacking is useful for variable assignment
- Looping and accessing items work just like lists
- Tuples support basic operations like concatenation, repetition, and indexing


### Day 10 – Python Sets

**What I did:**
- Explored the creation and usage of sets in Python
- Learned the difference between `set()` constructor and literal `{}` syntax
- Used methods like `add()`, `remove()`, `discard()`, and `pop()`
- Accessed set elements via loops and membership tests
- Updated sets with `update()` method
- Performed common set operations: union, intersection, difference, and intersection_update

**Files added:**
- `day10/python-sets.md`

**Key Learnings:**
- Sets are unordered collections with no duplicates
- Methods like `union()` and `intersection()` make set comparisons powerful
- Updating and modifying sets is intuitive but unordered
- Perfect for membership tests and data uniqueness


### Day 11 – Python Dictionaries

**What I did:**
- Created and printed dictionaries with multiple data types (including lists)
- Used the `dict()` constructor for cleaner syntax
- Accessed dictionary elements using `[]`, `.get()`, `.keys()`, `.values()`, `.items()`
- Modified values and saw dynamic views in `.values()`
- Checked for the existence of keys using `in`
- Learned dictionary updating and value overriding techniques

**Files added:**
- `day11/python-dictionaries.md`

**Key Learnings:**
- Dictionaries are key-value pairs with fast lookups
- `dict.values()` returns a live view that updates with changes
- `.update()` allows mass updating of dictionary values


### Day 12 – Python While Loops

**What I did:**
- Practiced while loops with `break` and `continue`
- Learned how incorrect `continue` usage can create infinite loops
- Demonstrated how to safely increment inside loops

**Files added:**
- `day12/while-loops.md`

**Key Learnings:**
- `while` loops run based on a condition rather than a counter
- `break` exits a loop when a condition is met
- `continue` skips the rest of the loop body for that iteration
- Proper increment placement is critical to avoid infinite loops


### Day 13 – Python Functions, Parameters & Scope

**What I did:**
- Defined and called basic functions
- Used parameters, return values, and default arguments
- Handled `*args` and `**kwargs`
- Practiced keyword arguments and dictionary unpacking
- Explored variable scopes and the use of `global`

**Files added:**
- `day13/functions-arguments-scope.md`

**Key Learnings:**
- Functions make code reusable and organized
- `*args` collects multiple positional arguments into a tuple
- `**kwargs` collects keyword arguments into a dictionary
- Scope management helps avoid accidental variable overwrites


### Day 14 – Arrays (Lists) and DateTime

**What I did:**
- Practiced using Python lists (arrays)
- Accessed, updated, added, and removed list elements
- Used loops to iterate through lists
- Worked with the `datetime` module
- Formatted date and time using `strftime()`

**Files added:**
- `day14/arrays-and-datetime.md`

**Key learnings:**
- Python lists are mutable and index-based
- `append()` and `remove()` modify lists dynamically
- `datetime.now()` gives current system date & time
- `strftime()` converts date/time into readable formats


### Day 15 – Python Modules and Platform

**What I did:**
- Imported built-in Python modules
- Imported variables from a custom module
- Used the `platform` module to detect the operating system
- Accessed dictionary data from another Python file

**Files added:**
- `day15/modules-and-platform.md`

**Key learnings:**
- Python supports built-in and user-defined modules
- `from module import item` imports specific objects
- `platform.system()` returns OS information
- Modules help keep code clean and reusable


### Day 16 – Regular Expressions (re)

**What I did:**
- Practiced regex pattern matching using Python’s `re` module
- Used `findall()` to match letters, digits, and patterns with wildcards
- Checked string start/end using anchors like `^`, `\A`, and `\Z`
- Practiced quantifiers (`*`, `+`, `?`, `{2}`) to control matching
- Used special sequences like `\d`, `\D`, `\s`, `\S`, `\w`, `\W`
- Split text using `re.split()`

**Files added:**
- `day16/regex-basics.md`

**Key learnings:**
- Regex helps search and validate text using patterns
- `findall()` returns all matches in a list
- Anchors check positions (start/end of string)
- Quantifiers control how much text a pattern matches


### Day 17 – Classes and Objects (OOP)

**What I did:**
- Created simple classes and objects
- Used class variables and instance variables
- Implemented constructors using `__init__()`
- Created methods and called methods inside other methods
- Built small real-world examples like calculator and movie manager

**Files added:**
- `day17/classes-and-objects.md`

**Key learnings:**
- Classes act as blueprints for objects
- Objects store data and behavior together
- `self` refers to the current object
- Methods define what an object can do
- OOP makes programs more structured and reusable


### Day 18 – Inheritance (OOP)

**What I did:**
- Practiced inheritance using parent and child classes
- Created a `Student` class that inherits from `Person`
- Added child-only methods and tested calling them safely using `try/except`
- Built a `Book` and `Publisher` example to understand inherited attributes + extra child methods

**Files added:**
- `day18/inheritance-basics.md`

**Key learnings:**
- Child classes inherit attributes and methods from parent classes
- `pass` creates an empty subclass that still inherits everything
- Parent objects cannot call child-only methods
- Child classes can add new methods and reuse parent methods
- `super().__init__()` is the preferred way to call the parent constructor


### Day 19 – Polymorphism

**What I did:**
- Practiced polymorphism using multiple classes with the same method name
- Created different classes representing life stages
- Called the same method (`teeth()`) on different objects
- Used a loop to treat objects uniformly

**Files added:**
- `day19/polymorphism-basics.md`

**Key learnings:**
- Polymorphism allows the same method name with different behavior
- Python supports polymorphism through duck typing
- Objects don’t need inheritance to behave polymorphically
- Method execution depends on the object type


### Day 20 – Exception Handling

**What I did:**
- Practiced using `try`, `except`, `else`, and `finally`
- Handled `ValueError` during user input conversion
- Learned how and when to raise custom exceptions
- Understood why `input()` always returns a string

**Files added:**
- `day20/exception-handling.md`

**Key learnings:**
- Exception handling prevents program crashes
- `else` runs only if no exception occurs
- `finally` always executes
- `raise` is used for custom error handling
- User input must be converted before validation


### Day 21 – File Handling

**What I did:**
- Read text files using `read()` and `readline()`
- Appended new content to files using append mode
- Handled missing files safely using `try/except`
- Learned why files must exist before opening in read mode
- Read specific numbers of characters from a file

**Files added:**
- `day21/file-handling.md`

**Key learnings:**
- `"r"` mode fails if the file does not exist
- Use `try/except FileNotFoundError` for file checks
- `"a"` mode adds content without deleting old data
- `read(n)` reads limited characters
- Always close files after use


### Day 22 – Multiple Class Practice

**What I did:**
- Created multiple independent classes (Person, Car, Book)
- Built calculation classes for circle and rectangle areas
- Practiced constructors and instance variables
- Called methods from different objects

**Files added:**
- `day22/multiple-classes-practice.md`

**Key learnings:**
- Classes organize related data and behavior
- `self` stores object-specific values
- Methods can either print or return values
- Naming conventions (PascalCase) improve code quality
- Calculation classes should return values instead of printing


### Day 23 – Dictionary Practice

**What I did:**
- Created a student dictionary with multiple keys and values
- Iterated through dictionary items using `.items()`
- Checked dictionary length using `len()`
- Retrieved specific values and checked their data types
- Modified list values inside a dictionary
- Used `.keys()` and `.values()`
- Removed items using `.pop()`
- Copied a dictionary and modified the copy

**Files added:**
- `day23/dictionary-practice.md`

**Key learnings:**
- Dictionaries store structured data using key–value pairs
- `.items()`, `.keys()`, and `.values()` are essential methods
- Lists inside dictionaries can be modified
- `.copy()` creates a shallow copy
- `.pop()` removes keys safely


### Day 24 – Clearing Lists in Python

**What I did:**
- Used `.clear()` to empty a list
- Cleared a list using `pop()` in a loop
- Removed elements using `remove()` with slicing
- Learned alternative methods like `del` and reassignment

**Files added:**
- `day24/clear-list-methods.md`

**Key learnings:**
- `.clear()` is the cleanest and most efficient way
- `pop()` and `remove()` loops are slower
- `mylist = []` creates a new list object
- `del mylist[:]` removes all elements using slicing


### Day 25 – Finding Largest Number (With Dry Run)

**What I did:**
- Found the largest number in a list without using `max()`
- Used a loop with comparison logic
- Practiced dry run step-by-step tracing
- Learned about time complexity O(n)

**Files added:**
- `day25/find-largest-dry-run.md`

**Key learnings:**
- Initialize with the first element
- Compare each value and update conditionally
- Dry run improves debugging and interview skills
- Manual logic helps understand built-in functions


### Day 26 – Find Maximum Number (Dry Run)

**What I did:**
- Found the maximum value in a list manually
- Used comparison inside a loop
- Practiced step-by-step dry run tracing
- Reinforced understanding of O(n) time complexity

**Files added:**
- `day26/find-max-dry-run.md`

**Key learnings:**
- Initialize with first element
- Update when a larger value is found
- Dry run improves debugging
- Manual approach builds strong algorithm foundation


### Day 27 – HTML Form with PHP & MySQL

**What I built:**
- HTML Signup Form
- PHP Backend Script
- MySQL Database Connection
- Insert Data into Database

**Concepts practiced:**
- POST method
- $_REQUEST
- mysqli_connect()
- SQL INSERT query
- Basic backend workflow

**Files added:**
- index.html (Frontend form)
- insert.php (Backend logic)
- README.md (Documentation)


### Day 28 – Python Functions & Lambda

**Concepts practiced:**
- User-defined functions
- Lambda expressions
- Closures
- filter()
- String manipulation
- Reversing sequences

**File added:**
- day28/functions-lambda.md


### Day 29 – Sets in Python

**Concepts practiced:**
- Creating sets
- Looping through sets
- add() and remove()
- union()
- intersection()
- difference()
- symmetric_difference()

**File added:**
- day29/sets-practice.md

**Key learning:**
Sets are unordered collections of unique elements and are useful for comparison operations.
