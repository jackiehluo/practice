def check_perm(n, perm):
    seq = {}
    for i in range(1, n + 1):
        seq[perm[i - 1]] = i
    for i in range(1, n + 1):
        if perm[i - 1] != seq[i]:
            return "not ambiguous"
    return "ambiguous"


while True:
    n = int(raw_input())
    if n == 0:
        break
    perm = map(int, raw_input().split())
    print check_perm(n, perm)