# Write a Python program to read last n lines of a file.

nlines = int(input("enter number of n line to print :"))

with open("mod1.txt","r") as file:
    lines = file.readlines()
    for Nlines in lines[nlines: :-1]:
        print(Nlines)