# shallow copy:
#    it is the process of copying the data from one variable to another with the help of copy method
#    in shallow copy main frame of all variables will be different but nested frame will be same

from copy import copy
lst=[1,2,[3,4]]

res =copy(lst)

print(id(lst))
print(id(res))

print(id(lst[2]))
print(id(res[2]))

lst[0]=11
print(lst)
print(res)

res[2][0]=33
print(lst)
print(res)


# output:
# 2191975495296
# 2191977650432
# 2191975378816
# 2191975378816
# [11, 2, [3, 4]]
# [1, 2, [3, 4]]
# [11, 2, [33, 4]]
# [1, 2, [33, 4]]