def find_odd(arr):
    exists = {}
    for n in arr:
        if n in exists.keys():
            exists.pop(n)
        else:
            exists[n] = 1
    for v in exists.keys():
        return v