def cut_board(m, n, y, x):
    y_dict = [[i, "y"] for i in y]
    x_dict = [[j, "x"] for j in x]
    z = sorted(y_dict + x_dict, reverse = True)
    y_parts = 1
    x_parts = 1
    cost = 0
    for k in range(len(z)):
        if z[k][1] == "y":
            cost += z[k][0] * x_parts
            y_parts += 1
        if z[k][1] == "x":
            cost += z[k][0] * y_parts
            x_parts += 1
    print cost % 1000000007
        
t = int(raw_input())

for case in range(t):
    m, n = (int(a) for a in raw_input().split())
    y = [int(b) for b in raw_input().split()]
    x = [int(c) for c in raw_input().split()]
    cut_board(m, n, y, x)
