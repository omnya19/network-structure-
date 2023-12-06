import networkx as nx
import nxviz as nv
import matplotlib.pyplot as plt

# Create a graph
G_matrix = nx.Graph()
G_matrix.add_node("A")
G_matrix.add_node("B")
G_matrix.add_node("C")
G_matrix.add_edges_from([('A', 'B'), ('A', 'C'),('A','A'),('B','B'),('C','C')])

# Create a MatrixPlot using the functional API
nv.matrix(G_matrix)

# Show the plot
plt.show()
