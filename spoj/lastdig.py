def last_dig(a, b):
    return str(a ** b)[-1:]

t = int(raw_input())

for case in range(t):
    a, b = (int(x) for x in raw_input().split())
    answer = last_dig(a, b)
    print answer
