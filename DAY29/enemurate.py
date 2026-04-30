# s=['apple','mango','orange','grapes']
# for i in enumerate(s):
#     print(i)

# output:
# (0, 'apple')
# (1, 'mango')
# (2, 'orange')
# (3, 'grapes')

# ----------------------------------------------------------------------------------
# s=['apple','mango','orange','grapes']
# for i,j in enumerate(s):
#     print(f'{i}-->{j}')

# output:
# 0-->apple
# 1-->mango
# 2-->orange
# 3-->grapes

# --------------------------------------------------------------------------------------
# str='apple'
# lst=[]
# for i,j in enumerate(str):
#     lst.append((i,j))

# print(lst)

# output:
# [(0, 'a'), (1, 'p'), (2, 'p'), (3, 'l'), (4, 'e')]


# ----------------------------------------------------------------------------------------
lst=['apple','bat','cat','dogs','road']
# dict={}
# for i,j in enumerate(lst):
#     if i%2 == 0:
#         dict[i]=j
#     else:
#         dict[j]=len(j)

# print(dict)

# output:
# {0: 'apple', 'bat': 3, 2: 'cat', 'dogs': 4, 4: 'road'}

                                            
                                    
                                            # or


# dict={}
# for i,j in enumerate(lst):
#     if i%2==0:
#         dict[i]=j
#     elif i%2==1:
#         for k in lst:
#             count=0
#             for l in k:
#                 count+=1
#                 dict[j]=count

# print(dict)


# output:
# {0: 'apple', 'bat': 3, 2: 'cat', 'dogs': 4, 4: 'road'}

# ----------------------------------------------------------------------------------------

lst=['qspiders','orange','app','mango']
lst1=[]

# for i,j in enumerate(lst):
#     lst1.append((i,len(j),j))
# print(lst1)

# output:
# [(0, 8, 'qspiders'), (1, 6, 'orange'), (2, 3, 'app'), (3, 5, 'mango')]


                    # or



for i,j in enumerate(lst):
    count = 0
    for k in j:
        count +=1
    lst1.append((i,count,j))
print(lst1)


# output:
# [(0, 8, 'qspiders'), (1, 6, 'orange'), (2, 3, 'app'), (3, 5, 'mango')]


