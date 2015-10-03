arr = [25, -10, 0, 501, -2000, 1010]

def pair(arr):
    arr = set(arr)
    for n in arr:
        if 1000 - n in arr:
            return True
    return False