def find_hackerrank(s):
    end = len(s) - 1
    if s[0] == "hackerrank" and s[end] == "hackerrank":
        return 0
    elif s[0] == "hackerrank":
        return 1
    elif s[end] == "hackerrank":
        return 2
    else:
        return -1

t = int(raw_input())

for case in range(t):
    s = []
    for w in raw_input().split():
        s.append(w)
    answer = find_hackerrank(s)
    print answer
