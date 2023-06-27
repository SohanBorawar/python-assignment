# Write a Python program to returns sum of all divisors of a number

divisors = []

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
        result = sum(divisors)

print("The sum of divisors of", num, "is", result)
