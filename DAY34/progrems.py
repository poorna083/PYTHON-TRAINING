# WAP TO CHECK WHEATHER THE PROGRAM IN HOMOGENIUS OR HETEROGENUS 
# lst=eval(input("Enter the list with boundaries :"))
# lst1=[]
# for i in lst:
#     lst1.append(type(i))

# for i in range(len(lst1)):
#     if lst1[0]!=lst1[i]:
#         print('Heterogenius')
#         break

# else:
#     print("homogenious")


# ----------------------------------------------------------------------
# CHECK WHEATHER TWO NUMBERS FORMS A FRIENDLY PAIR OR NOT
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum1 = 0
# for i in range(1, a):
#     if a % i == 0:
#         sum1 += i

# sum2 = 0
# for i in range(1, b):
#     if b % i == 0:
#         sum2 += i

# if sum1 / a == sum2 / b:
#     print("Friendly pair")
# else:
#     print("Not a friendly pair")

# ----------------------------------------------------------------------
#CHECK WHEATHER THE GIVEN NUMBER IS A PRIME NUMBER OR NOT
num=int(input("Enter the number :"))
for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break
    
else:
    print("prime number ")