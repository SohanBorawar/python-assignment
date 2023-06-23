# a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

str1 = input("enter a string S :")

if len(str1)> 3 and str1.endswith("ing") == False :
    print(str1+"ing")

elif str1.endswith("ing"):
    print(str1+"ly")
elif len(str1)<3:
    print(str1)
else:
    print("invalid input")

