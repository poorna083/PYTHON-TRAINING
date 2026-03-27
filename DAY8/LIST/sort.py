# sort():

#  it is used to arrange the elements either assending order or desending order
# it has two arguments.they are:
# *reverse
# *key

# syntax:
#    var_name.sort([reverse=true/false],[key=function])
list=[1,3,2,5,4]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list1=['a','b','A','E','f']
list1.sort()
print(list1)

list2=["apple","orange","grapes","Apple","app"]
list2.sort()
print(list2)

list3=[[1,2],[3,7],[1,3,2],[1,2,3,4],[5,3],[7,1]]
list3.sort()
print(list3)

# list4=[1,'apple',[2,1,3]]
# list4.sort()



# key=function
list5=["apple","Apple","mango","grapes"]
list5.sort(reverse=False,key=str.upper)
print(list5)