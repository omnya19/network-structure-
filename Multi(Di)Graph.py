import networkx as nx
import matplotlib.pyplot as plt

# Create a directed multigraph
G = nx.MultiDiGraph()

# Add nodes with labels
G.add_node(1, label="1")
G.add_node(2, label="2")

# Add edge with label
G.add_edge(1, 2)


# Define layout (optional)
pos = {1: (0, 0), 2: (1, 0)}

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", edge_color='gray', width=2)
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)
# Display the graph
plt.show()
