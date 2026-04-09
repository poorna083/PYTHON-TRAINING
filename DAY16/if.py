# if:
#   it is used to execute a block of code only if the condition is satisfied


# syntax:
# if condition:
#     [TSB]---> True statement block


# write a program to check given number is positive
number = int(input("enter the value:"))
if number>0:
   print(f'given {number} is positive')
print("exit")


# write a program to check given number is more than 5 but less than 10
num = int(input("enter the value:"))
if num > 5 and num <10:
   print(f'{num} is given number is more than 5 but less than 10')
print("exit")



#1.Write a program that checks if the given number is zero
num = int(input("enter the value:"))
if num==0:
    print(f'{num} the given number is zero')
print("exit")


#2. Write a program to check whether the first number is divisible by the second number
num1 = int(input("enter the value:"))
num2 = int(input("enter the value:"))
if  num1%num2==0:
  print(f' first number is divisible by the second number')
print("exit")

#3.Write a program to check if a character entered by the user is a vowel
char = input("enter the char :")
vowel = 'aAeEiIoOuU'
if char in vowel :
  print(f'{char} character entered by the user is a vowel')
print("exit")


#4. wap to covert first letter of the word into upper if it is starting with vowel
char = input("enter the char :")
vowel = 'aAeEiIoOuU'
if char in vowel :
  print(f'{char.upper()} character entered by the user is a vowel')
print("exit")


#5.Write a program that checks if a number entered by the user is a multiple of 5.
number = int(input("enter a number"))
if number%5 ==0:
    print(f'{number} number entered by the user is a multiple of 5')
print("exit")


#6.Write a program that check if a number entered by the user is divisible by both 2 and 3.
number = int(input("enter a number"))
if number%2 ==0 or number%3 ==0:
    print(f'{number} number entered by the user is a multiple of 2 and 3')
print("exit")


#7.wap to check whether the given string is palindrome
str = input("enter the string:")
if str == str[::-1]:
    print(f'{str} the given string is palindrome')
print("exit")


#8.wap to check whether the given number is palindrome
int = input("enter the string:")
if int == int[::-1]:
    print(f'{int} the given string is palindrome')
print("exit")


#9.Write a program that asks the user to enter a number and prints whether it is within the range of 1 to 100 (inclusive)
int = int(input("enter the number:"))
if int >=1 and int <=100:
    print(f'{int} it is within the range of 1 to 100')
print("exit")


#10.Write a program that asks the user to enter three sides of a triangle and prints whether it is an equilateral triangle
float1 = float(input("enter the value:"))
float2 = float(input("enter the value:"))
float3 = float(input("enter the value:"))

if float1 == float2 and float2 == float3 and float3 == float1 and float1 == float3:
    print(f'{float1,float2,float3} it is an equilateral triangle')
print("exit")