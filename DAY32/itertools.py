from itertools import product

for i in product(range(1,3),repeat=3):
    print(i)
    
# output:
# (1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 2, 2)
# (2, 1, 1)
# (2, 1, 2)
# (2, 2, 1)
# (2, 2, 2)


for i,j,k in product(range(1,3),repeat=3):
    print(i,j,k)

# output:
# 1 1 1
# 1 1 2
# 1 2 1
# 1 2 2
# 2 1 1
# 2 1 2
# 2 2 1
# 2 2 2

from itertools import count

# syntax:
        # count(start_value,stepvalue)


# for i in count(1,1):
#         print(i)
        
# output:
# 1
# 2
# 3
# 4
# 5
# .
# .
# .
# .
# .
# .
# .

from itertools import cycle
# repeat the values n number of times

lst=[1,2,3,4]
for i in cycle(lst):
     print(i)


# output:
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# .
# .
# .
# .
# .

