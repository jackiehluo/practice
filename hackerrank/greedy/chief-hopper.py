n = int(raw_input())
h = [int(x) for x in raw_input().split()]

for energy in range(max(h) + 1):
    current = energy
    for height in h:
        if height > current:
            current -= (height - current)
        else:
            current += (current - height)
        if current < 0:
            break
    if current >= 0:
        print energy
        break
