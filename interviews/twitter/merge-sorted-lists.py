def merge_sorted(a, b):
    c = []
    ind_a, ind_b = 0, 0
    while ind_a < len(a) and ind_b < len(b):
        if a[ind_a] < b[ind_b]:
            c.append(a[ind_a])
            ind_a += 1
        else:
            c.append(b[ind_b])
            ind_b += 1
    return c + a[ind_a:] + b[ind_b:]