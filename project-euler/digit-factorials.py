from math import factorial

total = 0

for i in range(10, 2540160):
    digit_sum = sum(factorial(int(digit)) for digit in str(i))
    if digit_sum == i:
        total += digit_sum

print total