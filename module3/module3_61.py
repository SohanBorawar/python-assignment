# Write a Python program to calculate surface volume and area of a cylinder
import math
r = int(input("enter the radius of cylinder :"))
h = int(input("enter the heigth of cylinder :"))
A = 2*math.pi*r**2 + 2*math.pi*r*h

print("the surface volume area of cylinder is :",A)
