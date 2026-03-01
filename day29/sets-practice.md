# Day 29 – Sets in Python

## 📌 Exercise Objectives

1. Create a set X with items: Rose, Orchid, Dalia, Daisy, Lilly, Jasmine, Lotus  
2. Create a set Y with items: Apple, Banana, Orange, Rose, Lotus  
3. Access both sets using a for loop  
4. Add ‘sunflower’ to set Y  
5. Remove ‘sunflower’ from set Y  
6. Join all items from both sets  
7. Return:
   - Items present in both sets  
   - Items not present in both sets  
8. Return items only in set X (not in Y)  
9. Return items in both set X and set Y  
10. Return items not present in both sets  

---

## ✅ Code

```python
# Day 29 – Sets Practice

X = {"Rose","Orchid","Dalia","Daisy","Lilly","Jasmine","Lotus"}
Y = {"Apple","Banana","Orange","Rose","Lotus"}

# 3️⃣ Access sets using for loop
print("Items in X:")
for x in X:
    print(x)

print("\nItems in Y:")
for y in Y:
    print(y)

# 4️⃣ Add sunflower
Y.add("sunflower")
print("\nAfter adding sunflower:", Y)

# 5️⃣ Remove sunflower
Y.remove("sunflower")
print("After removing sunflower:", Y)

# 6️⃣ Union (join both sets)
print("\nUnion:", X.union(Y))

# 7️⃣ 1) Present in both sets (Intersection)
print("Intersection:", X.intersection(Y))

# 7️⃣ 2) Not present in both sets (Symmetric Difference)
print("Symmetric Difference:", X.symmetric_difference(Y))

# 8️⃣ Only in X not in Y (Difference)
print("Only in X:", X.difference(Y))
