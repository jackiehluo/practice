def kaprekar(p, q):
    n = []
    for i in range(p, q + 1):
        s = str(i ** 2)
        m = len(s) / 2
        if len(s) == 1 and i == i ** 2:
            n.append(i)
        elif len(s) > 1 and i == int(s[0:m]) + int(s[m:]):
            n.append(i)
    if n:
        return " ".join(map(str, n))
    else:
        return "INVALID RANGE"

p = int(raw_input())
q = int(raw_input())
print kaprekar(p, q)
