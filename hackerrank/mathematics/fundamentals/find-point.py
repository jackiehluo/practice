def find_point(px, py, qx, qy):
    x_diff = qx - px
    y_diff = qy - py
    rx = qx + x_diff
    ry = qy + y_diff
    return str(rx) + " " + str(ry)

test_cases = int(raw_input())

for case in range(test_cases):
    px, py, qx, qy = (int(x) for x in raw_input().split())
    point = find_point(px, py, qx, qy)
    print point