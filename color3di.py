import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create an undirected graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c']
G.add_nodes_from(nodes)

# Add undirected edges
G.add_edge('a', 'b')
G.add_edge('a', 'c')
G.add_edge('b', 'c')

# Add an undirected edge between 'a' and 'c' only once
G.add_edge('a', 'c')

# Add an undirected edge between 'c' and 'b' only once
G.add_edge('c', 'b')

# Get the adjacency matrix
adj_matrix = nx.adjacency_matrix(G, nodelist=nodes).toarray()

# Set the same color for both edges 'a' to 'b' and 'b' to 'a'
adj_matrix[0, 1] = 1  # Set the color value for the edge 'a' to 'b'
adj_matrix[1, 0] = 1  # Set the same color value for the edge 'b' to 'a'

# Set a different color for edges 'a' to 'c' and 'c' to 'a'
adj_matrix[0, 2] = 2  # Set the color value for the edge 'a' to 'c'
adj_matrix[2, 0] = 2  # Set the same color value for the edge 'c' to 'a'

# Set a different color for edges 'c' to 'b' and 'b' to 'c'
adj_matrix[1, 2] = 3  # Set the color value for the edge 'c' to 'b'
adj_matrix[2, 1] = 3  # Set the same color value for the edge 'b' to 'c'
cmap=plt.cm.colors.ListedColormap(['grey','black','yellow','white'])

# Plot the matrix with different colors for edges
plt.imshow(adj_matrix, cmap=cmap, interpolation='none', origin='upper', vmin=0, vmax=3)

# Add labels and show the plot
plt.xticks(np.arange(len(nodes)), nodes)
plt.yticks(np.arange(len(nodes)), nodes)
plt.title('Undirected Graph Edge Coloring')
plt.colorbar(ticks=[0, 1, 2, 3], label='Edge Color')
plt.show()
