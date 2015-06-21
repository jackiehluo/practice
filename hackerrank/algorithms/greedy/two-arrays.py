def compare_arrays(n, k, a, b):
    a.sort()
    b.sort(reverse = True)
    for i in range(n):
        if a[i] + b[i] < k:
            return "NO"
    return "YES"

t = int(raw_input())

for case in range(t):
    n, k = (int(x) for x in raw_input().split())
    a = [int(y) for y in raw_input().split()]
    b = [int(z) for z in raw_input().split()]
    answer = compare_arrays(n, k, a, b)
    print answer
