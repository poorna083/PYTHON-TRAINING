# WAP TO CHECK WHEATHER GIVEN ELEMENT IS PRESENT IN THE COLLECTION OR NOT
lst=[1,4,3,6,2,10]


target = int(input("Enter the target :"))


# if target in lst:
#     print("present")
# else:
#     print("not present")


for i in lst:
    if i == target:
        print("present")
        break
else:
    print("not present ")


# WAP TO CHECK WHEATHER GIVEN NUMBER IS PRESENT IN THE COLLECTION OR NOT
no=int(input("Enter the number :"))
for i in range(2,no):
    if no%i==0:
        print("NOT A PRIME NUMBER")
        break
else:
    print("PRIME NUMBER")