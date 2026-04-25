# s="aaabbbcc"
# output:
# {'a':3,'b':3,'c':2}

# s="aaabbbcc"
# dict = {}
# lst = []
# for i in s:
#     lst.append(i)
# print(lst)

# for i in range(len(lst)):
#     count = 0
#     for j in range (len(lst)):
#         if lst[i]==lst[j]:
#             count+=1
#     dict[lst[i]]=count

# print(dict)
# -------------------------------------------------------------------------------------------------

# lst=["hi","hello","to","good","mango"]
# output = {2:["hi","to"],5:["hello","mango"],4:["good"]}

# lst=["hi","hello","to","good","mango"]
# dict = {}
# for i in lst:
#     count = 0
#     for j in i:
#         count +=1
#     if count not in dict:
#         dict[count] = []

#     dict[count].append(i)   
    
# print(dict)

# -----------------------------------------------------------------------------------------------

# s="a4b2c3"
# output : "aaaabbccc"

s="a4b2c3"
res = ""
lst_var = []
lst_val = []
for i in range(len(s)):
    if i%2==0:
        lst_var.append(s[i])
    else:
        lst_val.append(int(s[i]))
    


for i in range (len(s)//2):
    res += lst_var[i]*lst_val[i]

print(res)

