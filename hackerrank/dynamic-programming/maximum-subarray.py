def max_subarray(n, numbers):
    return str(contiguous(n, numbers)) + " " + str(noncontiguous(numbers))

def contiguous(n, numbers):
    p = False
    cur = 0
    best = 0
    for i in range(n):
        v = cur + numbers[i]
        if v > 0:
            cur = v
            p = True
        else:
            cur = 0
        if cur > best:
            best = cur
    if p == False:
        best = max(numbers)
    return best
    
def noncontiguous(numbers):
    p = False
    best = 0
    for j in numbers:
        if j > 0:
            p = True
            best += j
    if p == False:
        best = max(numbers)
    return best

t = int(raw_input())

for _ in range(t):
    n = int(raw_input())
    numbers = [int(x) for x in raw_input().split()]
    print max_subarray(n, numbers)