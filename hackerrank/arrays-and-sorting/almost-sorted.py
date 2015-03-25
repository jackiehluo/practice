def sort(n, d):
    sd = sorted(d)
    if d == sd:
        return True
    index = []
    for i in range(n):
        if d[i] != sd[i]:
            index.append(i + 1)
    if len(index) == 2:
        return index
    elif index:
        first, last = index[0], index[-1]
        sublist = d[first - 1:last]
        if sublist[::-1] == sd[first - 1:last]:
            return first, last

n = int(raw_input())
d = [int(x) for x in raw_input().split()]
answer = sort(n, d)
if answer:
    print "yes"
    if type(answer) is not bool:
        if type(answer) is list:
            print "swap", " ".join(map(str, answer))
        elif type(answer) is tuple:
            print "reverse", " ".join(map(str, answer))
else:
    print "no"