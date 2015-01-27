def check_lane(highway, entry, exit):
    minimum = 3
    for i in range(entry, exit + 1):
        if highway[i] < minimum:
            minimum = highway[i]
    return minimum

length, test_cases = (int(x) for x in raw_input().split())
highway = [int(y) for y in raw_input().split()]

for i in range(test_cases):
    entry, exit = (int(z) for z in raw_input().split())
    vehicle_type = check_lane(highway, entry, exit)
    print vehicle_type