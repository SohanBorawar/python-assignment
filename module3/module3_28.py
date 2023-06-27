# Write a Python program to remove an empty tuple(s) from a list of tuples.

l= [(1,2,3,4,5,"hello"),(6,7,8,89,"vishal"),(1,3,5,6),(),(56,78,89,3,23,"sohan")]

for i in l:
    if len(i)<1:
        l.remove(i)
        print(l)
    