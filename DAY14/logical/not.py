## 🔹 Basic Example

```python
a = True
print(not a)
```

👉 Output:

```
False
```

---

## 🔹 With Conditions

```python
x = 10

if not x > 20:
    print("Condition is True")
```

👉 Output:

```
Condition is True
```

### 🔍 Explanation:

* `x > 20` → False
* `not False` → True

---

## 🔹 With Null (Falsy) Values

### Example 1: `None`

```python
value = None
print(not value)
```

👉 Output:

```
True
```

---

### Example 2: `0`

```python
print(not 0)
```

👉 Output:

```
True
```

---

### Example 3: Empty String

```python
print(not "")
```

👉 Output:

```
True
```

---

### Example 4: Empty List

```python
print(not [])
```

👉 Output:

```
True
```

---

## 🔥 Important Rule:

* `not True` → `False`
* `not False` → `True`
* `not <falsy value>` → `True`
* `not <truthy value>` → `False`

---

## 🔹 Tricky Example

```python
print(not (None or 0 or "Hello"))
```

👉 Output:

```
False
```

### Why?

* `None or 0 or "Hello"` → `"Hello"` (truthy)
* `not "Hello"` → `False`


