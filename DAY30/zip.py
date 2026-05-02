l1=[1,2,3,4]
l2=[5,6,7,8]

for i in zip(l1,l2):
    print(i)

# (1, 5)
# (2, 6)
# (3, 7)
# (4, 8)
# -------------------------------------------------------------------------
for i,j in zip(l1,l2):
    print(i,j)


# output:
# 1 5
# 2 6
# 3 7
# 4 8
# -----------------------------------------------------------------------------------
# WAP TO CREATE A LIST AND PRODUCTING TWO LISTS
l1=[1,2,3,4]
l2=[5,6,7,8]
lst=[]
for i,j in zip(l1,l2):
    lst.append(i*j)

print(lst)


# output:
# [5, 12, 21, 32]
# ------------------------------------------------------------------------------------------
s1='abcd'
s2=['apple','bat','cat','dog']
# output:
# {'a': 'apple', 'b': 'bat', 'c': 'cat', 'd': 'dog'}



dict={}
for i,j in zip(s1,s2):
    dict[i]=j

print(dict)


# output:
# {'a': 'apple', 'b': 'bat', 'c': 'cat', 'd': 'dog'}


# ------------------------------------------------------------------------------------

l1=['a','b','c']
l2=[1,2,3]
l3=[4,5,6]

# output:
# {'a': 5, 'b': 7, 'c': 9}

dict={}
for i,j,k in zip(l1,l2,l3):
    dict[i]=j+k

print(dict)