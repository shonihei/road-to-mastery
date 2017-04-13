def dijkstra(graph, start):
    dist_val = [float('inf') for vertex in range(len(graph))]
    visited = [False for vertex in range(len(graph))]
    dist_val[start] = 0
    for count in range(len(graph) - 1):
        u = min_dist(dist_val, visited)
        visited[u] = True
        for v, node in enumerate(graph[u]):
            if node != 0 and not visited[v] and dist_val[u] != float('inf') and dist_val[u] + graph[u][v] < dist_val[v]:
                dist_val[v] = dist_val[u] + graph[u][v]
    return dist_val

def min_dist(d, v):
    m = float('inf')
    u = 0
    for i in range(len(d)):
        if not v[i] and d[i] < m:
            m = d[i]
            u = i
    return u

a = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
print(dijkstra(a, 0))
