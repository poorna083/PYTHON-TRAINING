# WAP TO PRINT SUM OF FIRST 100 FIBNOCII NUMBERS
# no=int(input("Enter the number :"))
# a=0
# b=1
# sum=0
# while no>0:
#     sum+=a
#     c=a+b
#     a=b
#     b=c
#     no-=1
# print(sum)
# WAP TO CHECK GIVEN NUMBER IS A HAPPY NUMBER OR NOT IF HAPPYNUMBER CHECK IT IS ODD OR EVEN 

# num=int(input("Enter the number :"))
# temp=num
# lst=[]
# while num!=1 and num not in lst:
#     lst.append(num)
#     sum=0
#     while num>0:
#         rem=num%10
#         sum+=(rem)**2
#         num=num//10
#     num=sum
# if num==1:
#     if temp%2==0:
#         print('happy even number ')
#     else:
#         print('happy odd number ')
# else:
#     print('not a happy number')

# WAP TO PRINT ALL THE STRONG NUMBERS IN A LIST
# lst = [145,123,585,2,178]

# for i in lst:
#     temp = i
#     total = 0
#     while i > 0:
#         val = i % 10
#         fact = 1
#         while val > 0:
#             fact *= val
#             val -= 1
#         total += fact
#         i = i // 10
#     if temp == total:
#         print(temp, "strong number")
#     else:
#         print(temp, "not a strong number")
        
# WAP TO FIND THE FOLLOWING PROGRAM
# input;
# lst=['a','b','c','d']
# d={}
# for i in lst:
#     up=i.upper()
#     d[i]=up

# print(d)

# output:{a:'A',b:'B',c:'C',d:'D'}

# WAP TO CREATE A DICTIONARY WITH KEY AS INDEX AND VALUES AS SUM OS ELEMENTS WHICH
# ARE PRESENT IN DIFFERENT LISTS
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[11,12,13,14,15]
d={}
from itertools import zip_longest
for h,(i,j,k) in enumerate(zip_longest(l1,l2,l3,fillvalue=' ')):
    d[h]=(i+j+k)
print(d)