t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    count = {}
    for i in range(n):
        acc = raw_input()
        if acc in count:
            count[acc] += 1
        else:
            count[acc] = 1
    answer = sorted(count.items())
    for k, v in answer:
        print k + " " + str(v)
    if case != t - 1:
        line = raw_input()
        print line