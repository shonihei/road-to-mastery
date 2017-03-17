# Problem : https://www.hackerrank.com/challenges/journey-to-the-moon

N, P = list(map(int, input().strip().split(' ')))
d = {n : [] for n in range(N)}
for p in range(P):
   pair = list(map(int, input().strip().split(' ')))
   d[pair[0]].append(pair[1])
   d[pair[1]].append(pair[0])

graphs = []
visited = []
for k in d:
    if k not in visited:
        q = [k]
        graph = set()
        while len(q) != 0:
            n = q.pop()
            graph.add(n)
            visited.append(n)
            for c in d[n]:
                if c not in visited:
                    q.append(c)
                    visited.append(c)
        graphs.append(graph)

pairs = 0
for country in graphs:
    count = len(country)
    N -= count
    pairs += N * count
print(pairs)
