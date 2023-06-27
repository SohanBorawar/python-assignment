# Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary. 
#Sample data: {'1': ['a','b'], '2': ['c','d']} 
#Expected Output: 
#ac ad bc bd
l=[]
d={'1': ['a','b'], '2': ['c','d']}.items()

print(d)
for i,j in d:
    print(i,j)
    

print(l)    
    
