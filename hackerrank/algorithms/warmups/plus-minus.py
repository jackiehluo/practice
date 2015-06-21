n = int(raw_input())

pos = 0
zeroes = 0
neg = 0
total = 0

for num in raw_input().split():
    if int(num) > 0:
        pos += 1
    elif int(num) < 0:
        neg += 1
    else:
        zeroes += 1

print "%.3f" % (float(pos) / n)
print "%.3f" % (float(neg) / n)
print "%.3f" % (float(zeroes) / n)