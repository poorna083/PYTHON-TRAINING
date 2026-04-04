## 🔗 Logical `and` Operator

# 👉 `and` returns:

# * **First falsy value**, OR
# * **Last value if all are true**


## ⚠️ Default Falsy Values in Python

# These are treated as **False**:

0        # int
0.0      # float
''       # empty string
[]       # empty list
{}       # empty dict
None     # none type
False    # boolean

## 📝 Examples of `and` with Default Values

### 🔹 Example 1: Integer


x = 0 and 5
print(x)   # 0

### 🔹 Example 2: String

x = '' and 'Hello'
print(x)   # ''


### 🔹 Example 3: List

x = [] and [1, 2, 3]
print(x)   # []


### 🔹 Example 4: All True Values


x = 10 and 20
print(x)   # 20


### 🔹 Example 5: Mixed Values


x = 5 and 0 and 10
print(x)   # 0




### 🔹 Example 6: None


x = None and 100
print(x)   # None


### 🔹 Example 7: Boolean


x = True and False
print(x)   # False


## 🎯 Key Concept (Very Important)

# a and b
# ```

# * If `a` is False → return `a`
# * If `a` is True → return `b`



##  Bonus Trick (Interview Level)

print(5 and 10 and 15)   # 15
print(5 and 0 and 15)    # 0

