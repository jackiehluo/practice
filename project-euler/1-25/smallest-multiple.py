number = 20

for i in range(20, 1000000000, 20):
	divisibles = 0
	for j in range(1, 21):
		if i % j == 0:
			divisibles += 1
	if divisibles == 20:
		print i
		break