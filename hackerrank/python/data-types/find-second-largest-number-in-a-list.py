n = int(raw_input())
a = list(map(int, raw_input().split()))
a = [x for x in a if x != max(a)]
print max(a)
