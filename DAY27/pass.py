# *pass:
#             it is a keyword which is used to specify the given block is empty

# for i in range(5):
#     if i == 3:



# output:
        # IndentationError: expected an indented block after 'if' statement on line 5


for i in range(5):
    if i == 3:
        pass
    else:
        print("Invalid")