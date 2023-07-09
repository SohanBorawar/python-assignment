# Write a Python program to copy the contents of a file to another file.

file = open("mod1.txt","r")
copyy = file.read()
file.close()
print("*"*60)

file = open("mod2.txt","w")
file.write(copyy)
file.close()