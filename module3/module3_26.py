#  a Python program to replace last value of tuples in a list.

t = (1,2,3,4,5,6,[9,87,6,5,4,3.2],7,8,9,10)

t[6].pop()
t[6].append(100)
print(t)
