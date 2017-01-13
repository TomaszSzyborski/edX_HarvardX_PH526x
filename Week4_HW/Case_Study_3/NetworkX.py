import networkx as nx

G = nx.Graph()

G.add_node(1)

G.add_nodes_from([2, 3])

G.add_nodes_from(["u", "v"])
print(G)

print(G.nodes())

G.add_edge(1, 2)

G.add_edge("u", "v")
print(G.edges())

#Python adds nodes automatically when creating edges
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
G.add_edge("u", "w")
print(G.edges())
print(G.nodes())

#Removing nodes
G.remove_node(2)
print(G.nodes())
print(G.edges())

G.remove_nodes_from([4, 5])
print(G.nodes())
print(G.edges())

#Removing edges
G.remove_edge(1, 3)
print(G.nodes())
print(G.edges())

G.remove_edges_from([(1, 2), ("u", "v")])
print(G.nodes())
print(G.edges())

#check number of nodes
print(G.number_of_nodes())

#check number of edges
print(G.number_of_edges())

G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(3,4)])
print(G.number_of_nodes(), G.number_of_edges())

