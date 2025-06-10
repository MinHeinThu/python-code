node = 7
edges_list = [
    ["a","b"],
    ["a","d"],
    ["b","c"],
    ["d","e"],
    ["d","g"],
    ["e","f"],
    ["e","g"],
    ["f","c"],
    ["g","f"],
]

def display_edges(edges_list):
    for edge in edges_list:
        print(f"{edge[0]} -> {edge[1]}") 

# display_edges(edges_list)

for row in edges_list:
    # print(row)
    pass


# Edges list to adjacency matrix

def  edges_to_adjacency_matrix(edges):
    # Initialize adjacency matrix with 0s
    # M = [[0 for _ in range(node)] for _ in range(node)]
    M = []
    for i in range(node):
        M.append([0] * node)
    
    # Map vertices to indices
    vertex = {chr(97+i):i for i in range(node)}

    for v, u in edges:
        M[vertex[v]][vertex[u]] = 1
    
    for row in M:
        print(row)
# edges_to_adjacency_matrix(edges_list)

# Edges_to_adjacency_list
from collections import defaultdict

dic = defaultdict(list)

for v,u in edges_list:
    dic[v].append(u)
print(dic)


# Edges_to_adjacency_list using function
# First set empyt dict
# Loop and if vertex is not in dic
# vertex is empty list
# Append edge into the empty list

def edges_list_to_adjacency_list(adges_list):
    adjacency_list = {}

    for vertex, edge in adges_list:
        if vertex not in adjacency_list:
            adjacency_list[vertex] = []
        adjacency_list[vertex].append(edge)
    for row,col in adjacency_list.items():
        print(f'{row}:{col}')

# edges_list_to_adjacency_list(edges_list)


# DFS with recursively : T, S : (v + e)

def dfs_recursive_graph(source_node):
    print(source_node)
    for neighbour_node in dic[source_node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            dfs_recursive_graph(neighbour_node)

source = 'a'
seen = set()
seen.add(source)




source = 'a'
seen = set()
seen.add(source)
stack = [source]
while stack:
    source_node = stack.pop()
    print(f"visted graph node:{source_node}")
    for neighbour_node in dic[source_node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            stack.append(neighbour_node)
print()

source = 'a'
seen = set() # Set ds is can't not be duplicate
seen.add(source)
def dfs_stack(node):
    stack = [node]
    while stack:
        source_node = stack.pop()
        print("stack dfs",source_node)
        for n_node in dic[source_node]:
            if n_node not in seen:
                seen.add(n_node)
                stack.append(n_node)
    else:
        return -1

dfs_stack(source)
        
# BFS(Queue)
from collections import deque
source = 'a'
seen = set()
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print("Bfs",node)
    for n_node in dic[node]:
        if n_node not in seen:
            seen.add(n_node)
            q.append(n_node)

source = 'a'
seen = set()

def bfs_queue(node):
    q = deque()
    q.append(node)
    while q:
        source_node = q.popleft()
        print(source_node)
        for n_node in dic[source_node]:
            if n_node not in seen:
                seen.add(n_node)
                q.append(n_node)
bfs_queue(source)

