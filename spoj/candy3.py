t = int(raw_input())

for case in range(t):
    line = raw_input()
    n = int(raw_input())
    candies = 0
    for num in range(n):
        candies += int(raw_input())
    if candies % n == 0:
        print "YES"
    else:
        print "NO"
