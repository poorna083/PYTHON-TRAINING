# remove all the duplicate elements 
# lst=[1,2,4,3,2,1,5,3]
# res = []
# for i in lst:
#     if i not in res:
#         res.append(i)

# print(res)

# -----------------------------------------------------------------------------------------------------

lst=['apple fruit','jasmine flower','mango fruit','neem plant','rose flower','money plant']

# output:
# {'fruit': ['apple', 'mango'], 'flower': ['jasmine', 'rose'], 'plant': ['neem', 'money']}

# dict = {}
# for i in lst:
#     value,key = i.split()
#     if key not in dict:
#         dict[key]=[value]
#     else:
#         dict[key].append(value)

# print(dict)

# -----------------------------------------------------------------------------------------------------------
s='apple mango apple orange'
# output:
# apple:-2
# orange:-1
# mango:-1

# lst=s.split()

# for i in range(len(lst)):
#     count = 1
#     for j in range(i+1,len(lst)):
#         if lst[i]==lst[j]:
#             count+=1
#     print(f'{lst[i]}:- {count}')

# --------------------------------------------------------------------------------------------------------

# WAP TO CHECK NUMBER OF CONSONENTS IN A GIVEN STRING 

# s = input("Enter the string :")
# count = 0
# for i in s:
#     if i.isalpha:
#         if i.lower() not in 'aeiou':
#             count+=1

# print(f'count of consonents in a given string is {count}')
    
# WAP TO CHECK NUMBER OF vowels IN A GIVEN STRING 

# count = 0
# for i in s:
#     if i.isalpha:
#         if i.lower()  in 'aeiou':
#             count+=1

# print(f'count of vowels in a given string is {count}')
    








# ----------------------------------------------------------------------------------------------------------
# WAP TO VALIDATE THE PASSWORD:
# CONDITIONS:
# MINMUM 8 CHARACTERS
# (1 UPPERCASE , 1LOWERCASE , 1 DIGIT , 1 SPECIAL CHARACTER) ARE MANDATORY
print("""ENTER PASSWORD:
      1 UPPERCASE , 1LOWERCASE , 1 DIGIT , 1 SPECIAL CHARACTER ARE MANDATORY""")
password = input("Enter the password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

if len(password) >= 8:
    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        elif i in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/":
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Valid password")
    else:
        print("Invalid password (missing conditions)")
else:
    print("Entered password length is less than 8 ❌")

        
    




    

