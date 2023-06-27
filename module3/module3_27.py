#  a Python program to find the repeated items of a tuple

t = (1,2,3,4,4.4,1.1,54,89,54,1,4,"hello","hello",True)
l = []
for i in t:
    if i not in l and t.count(i)>1:
        l.append(i)
print(l)
