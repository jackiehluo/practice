def build_list(n, s):
    combinations = list(s)
    index = [0, 0]
    for i in range(1, n - 1):
        index = [index[1], len(combinations)]
        for j in combinations[index[0]:]:
            for k in s:
                if j < k and k not in j and ''.join(sorted(j + k)) not in combinations:
                    combinations.append(j + k)
    combinations.append("".join(map(str, s)))
    answer = sorted(combinations)
    return answer

test_cases = int(raw_input())

for case in range(test_cases):
    n = int(raw_input())
    s = list(raw_input())
    answer = build_list(n, s)
    for x in range(len(answer)):
        print answer[x]