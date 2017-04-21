# task: given a directed graph, design an algorithm to find out whether there
#       is a route between two nodes
# assumption: graph is represented using an adjancency matrix

def route_between_nodes(g, a, b):
    visited = [False for i in range(len(g))]
    q = [a]
    while q:
        cur_node = q.pop(0)
        visited[cur_node] = True
        if cur_node == b:
            return True
        else:
            for neighbor, val in enumerate(g[cur_node]):
                if val != 0 and not visited[neighbor]:
                    q.append(neighbor)
    return False

g = [[0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0]]
print(route_between_nodes(g, 0, 4))
