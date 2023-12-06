import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
# Add nodes with labels
G.add_node(1, label="1")
G.add_node(2, label="2")

# Add edge with label
G.add_edge(1, 2)


# Define a custom position for the nodes
pos = {1: (0, 0), 2: (1, 0)}

# Set the size of the figure (in inches)
fig, ax = plt.subplots(figsize=(5, 5))
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)
# Draw the directed graph with custom settings
nx.draw(G, pos=pos, with_labels=False, node_color='skyblue', node_size=1000, width=3, ax=ax, arrowsize=20)

# Show the plot
plt.show()
