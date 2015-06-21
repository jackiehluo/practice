def count_values(length, numbers, counts):
    for i in range(length):
        number = numbers[i]
        counts[number] += 1
    print ' '.join(map(str, counts))

length = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
numbers.sort()
counts = [0] * 100
count_values(length, numbers, counts)