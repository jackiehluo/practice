import sys

def present_before(arr):
    bits = ""
    prev = set()
    for num in arr:
        if num in prev:
            bits += "1"
        else:
            bits += "0"
        prev.add(num)
    return bits

def present_after(arr):
    bits = ""
    later = arr[1:]
    for num in range(len(arr)):
        if arr[num] in later:
            bits += "1"
        else:
            bits += "0"
        if num < len(arr) - 1:
            later.pop(0)
    return bits

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    val = int(sys.stdin.readline())
    arr.append(val)

print present_before(arr)
print present_after(arr)