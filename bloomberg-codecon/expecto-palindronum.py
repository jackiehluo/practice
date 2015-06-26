s = list(raw_input())
c = []

while s != s[::-1]:
    c.append(s.pop())

print len(s) + len(c) * 2
