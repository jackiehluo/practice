count = 0
number = 1

while count < 10001:
	number += 1
	for i in range(2, number):
		if number % i == 0:
			break
	else:
		count += 1

print number