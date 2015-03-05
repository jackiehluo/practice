run = True

while run == True:
    n = int(raw_input())
    if n == 0:
        run = False
    else:
        squares = 0
        for i in range(n + 1):
            squares += i ** 2
        print squares