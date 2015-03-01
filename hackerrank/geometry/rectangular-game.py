steps = int(raw_input())
x = []
y = []

for step in range(steps):
    first, second = (int(a) for a in raw_input().split())
    x.append(first)
    y.append(second)

answer = min(x) * min(y)
print answer
