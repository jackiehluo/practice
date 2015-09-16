def count_islands(numbers):
    levels, level, count, prev = [0] * 13, 0, 0, numbers[0]
    for cur in numbers[1:]:
        if cur > prev:
            level += 1
            count += 1
            levels[level] = cur
        elif cur < prev:
            while level and cur < levels[level]:
                level -= 1
            if cur > levels[level]:
                level += 1
                count += 1
                levels[level] = cur
        prev = cur
    return count

for _ in range(int(input())):
    d = list(map(int, input().split()))
    k, numbers = d[0], d[1:]
    print(k, count_islands(numbers))