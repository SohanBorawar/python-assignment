# a Python program to get a single string from two given strings separated by a space and swap the first two characters of each string.

str1 = input("enter string S1 :")
str2 = input("enter string S2 :")

a = str2[:2] + str1[2:]
b = str1[:2] + str2[2:]

print(a," ",b)