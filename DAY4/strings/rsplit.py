# rsplit():
#     it is used to split the given the string based on saperator and amxsplit from the rightside
#     by default value is saperator

# syntax:
#     var_name.rsplit([saperator],[max_splits])

s="hello every one"
print(s.rsplit())
print(s.rsplit(maxsplit=1))
print(s.rsplit('a',5))