# Write a Python program to count the number of lines in a text file.

num = 0
with open("mod1.txt","r") as file:
    r = file.readlines()
for i in r:
    num += 1
print(num)    