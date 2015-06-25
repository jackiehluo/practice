s, ss = raw_input(), raw_input()
count = 0

for i in range(len(s) - len(ss) + 1):
    if s[i:i + len(ss)] == ss:
        count += 1

print count
