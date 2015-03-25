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
    quicksort(ar, start, pivot_index - 1)
    quicksort(ar, pivot_index + 1, end)

def swap(ar, a, b):
    global q_count
    q_count += 1
    if a == b:
        return
    temp = ar[a]
    ar[a] = ar[b]
    ar[b] = temp

def insertion_sort(ar, n):
    global i_count
    for i in range(1, n):
        number = ar[i]
        previous = i - 1
        while previous >= 0 and ar[previous] > number:
            i_count += 1
            ar[previous + 1] = ar[previous]
            previous = previous - 1
        ar[previous + 1] = number

n = int(raw_input())
ar1 = [int(x) for x in raw_input().split()]
ar2 = list(ar1)
q_count, i_count = 0, 0
global q_count
global i_count
quicksort(ar1, 0, n - 1)
insertion_sort(ar2, n)
print i_count - q_count