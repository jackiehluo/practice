max_sum = 0

for i in range(99, 0, -1):
    for j in range(99, 0, -1):
        v = sum(int(x) for x in str(i ** j))
        if v > max_sum:
            max_sum = v

print max_sum