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

# --- Define the graph ---
# This is an adjacency list representation
# A is connected to B and C
# B is connected to D and E
# C is connected to F
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# --- Run the BFS ---
if __name__ == "__main__":
    print("Starting BFS traversal from node 'A':")
    bfs(graph, 'A')