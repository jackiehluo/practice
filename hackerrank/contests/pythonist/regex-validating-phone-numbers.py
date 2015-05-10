import re

for _ in range(input()):
    n = raw_input()
    if len(n) == 10 and re.match('[7-9]+', n[0]) and n.isdigit():
        print "YES"
    else:
        print "NO"