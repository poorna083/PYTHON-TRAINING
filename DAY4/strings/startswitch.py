# startswitch:
#    it return true if the given string starts with the specified element
#    the return type of startswitch is boolean

# syntax:
#    var_name(startswitch/element,[si],[ei])

s = 'qspiders'
print(s.startswith('q'))
print(s.startswith('j'))
print(s.startswith('qsp'))
print(s.startswith('p',2,6))