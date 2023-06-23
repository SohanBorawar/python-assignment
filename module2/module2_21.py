# a Python function to reverses a string if its length is a multiple of 4

str1 = input("enter a string :")

if len(str1) % 4 == 0 :
    print(str1[::-1])
else:
    print(str1)   