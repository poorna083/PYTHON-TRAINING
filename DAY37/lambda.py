# lambda:
# A lambda function is a small anonymous function (a function without a name).

# res=lambda a,b:a+b
# print(res(3,4))

# output:
# 7
# ---------------------------------------------------------
# res = lambda a,b,c,d,e:a+b+c+d+e
# print(res(2,3,4,5,6))

# output:
# 20
# -----------------------------------------------------
# even or odd using the lambda

res=lambda no:'even' if no%2==0 else 'odd'
no=int(input("Enter the number :"))
print(res(no))

# output:
# Enter the number :5
# odd
