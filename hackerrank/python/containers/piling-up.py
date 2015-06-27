def pile_cubes(n, s):
    v = s.index(min(s))
    if s[:v] == sorted(s[:v], reverse = True) and s[v:] == sorted(s[v:]):
        return "Yes"
    return "No"

t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    side_lengths = map(int, raw_input().split())
    print pile_cubes(n, side_lengths)