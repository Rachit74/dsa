from collections import deque

# Adjacency List

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

    def bfs(self, start):
         visited = set()
         queue = deque([start])

         while queue:
              node = queue.popleft()
              if node not in visited:
                   visited.add(node)
                   print(node, end=" ")
                   queue.extend(self.graph[node])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for n in self.graph[start]:
             if n not in visited:
                  self.dfs(start=n, visited=visited)
        

    def __str__(self):
        return str(self.graph)
    
    
    
g = Graph()
g.add_vertex('A')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'C')
g.add_edge('B', 'F')
g.add_edge('D', 'E')
g.add_edge('D', 'G')
g.add_edge('E', 'H')

print(g)

g.bfs('A')
print("\n")
g.dfs('A')
print("\n")