# Graph implementation using oop

class Graph:
    def __init__(self, directed = False):
        self.add_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.add_list:
            self.add_list[vertex] = []
        else:
            return
    
    def add_edge(self, u, v):
        if u not in self.add_list:
            self.add_vertex(u)
        if v not in self.add_list:
            self.add_vertex(v)

        self.add_list[u].append(v)
        if not self.directed:
            self.add_list[v].append(u)

    def display(self):
        for u, v in self.add_list.items():
            print(u, v)

graph = Graph(directed = False)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

graph.display()