'''Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''

str1 = input("enter a string S :")

s_not = str1.find("not")                #The find method returns the index of the substring if found or -1 if not found
s_poor = str1.find("poor")              # so thats in condition we use != -1 

print(s_not)
print(s_poor) 


if s_not != -1 and s_poor != -1 and s_not < s_poor :
    print(str1[:s_not]+ "good" + str1[s_poor+4:])
else:
    print(str1)    
