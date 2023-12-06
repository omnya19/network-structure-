import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create an undirected graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c']
G.add_nodes_from(nodes)

# Add undirected edges
edges = [('a', 'b'), ('a', 'c'), ('c', 'a')]
G.add_edges_from(edges)

# Get the adjacency matrix
adj_matrix = nx.adjacency_matrix(G, nodelist=nodes).toarray()
cmap = plt.cm.colors.ListedColormap(['white', 'black'])

# Plot the matrix
plt.imshow(adj_matrix, cmap=cmap)

# Add labels and show the plot
plt.xticks(np.arange(len(nodes)), nodes)
plt.yticks(np.arange(len(nodes)), nodes)
plt.title('Undirected Graph Adjacency Matrix')
plt.colorbar()
plt.show()
