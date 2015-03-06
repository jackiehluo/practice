def find_moves(n, candies):
    goal = sum(candies) / n
    moves = 0
    for i in candies:
        if i < goal:
            moves += goal - i
    print moves

run = True

while run == True:
    n = int(raw_input())
    if n == -1:
        run = False
    else:
        candies = []
        for p in range(n):
            candies.append(int(raw_input()))
        if sum(candies) % n == 0:
            find_moves(n, candies)
        else:
            print "-1"
