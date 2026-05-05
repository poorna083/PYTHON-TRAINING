# lst=[1,2,3,4,5]
# k=3
# output:
# [5,4,3,1,2]

# lst=eval(input("Enter the string :"))
# k = int(input("Enter the shifts "))

# for i in range(k):
#     val=lst.pop()
#     lst.insert(i,val)

# print(lst)


# output:
# Enter the string   :[1,2,3,4,5]
# Enter the shifts   :3
# [5, 4, 3, 1, 2]

# -----------------------------------------------------------------------
# lst=[1,2,3,4,5]
# output:
# [1,4,3,2,5]

# lst=[1,2,3,4,5,6]
# output:
# [1,6,3,4,5,2]

lst = eval(input("Enter the list: "))


odd = []
for i in range(len(lst)):
    if i % 2 != 0:
        odd.append(lst[i])


j = len(odd) - 1

for i in range(len(lst)):
    if i % 2 != 0:
        lst[i] = odd[j]
        j -= 1

print(lst)




