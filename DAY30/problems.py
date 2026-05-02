s1="python class"
# output:
#     nothyp ssalc

# a,b=s1.split()
# print(a[::-1]+" "+b[::-1])

# output:
#     nothyp ssalc




s2="hai hello how are you"
# output:
#     {'hai':3,'hello':4,'how':3,'are':3,'you':3}

# dict={}
# lst=s2.split()
# for i in lst:
#     count = 0
#     for j in i:
#         count+=1
#     dict[i]=count

# print(dict)

# output:
#     {'hai':3,'hello':4,'how':3,'are':3,'you':3}

s3='aabcbabcab'
# output:
# a4b4c2


freq = {}

for ch in s3:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

res = ""
for key in freq:
    res += key + str(freq[key])

print(res)
    

