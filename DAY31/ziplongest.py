from itertools import zip_longest
l1=[1,2,3,4]
l2=[11,22,33]
l3=[111,222,333,444]

for i in zip_longest(l1,l2,l3):
    print(i)

# output:
# (1, 11, 111)
# (2, 22, 222)
# (3, 33, 333)
# (4, None, 444)

for i,j,k in zip_longest(l1,l2,l3):
    print(i,j,k)

# output:
# 1 11 111
# 2 22 222
# 3 33 333
# 4 None 444


for i,j,k in zip_longest(l1,l2,l3,fillvalue='  '):
    print(i,j,k)


# output:
# 1 11 111
# 2 22 222
# 3 33 333
# 4    444

s='abcd'
lst=['app','bat','cat']
dict={}
for i,j in zip_longest(s,lst,fillvalue='NOT PRESENT'):
    dict[i]=j

print(dict)


# output:
# {'a': 'app', 'b': 'bat', 'c': 'cat', 'd': 'NOT PRESENT'}


s='abcd'
lst=[11,22,33,44]

for i,(j,k) in enumerate(zip_longest(s,lst)):
    print(i,j,k)


#output:
# 0 a 11
# 1 b 22
# 2 c 33
# 3 d 44