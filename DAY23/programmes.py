# WAP TO CREATE A LIST FROM A STRING AND ADD ALL THE ELEMENTS BY CONVERTING THEM INTO A UPPER CASE
# str=input("Enter the string :")
# lst =[]
# i=0
# while i < len(str):
#     ele = str[i]
#     lst.append(ele.upper())
#     i+=1
# print(lst)

# WAP TO CREATE A SET FROM A LIST AND ADD THE ELEMENTS IN AN REVERSE ORDER
# lst=[]
# size = int(input("Enter the number of elements :"))
# i=0
# while i < size:
#     elem = input("Enter the element :")
#     lst.append(elem)
#     i+=1
# print(lst)

# s = set()
# j=0
# while j < len(lst):
#     element = lst[j]
#     s.add(element[::-1])
#     j+=1
# print(s)


# WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS INDEX AND VALUE AS ELEMENT

# lst=[]
# size = int(input("Enter the number of elements :"))
# i=0
# while i < size:
#     elem = input("Enter the element :")
#     lst.append(elem)
#     i+=1
# print(lst)

# dict={}
# j=0
# while j<size:
#     dict[j]=lst[j]
#     j+=1
# print(dict)



# WAP TO CREATE A LIST FROM A STRING AND ADD ONLY THE ELEMENTS WHICH ARE IN EVEN INDEX
# s=input("Enter the string  :")
# lst=[]
# i=0
# while i < len(s):
#     lst.append(s[i])
#     i+=2
# print(lst)


# WAP TO CREATE A DICTIONARY FROM A LIST WITH KEY AS ELEMENT AND VALUE AS INDEX

# lst=[]
# size = int(input("Enter the number of elements :"))
# i=0
# while i < size:
#     elem = input("Enter the element :")
#     lst.append(elem)
#     i+=1
# print(lst)

# dict={}
# j=0
# while j<size:
#     dict[lst[j]]= j
#     j+=1
# print(dict)


# WAP TO CREATE A LIST AND ADD THE ELEMENTS IN TUPLE OF ELEMENT AND INDEX PAIR
s=input("enter the string  :")
lst=[]
i=0
while i < len(s):
    elem = s[i]
    lst.append( (elem,i) )
    i+=1
print(lst)
