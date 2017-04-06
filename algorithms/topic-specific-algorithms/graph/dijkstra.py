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
        return str(self.g)

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

            # find min dist
            min_dist = float('inf')
            min_node = self.g.keys()[0]
            for k, v in dist_val.items():
                if v < min_dist:
                    min_node = k
                    min_dist = v
            
        
    
def main():
    g = Graph()
    g.add("A", "B", 2)
    g.add("C", "A", 4)
    print(g)
    g.build_spt_from("A")

if __name__ == "__main__":
    main()

    
