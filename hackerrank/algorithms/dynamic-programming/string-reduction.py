def find_length(counts):
    evens, odds, zeroes = True, True, 0
    for k, v in counts.iteritems():
        if v == 0:
            zeroes += 1
        else:
            c = k
        if v % 2 == 0:
            odds = False
        else:
            evens = False
    if zeroes == 2:
        return counts[c]
    return 2 if (evens or odds) else 1

for _ in range(int(raw_input())):
    counts = {"a": 0, "b": 0, "c": 0}
    for c in raw_input():
        counts[c] += 1
    print find_length(counts)