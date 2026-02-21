

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v, directed=False):
            self.add_vertex(u)
            self.add_vertex(v)
            self.graph[u].append(v)
            if not directed:
                self.graph[v].append(u)

    def __str__(self):
        return str(self.graph)
    
g1 = Graph()
g1.add_vertex('A')
g1.add_edge('A', 'B')
g1.add_edge('B', 'C')

print(g1)