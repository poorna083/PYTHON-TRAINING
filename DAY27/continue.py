# *continue:
#             it is a keyword which is used to skip the current iteration and continue 
#             with the next iteration

i=1
while i <= 5:
    if i == 3:
        i+=1
        continue
    else:
        print(i)
    i+=1
    

# ---------------------------------------------------------------------------------
for i in range(1,6):
    if i == 3:
        continue
    print(i)