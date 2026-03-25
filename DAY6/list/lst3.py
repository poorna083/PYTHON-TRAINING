list = [1,2,[3,4,[5,6,[7,8]]]]

# get   4,6,7 and update 5 -> 55

print(list[2][1])
print(list[2][2][1])
print(list[2][2][2][0])

list[2][2][1]=55
print(list)