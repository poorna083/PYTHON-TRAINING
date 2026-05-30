# filter:
# filter() is a built-in Python function used to extract elements from an iterable based on a condition.
# It examines each element one by one and keeps only those elements for which the given function returns True.

# Syntax:
# filter(function_name,collection)

# ceck if the number is even or odd
lst = eval(input("Enter the list : "))
def even_odd(n):
    return n % 2 == 0
res = list(filter(even_odd, lst))
print(res)

# output:
# Enter the list : [3,2,10,5,9]
# [2, 10]
