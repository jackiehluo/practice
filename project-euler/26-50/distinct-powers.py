powers = set()

for i in range(2, 101):
    for j in range(2, 101):
        powers.add(i ** j)

print len(powers)