# WAP TO PRINT FACTIORAL OF A GIVEN NUMBER
# no=int(input("Enter the number :"))
# res=1
# while no >1:
#     res = res*no
#     no-=1
# print(res) 
# WAP TO REVERSE THE GIVEN NUMBER
# no=int(input("enter the number :"))
# rev = 0
# while no>0:
#     rem = no%10
#     rev = rev*10 +rem
#     no = no//10
# print(rev)
# WAP TO FIND THE SUM OF ALL THE DIGITS PRESENT IN A GIVEN NUMBER
# no=int(input("enter the number :"))
# sum = 0
# while no > 0:
#     rem = no%10
#     sum =sum+rem
#     no = no//10
# print(sum)
# WAP TO CHECK GIVEN NUMBER IS PALANDROME OR NOT
# no=int(input("enter the number :"))
# temp = no
# rev = 0
# while no > 0:
#     rem = no % 10
#     rev = rev*10 + rem
#     no//=10
# if temp == rev:
#     print("palindraome")
# else:
#     print("not a palindrome")
# WAP TO CHECK A PROGRAM IS A SPY NUMBER OR NOT
# no=int(input("enter the number :"))
# sum = 0
# pro = 1
# while no > 0:
#     rem = no%10
#     sum += rem
#     pro *= rem
#     no//=10
# if sum == pro:
#     print("spy number")
# else:
#     print("not a spy number")
# WAP TO CHECK A PROGRAM IS A PERFECT NUMBER OR NOT
# no = int(input("Enter the number: "))
# i = 1
# val = 0
# while i < no:
#     if no % i == 0:
#         val += i
#     i += 1
# if val == no:
#     print("perfect number")
# else:
#     print("not a perfect number")
# WAP TO CHECK A PROGRAM IS A ARMSTRONG NUMBER
# no = int(input("enter the number: "))
# temp = no          
# count = 0
# ams = 0

# while temp > 0:
#     count += 1
#     temp = temp // 10

# size = count
# temp = no          

# while temp > 0:
#     rem = temp % 10
#     ams += rem ** size
#     temp = temp // 10

# if ams == no:
#     print("armstrong number")
# else:
#     print("not an armstrong number")

# WAP TO CHECK A PROGRAM IS A DISARIEN NUMBER
no = int(input("enter the number: "))
temp = no
count = 0
dis = 0

while temp > 0:
    count += 1
    temp = temp // 10

temp = no
pos = count   

while temp > 0:
    rem = temp % 10
    dis += rem ** pos
    temp = temp // 10
    pos -= 1

if dis == no:
    print("DISARIUM NUMBER")
else:
    print("NOT A DISARIUM NUMBER")