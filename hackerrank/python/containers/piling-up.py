def pile_cubes(n, s):
    if s[0] >= s[-1]:
        ind = 0
    else:
        ind = -1
    stack = [s[ind]]
    del s[ind]
    for _ in range(1, n):
        if s[0] >= s[-1]:
            ind = 0
        else:
            ind = -1
        if stack[-1] >= s[ind]:
            stack.append(s[ind])
            del s[ind]
        else:
            return "No"
    return "Yes"

t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    side_lengths = map(int, raw_input().split())
    print pile_cubes(n, side_lengths)