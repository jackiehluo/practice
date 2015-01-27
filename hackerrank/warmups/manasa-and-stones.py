def get_treasure(stones, a, b):
    values = []
    for j in range(stones):
        if (j * a + (stones - j - 1) * b) not in values:
            values.append(j * a + (stones - j - 1) * b)
    values.sort()
    values = map(str, values)
    return values

test_cases = (int)(raw_input())

for i in range(test_cases):
    stones = (int)(raw_input())
    a = (int)(raw_input())
    b = (int)(raw_input())
    treasure = get_treasure(stones, a, b)
    print (" ".join(treasure))