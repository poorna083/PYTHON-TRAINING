# pop():
#   it is used to remove the key and value based on the key specified
#   it raises keyerror if the specified key is not present

# Syntax:
# var_name.pop()

d={'a':1,'b':2,'c':3}
d.pop('b')
print(d)

d.pop('g')
print(d)