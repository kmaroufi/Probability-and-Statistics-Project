import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()


g.add_node(2)
g.add_node(5)
g.add_node(8)

g.add_edge(2, 5)

# nx.draw_circular(g)
# nx.draw(g)
# plt.show()

G=nx.complete_graph(5)
A=nx.to_agraph(G)
H=nx.from_agraph(A)