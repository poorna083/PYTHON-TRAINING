## 🔹 1. Bitwise AND (`&`)

* Compares each bit → returns **1 if both bits are 1**

```
a = 5   # 0101
b = 3   # 0011

print(a & b)  # 0001 → 1
```

👉 Result: **1**

---

## 🔹 2. Bitwise OR (`|`)

* Returns **1 if at least one bit is 1**

```
a = 5   # 0101
b = 3   # 0011

print(a | b)  # 0111 → 7
```

👉 Result: **7**

---

## 🔹 3. Bitwise XOR (`^`)

* Returns **1 if bits are different**

```
a = 5   # 0101
b = 3   # 0011

print(a ^ b)  # 0110 → 6
```

👉 Result: **6**

---

## 🔹 4. Bitwise NOT (`~`)

* Flips all bits (1 → 0, 0 → 1)

```
a = 5   # 00000101

print(~a)  # -6
```

👉 Result: **-6**
⚠️ Python uses **2’s complement**, so result becomes negative.

---

## 🔹 5. Left Shift (`<<`)

* Shifts bits to left → multiplies by 2

```
a = 5   # 0101

print(a << 1)  # 1010 → 10
```

👉 Result: **10**

---

## 🔹 6. Right Shift (`>>`)

* Shifts bits to right → divides by 2

```
a = 5   # 0101

print(a >> 1)  # 0010 → 2
```

👉 Result: **2**

---

## 🔥 Quick Summary Table

| Operator    | Symbol | Meaning             | Example Result |              |
| ----------- | ------ | ------------------- | -------------- | ------------ |
| AND         | `&`    | Both bits must be 1 | `5 & 3 = 1`    |              |
| OR          | `      | `                   | Any bit is 1   | `5 \| 3 = 7` |
| XOR         | `^`    | Bits different      | `5 ^ 3 = 6`    |              |
| NOT         | `~`    | Reverse bits        | `~5 = -6`      |              |
| Left Shift  | `<<`   | Multiply by 2       | `5 << 1 = 10`  |              |
| Right Shift | `>>`   | Divide by 2         | `5 >> 1 = 2`   |              |


