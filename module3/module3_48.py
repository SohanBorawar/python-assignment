# Write a Python function to calculate the factorial of a number (a nonnegative integer)

n = int(input("enter a number :"))

if n<0:
    print("There is no defined factorial for negative integer")
elif n==0:
    print("for 0 it is Zero")    
elif n==1:
    print("For 1 it is One")
else:
    result = 1
    for i in range(1,n+1):
        result *= i
print(result)        