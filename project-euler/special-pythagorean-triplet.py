from math import sqrt

for i in range(1000):
	for j in range(1000):
		if i < j:
			if sqrt(i ** 2 + j ** 2) == int(sqrt(i ** 2 + j ** 2)):
				a = i
				b = j
				c = sqrt(i ** 2 + j ** 2)
				if a + b + c == 1000:
					print int(a * b * c)
					break