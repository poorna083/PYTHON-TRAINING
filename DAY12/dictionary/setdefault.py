# setdefault():
#  it is used to add the key and value into a dictionary
#  by default it will assign a value None
#  setdefault will return the value which is assigned to the key

d={'a':1,'b':2}
d.setdefault('c')

print(d)

d.setdefault('f',4)

print(d)