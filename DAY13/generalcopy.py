# general copy:
#    it is the process of copying from one variable to another variable with the help of 
#    equal to operator
   
#    in general copy both main frame and nested frame of all the variables will be same

lst=[1,2,[3,4]]
print(id(lst))

res = lst

print(id(res))

lst[1]=22

print(lst)
print(res)

res[2][0]=33

print(res)
print(lst)


# output:
# 2149835272064
# 2149835272064
# [1, 22, [3, 4]]
# [1, 22, [3, 4]]
# [1, 22, [33, 4]]
# [1, 22, [33, 4]]
