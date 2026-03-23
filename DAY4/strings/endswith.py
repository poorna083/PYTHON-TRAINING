# endswitch:
#    it return true if the given ending ends with the specified element
#    the return type of startswitch is boolean

# syntax:
#    var_name(startswitch/element,[si],[ei])

s = 'qspiders'
print(s.endswith('s'))
print(s.endswith('j'))
print(s.endswith('ers'))
print(s.endswith('p',2,6))