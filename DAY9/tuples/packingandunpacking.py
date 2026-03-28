
# unpacking:

lst=[11,22,33,44]
a,b,c,d=lst
print(a)
print(b)
print(c)
print(d)

# packing:

a=10,20
print(a)

a,*b,c,d=10,20,30,40,50
print(a)
print(b)
print(c)
print(d)