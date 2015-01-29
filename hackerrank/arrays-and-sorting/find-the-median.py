def find_median(size, numbers):
    middle = (size / 2)
    median = numbers[middle]
    return median

size = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
numbers.sort()
answer = find_median(size, numbers)
print answer