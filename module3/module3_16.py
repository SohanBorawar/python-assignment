# a Python program to check whether a list contains a sub list

l = [1,2,3,5,6,7,8]
l1 = [1,2,3,4,5]

for i in l :
    if i in l1:
        print("list contains sub list")
        break
    else :
        print("list does not contain any sub list ")
        break