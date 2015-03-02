def add_rev(a, b):
    a_rev = int(str(a)[::-1])
    b_rev = int(str(b)[::-1])
    num = a_rev + b_rev
    return int(str(num)[::-1])

t = int(raw_input())

for case in range(t):
    a, b = (int(x) for x in raw_input().split())
    answer = add_rev(a, b)
    print answer
