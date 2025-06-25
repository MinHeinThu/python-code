# Edges list (Directed) [Start, end]
"""
This script converts a list of directed edges into an adjacency matrix representation of a graph.

The graph is defined by:
- `node`: The number of nodes in the graph.
- `edges_list`: A list of directed edges where each edge is represented as a list of two elements [start, end].

Steps performed in the script:
1. Print the edges list.
2. Create a mapping from vertex labels to indices.
3. Initialize an adjacency matrix with zeros.
4. Populate the adjacency matrix based on the edges list.
5. Print the adjacency matrix.

Time Complexity:
- Creating the vertex-to-index mapping: O(n), where n is the number of nodes.
- Initializing the adjacency matrix: O(n^2), where n is the number of nodes.
- Populating the adjacency matrix: O(e), where e is the number of edges.
- Overall time complexity: O(n^2 + e).

Space Complexity:
- Space for the vertex-to-index mapping: O(n), where n is the number of nodes.
- Space for the adjacency matrix: O(n^2), where n is the number of nodes.
- Overall space complexity: O(n^2).
"""
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
    ["g","f"]
]

for row in edges_list:
    print(row)

# Convert edges list -> adjacency 

# Before convert we need to bulilt matrix and map
vertex_to_index = {chr(97+i): i for i in range(node)}
for key,val in vertex_to_index.items():
    print(key,val)
M = []
for i in range(node):
    M.append([0]* node)

for row in M:
    print(row)

print()

# if virtex and edge is in the edges list it will show 1 in matrix
for u, v in edges_list:
    M[vertex_to_index[u]][vertex_to_index[v]]= 1

for row in M:
    print(row)