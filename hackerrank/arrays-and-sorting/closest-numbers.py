def find_closest_numbers(size, numbers):
    pairs = []
    minimum = numbers[size - 1]
    for i in range(size - 1):
        if numbers[i + 1] - numbers[i] < minimum:
            minimum = numbers[i + 1] - numbers[i]
    for i in range(size - 1):
        if numbers[i + 1] - numbers[i] == minimum:
            pairs.append(numbers[i + 1])
            pairs.append(numbers[i])
    pairs.sort()
    print ' '.join(map(str, pairs))

size = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
numbers.sort()
pairs = find_closest_numbers(size, numbers)