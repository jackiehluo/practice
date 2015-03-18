def swap(n, k, numbers):
    for j in range(n):
        if numbers[j] != n - j:
            p = numbers.index(n - j)
            t = numbers[j]
            numbers[j] = n - j
            numbers[p] = t
            k -= 1
            if k == 0:
                break
    return numbers

n, k = (int(x) for x in raw_input().split())
numbers = [int(y) for y in raw_input().split()]
print " ".join(map(str, swap(n, k, numbers)))