import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes with labels
G.add_node(1, label="1")
G.add_node(2, label="2")
G.add_node(3, label="3")

# Add edge with label
G.add_edge(1, 2)

# Define positions for nodes
pos = {1: (0, 0), 2: (1, 0), 3: (2, 0)}  # Added position for the third node

# Draw the graph with custom settings
nx.draw(G, pos, with_labels=False, node_color='red', node_size=300)

# Add node labels
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Show the plot
plt.show()
