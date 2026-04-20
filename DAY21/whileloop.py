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
# temp = no
# count = 0
# square = no **2
# while temp > 0:
#     count+=1
#     temp = temp//10
# final_output = square %(10**count)
# if no == final_output:
#     print("automorphic number")
# else:
#     print("not a automorphic number")





# WAP TO CHECK WHEATHER THE GIVEN NUMBER IS A XYLEM NUMBER AND PHONM NUMBER
# no = int(input("enter the number :"))
# temp = no
# temp1 = no
# sum = 0
# count = 0
# while temp > 0:
#     temp = temp//10
#     count +=1
# last_elem = temp1 %10
# first_elem = temp1 // (10**(count-1))
# sum_of_end = last_elem+first_elem

# middle = (no % (10 ** (count - 1))) // 10
# while middle > 0:
#     rem = middle % 10
#     sum += rem
#     middle = middle//10
# if sum == sum_of_end:
#     print("xylem")
# else:
#     print("phonem")








# no = int(input("enter the number  :"))
# temp = no
# sum_of_end=0
# sum_of_mid=0
# while no >0:
#     rem = no %10
#     if no == temp or no < 10:
#         sum_of_end+=rem
#     else:
#         sum_of_mid+=rem
#     no = no//10
# if sum_of_end==sum_of_mid:
#     print("xylem")
# else:
#     print("phonem")




# WAP to show that the given number is a happy number or not

# no = int(input("Enter the number  :"))
# temp = no

# while temp !=1 and temp !=4:
#     sum = 0
#     while temp > 0:
#         rem = temp % 10
#         sum = rem**rem
#         temp = temp // 10
#     temp = sum
# if temp ==1 :
#     print("happy number ")
# else:
#     print("Not an happy number")







