# A program to provide summ of three integers by the user input and any two inputs are same then print zero

print(">>>>>>>>> To provide sum of Three integers and if two inputs are equal ")

a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
c = int(input("enter number 3:"))


if a==b or b==c or c==a:
    sum = 0
    print("sum of number is :",sum)
else:
    sum = a+b+c
    print("sum of number is :",sum)
    

 