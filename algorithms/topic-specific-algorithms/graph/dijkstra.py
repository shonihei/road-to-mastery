# Dijkstra's algorithm implemented for a graph represented using a dict of adjacent nodes

class Graph:
    def __init__(self):
        self.g = dict()

    def add(self, s, e, w):
        self.add_aux(s, e, w)
        self.add_aux(e, s, w)
        
    def add_aux(self, s, e, w):
        if s not in self.g:
            self.g[s] = { e:w }
        else:
            self.g[s][e] = w
        
    def __repr__(self):
        out = ""
        for vertex, neighbors in self.g.items():
            sub_out = ""
            for neighbor, weight in neighbors.items():
                sub_out += "\tconnects to {} with weight {}\n".format(neighbor, weight)
            out += "vertex " + str(vertex) + "\n" + sub_out
        return out

    def build_spt_from(self, source):
        if source not in self.g:
            raise KeyError("source must be in graph")
        else:
            # initializing some variables used to keep track
            dist_val = dict() # ideally this would be a min-heap
            for k in self.g:
                if k == source:
                    dist_val[k] = 0
                else:
                    dist_val[k] = float('inf')
            visited = []

            min_node = source
            
            # find min dist
            while len(visited) != len(self.g.keys()):
                # find target
                min_dist = float('inf')
                for k, v in dist_val.items():
                    if k in visited:
                        continue
                    if v < min_dist:
                        min_node = k
                        min_dist = v
                if not min_node:
                    continue
                
                visited.append(min_node)
                neighbors = self.g[min_node]

                for neighbor in neighbors:
                    cur_dist_val = dist_val[neighbor]
                    new_dist_val = dist_val[min_node] + self.g[min_node][neighbor]
                    if new_dist_val < cur_dist_val:
                        dist_val[neighbor] = new_dist_val
            return dist_val
    
def main():
    import json
    g = Graph()
    g.add("A", "B", 7)
    g.add("B", "C", 10)
    g.add("B", "D", 15)
    g.add("C", "A", 9)
    g.add("A", "F", 14)
    g.add("C", "F", 2)
    g.add("C", "D", 11)
    g.add("D", "E", 6)
    g.add("E", "F", 9)
    print(g)
    spt = g.build_spt_from("A")
    print("Shortest distance from A to vertex")
    for k, v in spt.items():
        print("\t{} = {}".format(k, v))
    
if __name__ == "__main__":
    main()

    
