#  a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

import random
l =[]

for i in range (1,11):
    i = random.randint(1,30)
    i = i*i
    l.append(i)
   # print(l)    
print(l)    