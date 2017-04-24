# task: given a graph, find the shortest paths between every pair of nodes using the floyd warshall algorithm

def floyd_warshall(graph):
    dist = [[x for x in y] for y in graph]
    for k in range(len(graph)):
        for src in range(len(graph)):
            for dst in range(len(graph)):
                dist[src][dst] = min(dist[src][dst], dist[src][k] + dist[k][dst])
    return dist

def print_result(dist):
    for vertex, adjacent in enumerate(dist):
        print("path from {} to:".format(vertex))
        for dst, dist in enumerate(adjacent):
            print("\t{} costs {}".format(dst, dist))
        print('')
        
INF = float('inf')
g = [[0, 5, 1, 10, INF],
     [5, 0, INF, 7, INF],
     [1, INF, 0, 2, 8],
     [10, 7, 2, 0, INF],
     [INF, INF, 8, INF, 0]]
print_result(floyd_warshall(g))
