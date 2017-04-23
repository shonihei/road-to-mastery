# task: given a directed ascyclic graph, write an algorithm to print the nodes such that
#       if there's an edge u, v then vertex u is printed before vertex v

def topological_sort(g):
    q = []
    d = {u : 0 for u in g}
    for u in g:
        for v in g[u]:
            d[v] += 1

    for u in d:
        if d[u] == 0:
            q.append(u)

    out = []
    while q:
        u = q.pop(0)
        out.append(u)

        for v in g[u]:
            d[v] -= 1
            if d[v] == 0:
                q.append(v)
    if len(out) == len(g):
        return out
    return []

dependencies = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

print(topological_sort(dependencies))
