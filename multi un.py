import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected multigraph
G = nx.MultiGraph()

# Add nodes
G.add_nodes_from([1, 2, 3])

# Add multiple undirected edges between nodes
G.add_edge(1, 2)
G.add_edge(1, 2)
G.add_edge(3, 2)
G.add_edge(1, 3)

# Define layout (optional)
pos = nx.circular_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color='black')

# Display the graph
plt.show()
