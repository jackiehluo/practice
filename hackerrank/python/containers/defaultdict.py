from collections import defaultdict

n, m = map(int, raw_input().split())
n_dict = defaultdict(list)

for i in range(1, n + 1):
    n_dict[raw_input()].append(i)

for j in range(m):
    s = raw_input()
    if n_dict[s]:
        print ' '.join(map(str, n_dict[s]))
    else:
        print -1