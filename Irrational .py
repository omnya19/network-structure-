import networkx as nx
import matplotlib.pyplot as plt
import random

# Create an empty graph
G = nx.Graph()

# Add 31 nodes
num_nodes = 31
G.add_nodes_from(range(1, num_nodes + 1))

# Add edges randomly
num_edges = 45  # Adjust this based on the number of edges you want
for _ in range(num_edges):
    edge = (random.randint(1, num_nodes), random.randint(1, num_nodes))
    G.add_edge(*edge)

# Use the spring_layout for better node placement
pos = nx.spring_layout(G)

# Draw the graph
nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)

# Display the graph
plt.show()

# Print information about the graph
print("Total number of nodes:", G.number_of_nodes())
print("Total number of edges:", G.number_of_edges())
print("List of all nodes:", list(G.nodes()))
print("List of all edges:", list(G.edges(data=True)))
print("Degree for all nodes:", dict(G.degree()))
print("Total number of self-loops:", G.number_of_selfloops())
print("List of all nodes with self-loops:", list(G.nodes_with_selfloops()))
