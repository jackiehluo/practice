def find_number(x, y):
	if x == y:
		if x % 2 == 0:
			return x * 2
		else:
			return x * 2 - 1
	elif x > 1 and y == x - 2:
		if x % 2 == 0:
			return x * 2 - 2
		else:
			return x * 2 - 3
	else:
		return "No Number"

t = int(raw_input())

for case in range(t):
	x, y = (int(a) for a in raw_input().split())
	answer = find_number(x, y)
	print answer