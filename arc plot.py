import networkx as nx
from nxviz import ArcPlot
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_node(1, label="1")
G.add_node(2, label="2")
G.add_node(3, label="3")
# Add edge with label
G.add_edge(1, 2)
G.add_edge(1, 3)

# Create an ArcPlot with node labels
arcplot = ArcPlot(G, node_color="label")

# Display the plot
plt.show()
