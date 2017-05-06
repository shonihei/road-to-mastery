# task: given a directed ascyclic graph, write an algorithm to print the nodes such that
#       if there's an edge u, v then vertex u is printed before vertex v

def topological_sort(g):
    global q
    global d
    # initialize queue
    q = []
    # calculates in-degree
    d = {u : 0 for u in g}
    for u in g:
        for v in g[u]:
            d[v] += 1

    # insert any node with 0 in-degree vertex
    for u in d:
        if d[u] == 0:
            q.append(u)

    # initialize output list
    out = []

    # while the queue is not empty
    while q:
        # current node (initially it picks nodes with 0 in-degree)
        u = q.pop(0)
        out.append(u)

        # decrement in-degree vertex count
        # this essentially mimics deleting a node 
        for v in g[u]:
            d[v] -= 1
            if d[v] == 0:
                q.append(v)

    # no cycle
    if len(out) == len(g):
        return out
    # there was a cycle
    return []

dependencies = {
    "A": ["C"],
    "B": ["E"],
    "C": ["B", "D", "E"],
    "D": ["E"],
    "E": ["F", "G"],
    "F": ["H"],
    "G": ["H"],
    "H": []
}

print(topological_sort(dependencies))
