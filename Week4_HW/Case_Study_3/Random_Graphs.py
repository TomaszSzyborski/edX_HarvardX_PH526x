import networkx as nx
from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

#coinflip
bernoulli.rvs(p=0.2)

coin_flips=[]
for i in range(100):
    coin_flips.append(bernoulli.rvs(p=0.2))

print(np.array(coin_flips) == 1)

N = 20
p = 0.2

# Create empty graph
# add all N nodes in the graph
# loop over all pairs of nodes
    # add an edge with probability p

def er_graph(N, p):
    """Generate an ER graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

print(er_graph(N, p))

nx.draw(er_graph(50, 0.08), node_size=40,node_color="gray")
plt.savefig("er1.pdf")
plt.clf()

nx.draw(er_graph(10, 1), node_size=40,node_color="gray")
plt.savefig("er2.pdf")
plt.clf()

nx.draw(er_graph(10, 0), node_size=40,node_color="gray")
plt.savefig("er3.pdf")
plt.clf()