# INDEXING:
#   *it is the process of extracting individual character from a collection is known as 
# INDEXING

# *it raises index error if the specified index is not present

# syntax:
#        variable_name/collection [index]

s = "hello every one"

# get the v, y,n from the string

print(s[8])
print(s[10])
print(s[-2])
print("-----------------------------------")
print(s[9+2-1])
print(s[len(s)-6])
print(s[len('hi')+2])
print("------------------------------------")
# we can also write the indexing method in an form of
print("hello every one"[4])
print("hello every one"[len('hi')+2])