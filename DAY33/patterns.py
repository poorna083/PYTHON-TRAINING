n=int(input("ENter the number :"))
# 1. Butterfly Pattern
# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *
# for i in range(1,n+1):
#     print('*'*i,end='')
#     print(' '*(n-i)*2,end='')
#     print('*'*i)
# for i in range(n,0,-1):
#     print('*'*i,end='')
#     print(' '*(n-i)*2,end='')
#     print('*'*i)


# output:
# ENter the number :5
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# 2. Hollow Diamond
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

# for i in range(1, n+1):
#     print(' '*(n-i), end='')

#     if i == 1:
#         print('*')
#     else:
#         print('*', end='')
#         print(' '*(2*i-3), end='')
#         print('*')

# for i in range(n-1, 0, -1):
#     print(' '*(n-i), end='')

#     if i == 1:
#         print('*')
#     else:
#         print('*', end='')
#         print(' '*(2*i-3), end='')
#         print('*')

# output:
# ENter the number :5
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
    #   *
# 3. Number Pyramid Palindrome
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
# for i in range(1, n+1):
#     # spaces
#     print(' '*(n-i), end='')

#     # decreasing part
#     for j in range(i, 0, -1):
#         print(j, end=' ')

#     # increasing part
#     for j in range(2, i+1):
#         print(j, end=' ')

#     print()
# 4. Zig-Zag Pattern
# *   *   *
#  * * * * 
#   *   *

# 5. Spiral Matrix
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7

# 6. Pascal’s Triangle
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1
# from math import factorial
# for i in range(n):
#     print(' ' * (n - i), end=' ')
#     for j in range(i + 1):
#         ncr = factorial(i) // (factorial(j) * factorial(i - j))
#         print(ncr, end=' ')
        
#     print()

# 7. Sandglass Pattern
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

# 8. Hollow Hourglass
# *********
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *********

# 9. Binary Pattern
# 1
# 01
# 101
# 0101
# 10101

# 10. Alternating 0-1 Triangle
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# 11. Diamond with Numbers
#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1

# 12. Concentric Square Pattern
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5