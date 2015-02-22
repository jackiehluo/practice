from math import sqrt

triangle = 0

for i in xrange(1, 100000000):
	triangle += i
	divisors = 0
	for j in xrange(1, int(sqrt(i)) + 1):
		if triangle % j == 0:
			divisors += 1
	if divisors > 500:
		print triangle
		break