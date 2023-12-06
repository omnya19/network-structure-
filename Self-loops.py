import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add a single node
G.add_node(1)

# Add a self-loop to the node
G.add_edge(1, 1)

# Define layout (optional)
pos = {1: (0, 0)}  # Manually set position for the node

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=300, node_color="skyblue", edge_color="black", node_shape="o", connectionstyle='arc3,rad=0.1')

# Display the graph
plt.show()
