def check_planes(points):
    for i in range(3):
        if points[0][i] == points[1][i] == points[2][i] == points[3][i]:
            return "YES"
    return "NO"

test_cases = int(raw_input())

for case in range(test_cases):
    points = []
    for point in range(4):
        points.append([int(a) for a in raw_input().split()])
    answer = check_planes(points)
    print answer