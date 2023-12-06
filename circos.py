import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
G.add_nodes_from(nodes)

# Add undirected edges
edges = [('a', 'e'), ('a', 'd'), ('b', 'd'), ('c', 'd'), ('b', 'c')]
G.add_edges_from(edges)

# Draw the graph
pos = nx.circular_layout(G)
labels = nx.get_edge_attributes(G, 'label')  # Get edge labels

nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
