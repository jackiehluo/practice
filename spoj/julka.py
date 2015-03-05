def apples(total, diff):
    k = (total + diff) / 2
    n = total - k
    print k
    print n

for case in range(10):
    total = int(raw_input())
    diff = int(raw_input())
    apples(total, diff)