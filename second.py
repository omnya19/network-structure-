import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes with labels
G.add_node(1, label="Hugo:id:1")
G.add_node(2, label="Eric:id:2")

# Add edge with label
G.add_edge(1, 2, label="Friendship:date:2016-05-21")

# Draw the graph
pos = {1: (0, 0), 2: (2, 0)}  # Define positions for nodes
nx.draw(G, pos, with_labels=False, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", font_family="sans-serif", edge_color="black")

# Draw labels on nodes
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Draw labels on edges
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw a dotted circle around the nodes
circle = plt.Circle((1, 0), 1.2, color='lightgray', fill=False, linestyle='dotted')
plt.gca().add_patch(circle)

# Show the plot
plt.axis('equal')  # Keep the aspect ratio equal
plt.show()
