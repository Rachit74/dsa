from collections import deque

# Graph using Adjacency List
class Graph:
    def __init__(self):
        self.graph = {}   # Stores each node and its neighbors

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    # ---------------- BFS ----------------
    def bfs(self, start):
        visited = set()                 # Keeps track of visited nodes
        queue = deque([start])          # Queue starts with the start node

        while queue:                    # Run until queue becomes empty
            node = queue.popleft()      # Take the first node from queue

            if node not in visited:     # If node not visited yet
                visited.add(node)       # Mark node as visited
                print(node, end=" ")    # Process the node (print here)

                # Add all neighbors of current node to queue
                # They will be visited later in FIFO order
                queue.extend(self.graph[node])

    # ---------------- DFS ----------------
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()             # Initialize visited set once

        visited.add(start)              # Mark current node as visited
        print(start, end=" ")           # Process the node (print here)

        # Go through each neighbor of current node
        for n in self.graph[start]:
            if n not in visited:        # If neighbor not visited
                self.dfs(start=n, visited=visited)  # Go deeper (recursive)

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