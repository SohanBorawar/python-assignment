# Write a Python program to read a file line by line and store it into a list

l = []

file = open("mod1.txt","r")

line = file.readlines()
for store in line:
    l.append(store)
print(l)