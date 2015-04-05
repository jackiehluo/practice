import sys

def borrow(s, offers):
    offers.sort(reverse = True)
    total = 0
    friends = 0
    for offer in offers:
        total += offer
        friends += 1
        if total >= s:
            return str(friends)
    return "impossible"

t = int(sys.stdin.readline().strip())

for case in range(1, t + 1):
    s, f = (int(x) for x in sys.stdin.readline().split())
    offers = [int(y) for y in sys.stdin.readline().split()]
    answer = borrow(s, offers)
    print "Scenario #%d:\n%s\n" % (case, answer)