## 🔹 Identity Operators in Python


## ✅ Types of Identity Operators

| Operator | Meaning                                            |
| -------- | -------------------------------------------------- |
| `is`     | True if both variables are the **same object**     |
| `is not` | True if both variables are **not the same object** |

---

## 🔹 Example 1: Same Object

```python
a = [1, 2, 3]
b = a

print(a is b)      # True
print(a is not b)  # False
```

### 🔍 Explanation:

* `b = a` → both point to the **same list in memory**

---

## 🔹 Example 2: Different Objects (same value)

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)   # False
print(a == b)   # True
```

### 🔍 Important:

* `==` → compares **values**
* `is` → compares **memory (identity)**

---

## 🔹 Example 3: With Numbers

```python
x = 10
y = 10

print(x is y)  # True
```

👉 Sometimes Python stores small integers in the same memory (optimization), so result is True.

---

## 🔹 Example 4: Using `is not`

```python
x = [1]
y = [1]

print(x is not y)  # True
```

---

## 🔥 Key Difference

| Operator | Checks                  |
| -------- | ----------------------- |
| `==`     | Values are equal        |
| `is`     | Memory location is same |

---

## 🔹 Tricky Example

```python
a = None
b = None

print(a is b)  # True
```

👉 `None` is a **singleton object**, so always same memory.

---

## ⚡ Easy Rule to Remember:

* Use **`==`** → when comparing values
* Use **`is`** → when checking identity (same object)

