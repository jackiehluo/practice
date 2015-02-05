def draw_socks(pairs):
    if pairs == 1:
        draws = 2
    elif pairs > 1:
        draws = pairs + 1
    return draws

test_cases = int(raw_input())

for case in range(test_cases):
    pairs = int(raw_input())
    answer = draw_socks(pairs)
    print answer