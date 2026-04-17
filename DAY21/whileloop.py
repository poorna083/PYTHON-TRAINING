# WAP TO CHECK WHEATHER THE GIVEN NUMBER IS A STRONG NUMBER OR NOT
# no=int(input("Enter the number :"))
# temp1=no
# total = 0
# while temp1>0:
#     rem = temp1 % 10
#     temp1 = temp1 // 10

#     pro = 1
#     while rem > 1:
#         pro=pro*rem
#         rem-=1
#     total += pro
    
# if no == total:
#     print("strong number")
# else:
#     print("not a strong number")


# WAP TO CHECK WHEATHER THE GIVEN NUMBER IS A AUTOMORPHIC NUMBER OR NOT
# no=int(input("enter the number :"))
# pow = no*no
# if pow%10 == no:
#     print("automorphic number")
# else:
#     print("not a automorphic number")


# WAP TO CHECK WHEATHER THE GIVEN NUMBER IS A XYLEM NUMBER AND PHONM NUMBER
no=int(input("enter the number :"))
count = 0
temp1 = no
temp2 = no
temp3 = no
temp4 = no
while temp1 > 0:
    temp1 = temp1 //10
    count +=1

div = 1
i = 1
while i < count:
    div = div * 10
    i += 1

first_elem = temp3 // div
last_elem  = temp2 %10

sum_first_last = first_elem+last_elem

temp4 = no // 10   
middle_elem = 0
pos = 2

while temp4 > 0:
    rem = temp4 % 10

    if pos != count:   
        middle_elem += rem

    temp4 = temp4 // 10
    pos += 1

if sum_first_last == middle_elem:
    print("xylem number")
else:
    print("phonm number")






