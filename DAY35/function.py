# from function1 import greet

# greet()


# output:

# Hello everyone
# Hello everyone

# When a function is in another file, you must import that file (module) to use the function






# -------------------------------------------------------------------------------------------
# WAP TO PRINT THE SUM OF TWO NUMBERS
# def sum(a,b):
#     print(a+b)

# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# sum(a,b)
# -------------------------------------------------------------------------------------------
# WAP TO PRINT MULTIPLICATION OF TWO NUMBERS
# def mul(a,b):
#     print(a*b)

# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# mul(a,b)
# ------------------------------------------------------------------------------------------
# WAP TO PRINT STRING AS INPUT AND PRINT IT IN UPPERCASE
# def upper(s):
#     print(s.upper())

# s=input("Enter the string :")
# upper(s)
# ---------------------------------------------------------------------------------------
# WAP TO PRINT THE LENGTH OF A GIVEN STRING
# def length(s):
#     print(len(s))

# s=input("Enter the string :")
# length(s)
# ----------------------------------------------------------------------------------------
# WAP TO PRINT THE NUMBER IS EVEN OR ODD
def oddoreven(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

num=int(input("Enter the number :"))
oddoreven(num)