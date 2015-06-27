n, m = map(int, raw_input().split())
numbers = list(map(int, raw_input().split()))
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))
happiness = 0

for v in numbers:
    if v in a:
        happiness += 1
    elif v in b:
        happiness -= 1

print happiness