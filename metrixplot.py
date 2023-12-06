import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes
nodes = ['a', 'b', 'c']
G.add_nodes_from(nodes)

# Add undirected edges
edges = [('a', 'b'), ('a', 'c')]
G.add_edges_from(edges)

# Draw the graph
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', edge_color='black', linewidths=1, alpha=0.7)

plt.show()
