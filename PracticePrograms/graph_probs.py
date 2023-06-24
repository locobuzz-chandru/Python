from collections import deque


# Write a Python program to create an un-directed graph using an adjacency list.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node in self.graph:
            return f'{node} is already present in the graph'
        self.graph[node] = []

    def add_edge_unweighted(self, node1, node2):
        if node1 not in self.graph:
            return f'{node1} is not present in the graph'
        elif node2 not in self.graph:
            return f'{node2} is not present in the graph'
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Write a Python program to perform a depth-first search (DFS) traversal on an undirected graph.
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph[node])

    # Write a Python program to perform a breadth-first search (BFS) traversal on an undirected graph.
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        print(start, end=' ')
        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Write a Python program to check if a given directed graph is cyclic.
    def _cyclic(self, vertex, visited, rec_stack):
        visited.add(vertex)
        rec_stack.add(vertex)
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                if self._cyclic(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(vertex)
        return False

    def is_cyclic(self):
        visited = set()
        rec_stack = set()
        for vertex in self.graph:
            if vertex not in visited:
                if self._cyclic(vertex, visited, rec_stack):
                    return True
        return False


if __name__ == '__main__':
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    # print(g.graph)
    g.add_edge_unweighted("A", "B")
    g.add_edge_unweighted("A", "C")
    g.add_edge_unweighted("B", "D")
    g.add_edge_unweighted("C", "D")
    print(g.graph)
    # g.bfs('A')
    # print()
    # g.dfs('A')
    # print()
    print(g.is_cyclic())
