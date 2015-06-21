def fibonacci(a, b, n):
    first = a
    second = b
    for _ in range(3, n + 1):
        cur = first + second ** 2
        first = second
        second = cur
    return cur

a, b, n = (int(x) for x in raw_input().split())
print fibonacci(a, b, n)