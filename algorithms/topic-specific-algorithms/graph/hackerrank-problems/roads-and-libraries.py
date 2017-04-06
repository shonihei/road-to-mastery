# Not complete => algorithm works but not with large input (time out error)
# Problem : https://www.hackerrank.com/challenges/torque-and-development

import sys

def findNumIslandsRec(graph):
    islands = 0
    visited = []
    islandSizes = []
    # iterate through starting each city
    for startCity in range(len(graph)):
        if startCity in visited:
            continue
        islandSize = dfsIslandTraversal(graph, startCity)
        visited.extend(islandSize)
        islandSizes.append(len(islandSize))
        islands += 1
    return islands, islandSizes

def dfsIslandTraversal(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for n in graph[start] - visited:
        dfsIslandTraversal(graph, next, visited)
    return visited

q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    graph = {x : set() for x in range(n)}
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1) - 1,int(city_2) - 1]
        # Add potential road
        graph[city_1].add(city_2)
        graph[city_2].add(city_1)
    numCities = len(graph)
    if y > x:
        print(numCities * x)
        continue
    numIslands, islandSizes = findNumIslandsRec(graph)

    allLibraryCost = numCities * x
    roadAndLibrary = (numIslands * x) + sum(list(map(lambda size: (size - 1) * y, islandSizes)))
    print(min(allLibraryCost, roadAndLibrary))
