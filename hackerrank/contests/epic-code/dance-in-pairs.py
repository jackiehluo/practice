n, k = map(int, raw_input().split())
boys = sorted(list(map(int, raw_input().split())))
girls = sorted(list(map(int, raw_input().split())))
pairs, i, j = 0, 0, 0

while i < n and j < n:
    if abs(boys[i] - girls[j]) <= k:
        pairs += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1

print pairs