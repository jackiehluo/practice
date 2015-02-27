def play_game(x, y, steps):
    height = max(x)
    width = max(y)
    board = [[0 for b in range(width)] for b in range(height)]
    largest = 0
    for i in range(steps):
        for j in range(x[i]):
            for k in range(y[i]):
                board[j][k] += 1
                if board[j][k] > largest:
                    largest = board[k][k]
    number = sum(c.count(largest) for c in board)
    return number

steps = int(raw_input())
x = []
y = []

for step in range(steps):
    first, second = (int(a) for a in raw_input().split())
    x.append(first)
    y.append(second)

answer = play_game(x, y, steps)
print answer