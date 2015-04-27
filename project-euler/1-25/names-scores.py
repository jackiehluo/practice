s = raw_input()
names = s.strip().split(',')
names.sort()
total = 0

for n in range(len(names)):
    worth = 0
    for c in range(1, len(names[n]) - 1):
        worth += ord(names[n][c]) - 64
    print names[n], worth
    total += (n + 1) * worth

print total