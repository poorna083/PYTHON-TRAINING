#upper()
# it is used to convert all the lower case characters into uppercase
# it wont accept any argument
# the return type of upper is string


# syntax:
# var_name/collection.upper()

s="hello"
print(s.upper())
a='HeLlo'
print(a.upper())
b = "hello"
print(b.upper('c'))
# type error:it cannot accept any argument





# lower()

# syntax:
# var_name/collection.lower()

# it is used to convert all the upper case characters into lowercase
# it wont accept any argument
# the return type of upper is string

t="hello"
print(s.lower())
c='HeLlo'
print(a.lower())
d = "hello"
print(b.lower('c'))
# type error:it cannot accept any argument


# *SWITCHCASE():
# Var_name/collection.switchcase()

# it is used to convert all the lower case characters into uppercase and uppercase into lowercase
# it wont accept any argument
# the return type of upper is string

u ="hello&%#@HSFE"
print(u.swapcase())

 
# (Q) v = 'qspiders' convert the given output as spider from v and convert into upper
#SPIDER     #QSP  # SIE   # RED
 
v = 'qspiders'
print(v[1:7].upper())
print(v[:3].upper())
print(v[1:6:2].upper())
print(v[-2:-5].upper())
print(v[4:7][::-1].upper())






