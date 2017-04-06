class Graph:
    def __init__(self):
        self.graph = dict()
        self.num_vertices = 0
        self.num_edges = 0
        self.vertex_list = []

    def __repr__(self):
        f = "{}'s neighbors : {}"
        out_string = ""
        for node, neighbors in self.graph.items():
            s = ""
            for neighbor, dist in neighbors.items():
                s += neighbor + "[ {} ]".format(dist) + ", "
            out_string += f.format(node, s) + "\n"
        return out_string

    def add_edge(self, start, end, weight=1):
        if start not in self.vertex_list:
            self.vertex_list.append(start)
        if end not in self.vertex_list:
            self.vertex_list.append(end)

        # assumes undirected graph
        if start not in self.graph:
            self.graph[start] = { end: weight }
        else:
            self.graph[start][end] = weight
        if end not in self.graph:
            self.add_edge(end, start, weight)

    def is_disjoint(self):
        visited = []

        # arbitrary starting point
        stack = [self.vertex_list[0]]

        while stack:
            cur_vertex = stack.pop()
            visited.append(cur_vertex)

            cur_neighbors = self.graph[cur_vertex]
            for neighbor in cur_neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

        if len(visited) != len(self.vertex_list):
            return True
        return False

def main():
    g = Graph()
    s = "SA2 SB5 AF1 AC6 BD2 CD2 DG4 DE3 FG10 GE16"
    parsed_string = s.split(' ')
    for i in parsed_string:
        g.add_edge(i[0], i[1], i[2:])
    print(g)
    print("\tis the graph disjoint? : {}".format(g.is_disjoint()))

    r = Graph()
    s = "SA2 SB4 AB9 CD3 DE10 EC1"
    parsed_string = s.split(' ')
    for i in parsed_string:
        r.add_edge(i[0], i[1], i[2:])
    print(r)
    print("\tis the graph disjoint? : {}".format(r.is_disjoint()))

if __name__=="__main__":
    main()
