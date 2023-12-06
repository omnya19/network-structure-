import networkx as nx
import matplotlib.pyplot as plt

# Create a directed multigraph
G = nx.MultiDiGraph()

# Add nodes
G.add_nodes_from([1, 2])

# Add multiple directed edges between nodes with weights
G.add_edge(1, 2, weight=2)
G.add_edge(1, 2, weight=3)

# Define layout (optional)
pos = {1: (0, 0), 2: (1, 0)}

# Get edge weights for edges with weight 2
edge_labels = {(i, j): d['weight'] for i, j, d in G.edges(data=True) if d['weight'] == 2}

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", edge_color='gray', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Display the graph
plt.show()
