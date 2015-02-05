def light_bulbs(bulbs):
    patterns = (2 ** bulbs) - 1
    return str(patterns % (10 ** 5))

test_cases = int(raw_input())

for case in range(test_cases):
    bulbs = int(raw_input())
    answer = light_bulbs(bulbs)
    print answer