def find_minimax(numbers, p, q):
    mins = []
    for i in range(p, q + 1):
        minimum = max(numbers)
        for j in numbers:
            if abs(j - i) < minimum:
                minimum = abs(j - i)
        mins.append(minimum)
    minimax = max(mins)
    index = min([k for k, l in enumerate(mins) if l == minimax])
    return range(p, q + 1)[index]

n = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
p, q = (int(y) for y in raw_input().split())
answer = find_minimax(numbers, p, q)
print answer
