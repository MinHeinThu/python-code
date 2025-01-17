# Array of Edges (Directed) [Start, end]

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

print(A)

# Convert array of edges -> Ajancency Matrix

M = []
for i in range(n):
    M.append([0] * n)


for u, v in A:
    M[u][v] = 1

    # Uncomment the following line if the graph is undirected
    M[v][u] = 1

print(M)


# Convert Array of Edges -> Adjacency List


from collections import defaultdict

D = defaultdict(list)

for u,v in A:
    D[u].append(v)

    # Uncomment the following line if the graph is underected
    # D[v].append(u)

print(D)

# DFS with Recursion - O(V + E) Where V is the number of nodes and E is the number of edges

def dfs_recursive(node):
    print(node, end= "->")

    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            dfs_recursive(neighbour_node)


source = 0
seen = set()
seen.add(source)
dfs_recursive(source)


# DFS with stack
source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node, end = " ")
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)
print()

# BFS (Queue) = O( V + E )

from collections import deque
source = 0
seen = set()
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node,end=" ")
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)