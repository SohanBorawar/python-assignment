# A to print firnt n positive number 

print("print the sum of entered number by the user ")

'''n= int(input("enter the number :"))
sum= 0

while n>0:
    sum = sum + n
    n= n-1
print("sum :",sum)'''

n = int(input("enter n:"))
result = sum(range(1,n+1))
print(result)
