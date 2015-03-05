digits = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6, 4, 6],
        [5, 5, 5, 5],
        [6, 6, 6, 6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1, 9, 1]]

t = int(raw_input())

for case in range(t):
    a, b = (int(x) for x in raw_input().split())
    a %= 10
    rem = b % 4
    if rem == 0:
        if b == 0:
            print "1"
        else:
            print digits[a][3]
    else:
        print digits[a][rem - 1]