def count_steps(heights):
    line, steps = [], 0
    for h in heights:
        i = 0
        while i < len(line) and h > line[i]:
            i += 1
        line.insert(i, h)
        steps += len(line) - 1 - i
    return steps

for _ in range(int(input())):
    d = list(map(int, input().split()))
    k, heights = d[0], d[1:]
    print(k, count_steps(heights))
