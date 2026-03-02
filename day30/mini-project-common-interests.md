# Day 30 – Mini Project
## 🎯 Common Interests Finder

---

## 📌 Project Description

This mini project takes input from two users and compares their favorite items.

The program:
- Accepts comma-separated input from both users
- Converts the input into sets
- Performs set operations to compare results
- Displays:
  - All combined items (Union)
  - Common items (Intersection)
  - Items unique to each person (Difference)
  - Items not common to both (Symmetric Difference)

This project combines:
- User input
- Functions
- Sets
- Data cleaning using strip()
- Set operations

---

## ✅ Python Code

```python
# Day 30 – Mini Project: Common Interests Finder

def get_items(person):
    items = input(f"Enter items for {person} (comma separated): ")
    item_set = set(item.strip() for item in items.split(","))
    return item_set


def show_results(set1, set2):
    print("\nAll Items (Union):", set1.union(set2))
    print("Common Items (Intersection):", set1.intersection(set2))
    print("Only in Person 1:", set1.difference(set2))
    print("Only in Person 2:", set2.difference(set1))
    print("Not Common (Symmetric Difference):", set1.symmetric_difference(set2))


# Main Program
person1 = get_items("Person 1")
person2 = get_items("Person 2")

show_results(person1, person2)
```

---

## 🧪 Example Run

Example input:

Person 1:
apple, banana, mango

Person 2:
banana, orange, mango

Example output:

All Items (Union):
{'apple', 'banana', 'mango', 'orange'}

Common Items (Intersection):
{'banana', 'mango'}

Only in Person 1:
{'apple'}

Only in Person 2:
{'orange'}

Not Common (Symmetric Difference):
{'apple', 'orange'}

---

## 🎯 Learning Outcome

After completing this project, you understand:

- How to take structured user input
- How to convert strings into sets
- How to apply union, intersection, difference
- How to structure small programs using functions
- How to combine multiple Python concepts into one mini project

---

## 📂 File Info

Day 30 mini project documentation file.
