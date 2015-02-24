max_sequence = 0

for i in range(1000000, 0, -1):
	sequence = 1
	n = i
	while n > 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		sequence += 1
	if sequence > max_sequence:
		max_sequence = sequence
		start = i
print start