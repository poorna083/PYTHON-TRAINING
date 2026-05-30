# generator:
#     a grnrrator is a special type of function which is used to return one value
# at a Time

# generator is also known as lazy iterator

# we can access the values of generators in three types:
# 1) next
# 2) Typecasting
# 3) for Loop
# -------------------------------------------------------------------------------------
# def sample():
#     for i in range(3):
#         yield i

# s=sample()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# output:
# 0
# 1
# 2
# Traceback (most recent call last):
#   File "c:\QSP_TRAINING\PYTHON-TRAINING\DAY36\generators.py", line 20, in <module>
#     print(next(s))
#           ~~~~^^^
# StopIteration
# -------------------------------------------------------------------------------------------
# def sample():
#     for i in range(5):
#         yield i
# s=sample()
# for i in s:
#     print(i)

# output:
# 0
# 1
# 2
# 3
# 4

# --------------------------------------------------------------------------------------------
def sample():
    for i in range(5):
        yield i

s=sample()
print(list(s))

# output:
# [0, 1, 2, 3, 4]