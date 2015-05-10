n, m = map(int, raw_input().split())
table = []

for _ in range(n):
    row = [int(x) for x in raw_input().split()]
    table.append(row)

k = int(raw_input())

result = sorted(table, key=lambda x: x[k])

for r in result:
    print " ".join(map(str, r))