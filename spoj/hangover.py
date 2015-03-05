import sys

def hang(length):
	c = 0.0000
	f = 1.0000
	while c < length:
		f += 1.0000
		c += 1.0000 / f
	return str(int(f - 1)) + " card(s)"

for line in sys.stdin:
    length = float(line)
    if length != 0.00:
    	answer = hang(length)
    	print answer