number = int(raw_input())
rocks = []

for x in range(number):
    rocks.append(set(raw_input()))

print len(set.intersection(*rocks))