def quicksort(a, s):
    if s == 1 or s == 0:
        if s == 0:
            return [None]
        else:
            return [a[0]]
    p = a[0]
    first = []
    last = []
    for x in range(s):
        if a[x] < p:
            first.append(a[x])
        elif not a[x] is p:
            last.append(a[x])
    f = quicksort(first, len(first))
    l = quicksort(last, len(last))
    if f == [None]:
        temp = [p] + l
    elif l == [None]:
        temp = f + [p]
    else:
        temp = f + [p] + l
    print(" ".join(map(str, temp)))
    return temp

length = int(raw_input())
numbers = [int(x) for x in raw_input().split()]
quicksort(numbers, length)
