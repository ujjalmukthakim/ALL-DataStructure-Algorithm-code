from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node in visited:
            continue

        visited.add(node)
        print(node)

        for nei in graph[node]:
            if nei not in visited:
                q.append(nei)