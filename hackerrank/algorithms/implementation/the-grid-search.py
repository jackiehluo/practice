def search_grid(R, C, G, r, c, g):
    i = 0
    while i < R:
        if g[0] in G[i]:
            j = 0
            p = G[i].find(g[0])
            while j < r and p != -1:
                if p != G[i].find(g[j]):
                    break
                p = G[i].find(g[j])
                i += 1
                j += 1
            if j == r and p != -1:
                return "YES"
        i += 1
    return "NO"

for _ in range(int(raw_input())):
    R, C = map(int, raw_input().split())
    G = []
    for _ in range(R):
        G.append(raw_input())
    r, c = map(int, raw_input().split())
    g = []
    for _ in range(r):
        g.append(raw_input())
    print search_grid(R, C, G, r, c, g)