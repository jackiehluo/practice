def find_substrings(a, b):
    length = len(a)
    a_substrings = [a[i:j + 1] for i in xrange(length) for j in xrange(i, length)]
    b_substrings = [b[k:l + 1] for k in xrange(length) for l in xrange(k, length)]
    return a_substrings, b_substrings

def max_length(p_subs, q_subs, mismatches):
    length = 0
    for y in range(len(p_subs)):
        differences = 0
        for z in range(len(p_subs[y])):
            if p_subs[y][z] != q_subs[y][z]:
                differences += 1
        if differences == mismatches and len(p_subs[y]) > length:
            length = len(p_subs[y])
    return length
    
test_cases = int(raw_input())

for case in range(test_cases):
    s, p, q = (x for x in raw_input().split())
    mismatches = int(s)
    p_subs, q_subs = find_substrings(p, q)
    answer = max_length(p_subs, q_subs, mismatches)
    print answer