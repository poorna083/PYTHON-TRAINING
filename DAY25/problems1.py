# 1. find the second largest element
# lst=[5,4,3,2,5,6,7,9,13,24,54,32]

# lst.sort()
# print(lst[-2])

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] < lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp

# print(lst[1])

# 2. reverse an array
# lst=[5,4,3,2,5,6,7,9,13,24,54,32]
# res = []
# for i in range(len(lst)-1,-1,-1):
#     res.append(lst[i])

# print(res)



# 3. find the duplicate elements
# lst = [5,4,3,2,5,6,7,2,4,9,13,24,54,32]

# lst1 = []
# visited = []

# for i in lst:
#     if i not in visited:
#         count = 0
#         for j in lst:
#             if i == j:
#                 count += 1
#         if count > 1:
#             lst1.append(i)
#         visited.append(i)

# print(lst1)


        


# 4. maximum subarray sum

    



# # 5. move zeros to End
lst = [5,4,0,2,5,0,7,9,13,24,54,32]
lst1 = []

for i in lst:
    if i != 0:
        lst1.append(i)

for i in lst:
    if i == 0:
        lst1.append(i)

print(lst1)


# # 6. roate array
# lst=[5,4,3,2,5,6,7,9,13,24,54,32]


# 7. two sum
# lst=[5,4,3,2,5,6,7,9,13,24,54,32]
# res = []
# target = int(input("Enter the target  :"))
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             res.append([lst[i],lst[j]])

# print(res)