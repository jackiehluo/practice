def pairs(k, numbers):
    a = set(numbers)
    return sum(1 for i in numbers if i - k in a)

n, k = (int(x) for x in raw_input().split())
numbers = [int(y) for y in raw_input().split()]
print pairs(k, numbers)