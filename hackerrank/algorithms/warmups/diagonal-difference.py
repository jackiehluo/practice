n = int(raw_input())
numbers = []

for _ in range(n):
    line = [int(x) for x in raw_input().split()]
    numbers.append(line)

first_ind = 0
first_sum = 0
second_ind = n - 1
second_sum = 0

for row in numbers:
    first_sum += row[first_ind]
    second_sum += row[second_ind]
    first_ind += 1
    second_ind -= 1

print abs(first_sum - second_sum)