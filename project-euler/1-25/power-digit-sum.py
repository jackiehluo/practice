number = 2 ** 1000
string = str(number)
digit_sum = 0

for digit in string:
	digit_sum += int(digit)

print digit_sum