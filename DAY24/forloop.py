# WRITE A PROGRAM TO PRINT 1 TO 5 NUMBERS 
# for i in range(1,6):
#     print(i)

# WRITE A PROGRAM TO PRINT ALL THE EVEN NUMBERS FROM 1 TO 100 
# BY USING CONDITIONAL STATEMENT AND WITHOUT USING CONDITIONAL STATEMENT
# method1:
# for i in range (1,101):
#     if i%2 ==0:
#         print(i)

# method2:
# for i in range (2,101,2):
#         print(i)

# WRITE A PROGRAM TO PRINT ALL THE ELEMENT PRESENT IN THE GIVEN STRING BY USING FOR LOOP AND WHILE LOOP
# s="apple"
# forloop:
# for i in range(0,len(s)):
#     print(s[i])

#While loop
# i=0
# while i < len(s):
#     print(s[i])
#     i+=1

# WRITE A PROGRAM TO PRINT 5 TO 1 NUMBERS BY USING FOR LOOP 
# for i in (range(5,0,-1)):
#     print(i)

# WRITE A PROGRAM TO PRINT ALL THE ELEMENTS PRESENT IN A GIVEN LIST 
# LIST=[APPLE,BAT,CAT,DOG]
# Lst=['APPLE','BAT','CAT','DOG']
# for i in range (len(Lst)):
#     print(Lst[i])

# for i in Lst:
#     print(i)

# WRITE A PROGRAM TO PRINT ALL THE ELEMENTS WHICH ARE IN ODD INDEX FROM A TUPLE 
# TUPLE=(A,B,C,D,E,F,G)
tup=('A','B','C','D','E','F','G')
# for i in range (0,len(tup),2):
#     print(tup[i])

# i=1
# while i < len(tup):
#     print(tup[i])
#     i+=2

# WRITE A PROGRAM TO CREATE A LIST FROM A STRING AND ADD THE ELEMENTS IN THE UPPER CASE 
lst=[]
s="pythonprogram"
for i in range(len(s)):
    res = s[i].upper()
    lst.append(res)
print(lst)