# get():
# it is used to get the values based on the key specifiers
# it returns none if the specifird key value is not present
# it accept two arguments.they are:
#          *key
#          *value


# syntax:
#    variable_name.get(key,[value=None])


d={'a':1,'b':2,'c':3}
print(d.get('a'))

print(d.get('g'))

print(d.get('g',"stupid key is not present re check again"))

print(d.get('b'))