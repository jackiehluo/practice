def read(t):
    l = t.lower()
    if "hackerrank" in l:
        return 1
    else:
        return 0

n = int(raw_input())
count = 0

for line in range(n):
    t = raw_input()
    count += read(t)
    
print count
