import networkx as nx
import nxviz as nv
import matplotlib.pyplot as plt

# Create a directed graph
G_matrix = nx.DiGraph()
G_matrix.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'A')])

# Create a DirectedMatrixPlot
nv.matrix(G_matrix)

# Show the plot
plt.show()