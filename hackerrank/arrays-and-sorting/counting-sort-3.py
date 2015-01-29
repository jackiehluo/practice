def count_values(length, numbers, counts):
    less = 0
    for i in range(length):
        value = numbers[i]
        less += 1
        counts[value] = less
    print ' '.join(map(str, counts))

length = int(raw_input())
numbers = []

for x in range(length):
    number, word = raw_input().split()
    numbers.append(int(number))
    
numbers.sort()
counts = [length] * 100
count_values(length, numbers, counts)