total = 2
previous = 1
current = 2

while current <= 4000000:
	temp = current
	current += previous
	if current % 2 == 0:
		total += current
	previous = temp

print total