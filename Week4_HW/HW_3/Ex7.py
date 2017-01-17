import pandas as pd
import numpy as np
import networkx as nx

data_filepath = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_974/datasets/'

A1 = np.loadtxt("../Case_Study_3/adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("../Case_Study_3/adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

df  = pd.read_stata(data_filepath + "individual_characteristics.dta")

df1 = df[df["village"] == 1]
df2 = df[df["village"] == 2]

pid1 = pd.read_csv(data_filepath + "key_vilno_1.csv", header=None)
pid2 = pd.read_csv(data_filepath + "key_vilno_2.csv", header=None)

#dictionaries of values from pandas DataFrame

sex1      = pd.Series(df1.resp_gend.values,index=df1.pid).to_dict()
caste1    = pd.Series(df1.caste.values,index=df1.pid).to_dict()
religion1 = pd.Series(df1.religion.values,index=df1.pid).to_dict()

sex2      = pd.Series(df2.resp_gend.values,index=df2.pid).to_dict()
caste2    = pd.Series(df2.caste.values,index=df2.pid).to_dict()
religion2 = pd.Series(df2.religion.values,index=df2.pid).to_dict()

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties, num_ties = 0, 0
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 > n2:   # do not double-count edges!
                if IDs[0][n1] in chars and IDs[0][n2] in chars:
                    if G.has_edge(n1, n2):
                        # Should `num_ties` be incremented?  What about `num_same_ties`?
                        num_ties += 1
                        if chars[IDs[0][n1]] == chars[IDs[0][n2]]:
                            # Should `num_ties` be incremented?  What about `num_same_ties`?
                            num_same_ties += 1
    return (num_same_ties / num_ties)

print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1))
print("Village 1 observed proportion of same religion:", homophily(G1, religion1, pid1))

print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2))
print("Village 2 observed proportion of same religion:", homophily(G2, religion2, pid2))



