### ✅ Common falsy (null-like) values in Python:

* `None`
* `0`
* `0.0`
* `""` (empty string)
* `[]` (empty list)
* `{}` (empty dictionary)
* `set()`

---

## 🔹 Example 1: Using `None`

```python
value = None
default = "Python"

print(value or default)
```

👉 Output:

```
Python
```

**Why?** → `None` is False → so `or` returns `"Python"`

---

## 🔹 Example 2: With numbers

```python
a = 0
b = 100

print(a or b)
```

👉 Output:

```
100
```

**Why?** → `0` is False → returns `b`

---

## 🔹 Example 3: Empty string

```python
name = ""
fallback = "Guest"

print(name or fallback)
```

👉 Output:

```
Guest
```

---

## 🔹 Example 4: Empty list

```python
lst = []
default_lst = [1, 2, 3]

print(lst or default_lst)
```

👉 Output:

```
[1, 2, 3]
```

---

## 🔹 Example 5: Multiple OR conditions

```python
print(None or 0 or "" or "Hello")
```

👉 Output:


Hello


### 🔍 Rule of `or`:

# * It returns the **first TRUE value**
# * If all are False → returns the **last value**



## 🔥 Important Concept:

print(0 or None or False)


Output:

False

