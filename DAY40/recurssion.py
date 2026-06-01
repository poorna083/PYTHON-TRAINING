# WAP TO FIND THE FACTORIAL OF A GIVEN BY USING RECURSSION

def recurssion(no):
    if no==1:
        return 1
    else:
        return no*recurssion(no-1)
    
num=int(input("Enter a number :"))
res=recurssion(num)
print(res)