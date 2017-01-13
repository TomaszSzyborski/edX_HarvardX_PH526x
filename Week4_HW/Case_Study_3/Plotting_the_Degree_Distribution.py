import networkx as nx
from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

def er_graph(N, p):
    """Generate an ER graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

G = er_graph(50, 0.08)
plot_degree_distribution(G)
plt.savefig("hist.pdf")
plt.clf()

G = er_graph(500, 0.08)
plot_degree_distribution(G)
plt.savefig("hist1.pdf")
plt.clf()

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("g3_hist.pdf")
plt.clf()

# error in following code
# D = {1:1, 2:2, 3:3}
# plt.hist(D)
# plt.savefig("D.pdf")
# plt.clf()

plot_degree_distribution(nx.erdos_renyi_graph(100, 0.03))
plot_degree_distribution(nx.erdos_renyi_graph(100, 0.30))
plt.savefig("comparison.pdf")