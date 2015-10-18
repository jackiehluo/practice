total, ind = 0, 0

for i in range(int(raw_input())):
    petrol, distance = map(int, raw_input().split())
    total += petrol - distance
    if total < 0:
        total, ind = 0, i + 1

print ind
