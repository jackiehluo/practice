def quicksort(ar, start, end):
    if start >= end:
        return
    pivot = ar[end]
    index = start - 1
    for i in range(start, end):
        if ar[i] < pivot:
            swap(ar, i, index + 1)
            index += 1
    pivot_index = index + 1
    swap(ar, end, pivot_index)
    print ' '.join(list(map(str, ar)))
    quicksort(ar, start, pivot_index - 1)
    quicksort(ar, pivot_index + 1, end)

def swap(ar, a, b):
    if a == b:
        return
    temp = ar[a]
    ar[a] = ar[b]
    ar[b] = temp

n = int(raw_input())
ar = [int(x) for x in raw_input().split()]
quicksort(ar, 0, n - 1)