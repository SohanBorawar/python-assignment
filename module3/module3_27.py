#  a Python program to find the repeated items of a tuple

t = (1,2,3,4,4.4,1.1,54,89,54,1,4)

for i in t:
    if t.count(i)>1:
        print(i)
else:
    print("no repeated items")