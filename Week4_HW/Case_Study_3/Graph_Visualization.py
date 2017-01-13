import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")

plt.savefig("karate_graph.pdf")

#Pritns dictionary - keys : node IDs, values : degrees of the nodes
print(G.degree())

#Pass node ID
print(G.degree()[33]) #dictionary lookup
print(G.degree(33)) #function lookup

print("nodes")
print(G.number_of_nodes())
print("edges")
print(G.number_of_edges())

print(G.degree(0) is G.degree()[0])