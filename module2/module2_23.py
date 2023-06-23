# Write a Python function to insert a string in the middle of a string

str1 = input("enter the original string S1 :")
str2 = input("enter the inserting string S2 :")

mid_index = len(str1) //2
 # integer division (// operator)
print(mid_index) 

print(str1[:mid_index] + str2 + str1[mid_index:])

