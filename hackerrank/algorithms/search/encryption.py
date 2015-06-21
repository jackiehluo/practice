from math import floor, ceil, sqrt

def split_text(text):
    length = len(text)
    rows = int(floor(sqrt(length)))
    columns = int(ceil(sqrt(length)))
    grid = []
    first = 0
    last = columns
    for x in range(rows + 1):
        grid.append(text[first:last])
        first += columns
        last += columns
    return grid

def encrypt(text, grid):
    length = len(text)
    rows = int(floor(sqrt(length)))
    columns = int(ceil(sqrt(length)))
    encryption = ""
    for i in range(columns):
        for j in range(rows + 1):
            if i < len(grid[j]):
                encryption += grid[j][i]
        encryption += " "
    return encryption

text = list(raw_input())
grid = split_text(text)
encryption = encrypt(text, grid)
print encryption