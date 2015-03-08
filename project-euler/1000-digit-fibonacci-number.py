term = 3
previous = 1
current = 2
digits = 1

while digits < 1000:
	temp = current
	current += previous
	if len(str(current)) > digits:
		digits = len(str(current))
	previous = temp
	term += 1

print term