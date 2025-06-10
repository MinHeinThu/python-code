# Graph

class Graph:
    def __init__(self, directed = False):
        self.edges_list = {}
        self.directed = directed

    
    def add_verted(self, vertex):
        if vertex not in self.edges_list:
            self.edges_list[vertex] = []
        else:
            return
        
    def add_edge(self, u, v):
        if u not in self.edges_list:
            pass

import numpy as np