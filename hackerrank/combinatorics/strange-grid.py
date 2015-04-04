def strange_grid(r, c):
    if r % 2 == 0:
        return (c * 2 - 1) + 10 * (r / 2 - 1)
    else:
        return (c * 2 - 2) + 10 * ((r - 1) / 2)

r, c = (int(x) for x in raw_input().split())
print strange_grid(r, c)