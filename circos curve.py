import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)
edges = [("A", "D"), ("A", "E"), ("D", "B"), ("D", "C"), ("B", "C")]
G.add_edges_from(edges)

# Set node labels as attributes
node_labels = {"A": "Label_A", "B": "Label_B", "C": "Label_C", "D": "Label_D", "E": "Label_E", "F": "Label_F"}
nx.set_node_attributes(G, node_labels, "label")

# Create a CircosPlot with node colors based on the "label" attribute
circos = CircosPlot(G, node_color="label")

# Display the plot
plt.show()
