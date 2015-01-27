def count(sequence, item):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            count += 1
    return count