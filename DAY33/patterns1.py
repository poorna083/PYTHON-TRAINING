# 1. Right Triangle
# *
# **
# ***
# ****
# *****
n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     print('*'*i,end='')
#     print(' '*(n-1))

# output:
# Enter the number :5
# *    
# **    
# ***    
# ****    
# *****    

# --------------------------------------------------------------------------------
# 2. Inverted Triangle
# *****
# ****
# ***
# **
# *
# for i in range(0,n):
#     print('*'*n,end='')
#     print(' '*i)
#     n-=1

# output:
# Enter the number :5
# *****
# **** 
# ***  
# **   
# *    
# ---------------------------------------------------------------------------------
# 3. Pyramid
#     *
#    ***
#   *****
#  *******
# *********
# j=1
# for i in range(1,n+1):
#     print(' '*(n-i),end=' ')
#     print('*'*j)
#     j+=2

# output:
# Enter the number :5
#      *
#     ***
#    *****
#   *******
#  *********

# -----------------------------------------------------------------
# 4. Inverted Pyramid
# *********
#  *******
#   *****
#    ***
#     *
# j=(n*2)-1
# for i in range(0,n):
#     print(' '*i,end=' ')
#     print('*'*j)
#     j-=2

# output:
# Enter the number :5
#  *********
#   *******
#    *****
#     ***
#      *

# ------------------------------------------------------------------------------
# 5. Diamond
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# j=1
# for i in range(1,n):
#     print(' '*(n-i),end='')
#     print('*'*j)
#     j+=2
# k=(n*2)-1
# for i in range(0,n):
#     print(' '*i,end='')
#     print('*'*k)
#     k-=2

# output:
# Enter the number :5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# --------------------------------------------------------------
# 6. Number Increasing
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,n+1):
#     count=1
#     for j in range(1,n+1):
#         if i>=j:
#             print(count,end='')
#             count+=1
#     print()

# output:
# Enter the number :5
# 1
# 12
# 123
# 1234
# 12345

# ----------------------------------------------------------------
# 7. Number Decreasing
# 12345
# 1234
# 123
# 12
# 1
# for i in range(1,n+1):
#     count=n
#     for j in range(1,n+1):
#         if i<=j:
#             print(count,end='')
#         count-=1
#     print()

# output:
# Enter the number :5
# 54321
# 4321
# 321
# 21
# 1

# ---------------------------------------------------------------------
# 8. Same Number Row
# 1
# 22
# 333
# 4444
# 55555
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(i,end='')
#     print()

# output:
# Enter the number :5
# 1
# 22
# 333
# 4444
# 55555

# -------------------------------------------------------------------
# 9. Floyd’s Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(count,end=' ')
#             count+=1
    # print()

# output:
# Enter the number :4
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# ----------------------------------------------------------------

# 14. Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# output:
# Enter the number :5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# --------------------------------------------------------------
# 15. Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('* '*i)
