# from keys():
#   it is used to create a dictionary from a collection of keys
#   by default it will assign the values as None

# syntax:
# var_name = dict.fromkeys(collection,[value=None])

lst=['bgmi','free fire','cod','coc','gta5']

d =dict.fromkeys(lst)

print(d)

d=dict.fromkeys(lst,'mobile game')

print(d)

d['free fire']='waste game'

print(d)