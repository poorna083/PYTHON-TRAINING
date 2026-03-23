# join():
#      it is used to add the specified in between the element present in the given collection
#      the return type of join is string

# syntax:
# "string".join(collection)

s="malayalam"
print("-".join(s))


# Q) convert the 'hello every one" into "one every hello"
s1 = "hello every one"
lst = s1.split()
res = lst[::-1]
print(' '.join(res))