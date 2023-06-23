# Write a Python function that takes a list and returns a new list with unique elements of the first list.


l = [1,2,5,5,5,55,"bhargav",1,1.1,5,58,55,"hello","hello","bhargav",2,2,5]
l1=[]
# set() function is used to removee duplicate elements in the list 
# set() function will convert it in to set so we have to convert it back in to list by list() function 
#print(list(set(l)))

for i in l:
    if l.count(i) > 1 and i not in l1:
        l1.append(i)
print(l1)
    
