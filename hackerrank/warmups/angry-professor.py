def cancel_class(k, arrivals):
    students = 0
    for time in arrivals:
        if time <= 0:
            students += 1
    if students >= k:
        return "NO"
    else:
        return "YES"

test_cases = int(raw_input())

for case in range(test_cases):
    n, k = (int(x) for x in raw_input().split())
    arrivals = [int(y) for y in raw_input().split()]
    answer = cancel_class(k, arrivals)
    print answer