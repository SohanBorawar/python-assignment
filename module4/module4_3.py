# Write a Python program to read first n lines of a file.           

nlines = int(input("Enter The Number Of Lines To Print :"))

with open("mod1.txt","r") as file:
    text = file.readlines()

for i in text[:nlines]:
    print(i)