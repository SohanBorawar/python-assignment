# Write a Python program to write a list to a file.

l = ['apple', 'banana', 'cherry', 'date']

file = open("mod2.txt","a")
for i in l:
    file.write(i+"\n")
file.close()
print("*"*60)

file = open("mod2.txt","r")
view = file.read()
print(view)
file.close()