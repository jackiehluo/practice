m = int(raw_input())
m_list = set(map(int, raw_input().split()))
n = int(raw_input())
n_list = set(map(int, raw_input().split()))

diff = set()
diff.update(m_list.difference(n_list))
diff.update(n_list.difference(m_list))

for v in sorted(diff):
    print v
