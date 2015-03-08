from itertools import permutations

s = '0123456789'
n = 10
count = 0

for p in permutations(s, n):
	count += 1
	if count == 1000000:
		print p
		break