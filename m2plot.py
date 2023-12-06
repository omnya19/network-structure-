import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a directed graph
G_matrix = nx.DiGraph()
G_matrix.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'A')])

# Get the adjacency matrix
adj_matrix = nx.adjacency_matrix(G_matrix).toarray()

# Apply custom shape to the matrix
shape_matrix = np.zeros_like(adj_matrix, dtype=float)
shape_matrix[adj_matrix.nonzero()] = 1.0  # Set non-zero values to 1.0
cmap=plt.cm.colors.ListedColormap(['white','black'])
# Create a custom matrix plot using matplotlib
plt.imshow(shape_matrix, cmap=cmap, interpolation='none', origin='upper')

# Add labels and show the plot
plt.xticks(np.arange(len(G_matrix.nodes())), G_matrix.nodes())
plt.yticks(np.arange(len(G_matrix.nodes())), G_matrix.nodes())
plt.title('Custom Matrix Layout')
plt.colorbar()
plt.show()
