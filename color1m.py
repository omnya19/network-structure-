import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create an undirected graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c']
G.add_nodes_from(nodes)

# Add undirected edges
edges = [('a', 'b'), ('a', 'c')]
G.add_edges_from(edges)

# Add self-loops with a different color
G.add_edge('a', 'a')
G.add_edge('b', 'b')
G.add_edge('c', 'c')

# Get the adjacency matrix
adj_matrix = nx.adjacency_matrix(G, nodelist=nodes).toarray()

# Set different colors for edges and self-loops
edge_colors = np.array(adj_matrix)
np.fill_diagonal(edge_colors, 2)  # Assign a different value for self-loops
cmap=plt.cm.colors.ListedColormap(['white','black','grey'])

# Plot the matrix with different colors for edges and self-loops
plt.imshow(edge_colors, cmap=cmap, interpolation='none', origin='upper')

# Add labels and show the plot
plt.xticks(np.arange(len(nodes)), nodes)
plt.yticks(np.arange(len(nodes)), nodes)
plt.title('Undirected Graph Edge Coloring')
plt.colorbar()
plt.show()
