def decrypt(col, string):
    grid = []
    message = ""
    for i in range(0, len(string) / col):
        letters = string[i * col:i * col + col]
        if i % 2 == 0:
            grid.append(letters)
        else:
            grid.append(letters[::-1])
    for j in range(col):
        for k in range(len(grid)):
            message += grid[k][j]
    return message

run = True

while run == True:
    col = int(raw_input())
    if col == 0:
        run = False
    else:
        string = raw_input()
        answer = decrypt(col, string)
        print answer