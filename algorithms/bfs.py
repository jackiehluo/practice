def bfs(graph, root):
    visited, queue = set(), [root]
    while queue:
        cur = queue.pop(0)
        visited.add(cur)
        for n in graph[cur]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited

graph = {'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])}

print(bfs(graph, 'A'))