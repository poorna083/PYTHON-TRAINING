# reduce:
#*reduce() is used to reduce an iterable to a single value by repeatedly applying a function to its elements.
# *reduce present in the module called function tools
# *reduce we need to pass two arguments mandatory

from functools import reduce
lst=[1,2,3,4]
def demo(x,y):
    return x+y
result=reduce(demo,lst)
print(result)

# output:
# 10