from math import factorial

number = factorial(100)
string = str(number)
sum = 0

for digit in string:
    sum += int(digit)

print sum 
