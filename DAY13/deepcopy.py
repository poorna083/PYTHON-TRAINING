# Deep copy:
#    it is the process of copying the data from one variable to another with the help of deep copy method
#    in deep copy main frame and nested frame of all variables will be different 

from copy import deepcopy
lst=[1,2,[3,4]]

res = deepcopy(lst)

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

res[2][1]=44
print(lst)
print(res)


# output:
# 2815468549760
# 2815471688064
# 2815468433280
# 2815471696768
# [11, 2, [3, 4]]
# [1, 2, [3, 4]]
# [11, 2, [3, 4]]
# [1, 2, [33, 4]]
# [11, 2, [3, 4]]
# [1, 2, [33, 44]]