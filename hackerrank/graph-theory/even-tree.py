def cut_tree(count):
    evens = 0
    for j in count:
        if j % 2 == 0:
            evens += 1
    if max(count) % 2 == 0:
        evens -= 1
    return evens

def count_nodes(edges, n, m):
    count = [1 for i in range(n)]
    for i in range(m - 1, -1, -1):
        count[edges[i][1] - 1] += count[edges[i][0] - 1]
    return count

n, m = (int(x) for x in raw_input().split())
edges = []

for edge in range(m):
    ui, uv = (int(y) for y in raw_input().split())
    edges.append([ui, uv])

count = count_nodes(edges, n, m)
answer = cut_tree(count)
print answer
