# Write a Python program to append text to a file and display the text.

file = open("mod1.txt","a")
file.write("this is the module 1 txt file.\nthis text is appended by the file append function.\nthis text is appended by the file append function.\nGoood morning.\nhello How are you be healthy")
file.close()
print(60*"*")

file = open("mod1.txt","r")
r = file.read()
print(r)
file.close()