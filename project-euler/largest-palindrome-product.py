max_pal = 0

for x in range(999, 0, -1):
	for y in range(999, 0, -1):
		product = x * y
		if str(product) == str(product)[::-1] and product > max_pal:
			max_pal = product

print max_pal