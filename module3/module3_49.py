# Write a Python function to check whether a number is perfect or not.

def is_perfect_number(num):
    if num < 1:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        return True
    else:
        return False
number = 28
is_perfect = is_perfect_number(number)

if is_perfect:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
