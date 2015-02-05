def find_routes(routes):
    choices = 1
    for i in range(len(routes)):
        choices *= routes[i]
    return str(choices % 1234567)

test_cases = int(raw_input())

for case in range(test_cases):
    towns = int(raw_input())
    routes = [int(x) for x in raw_input().split()]
    answer = find_routes(routes)
    print answer