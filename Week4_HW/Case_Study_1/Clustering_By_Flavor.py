from sklearn.cluster.bicluster import SpectralCoclustering
import pandas as pd
import numpy as np

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

#extracting flavors from whisky data frame
flavors = whisky.iloc[:,2:14]

#pairwise correlation of columns in flavors
corr_flavours = pd.DataFrame.corr(flavors)
corr_whisky = pd.DataFrame.corr(flavors.transpose())


model = SpectralCoclustering(n_clusters=6, random_state=0)

model.fit(corr_whisky)
#print(model.rows_)

#how many observations belong to each cluster
cluster_belongings = np.sum(model.rows_, axis=1) #axis = 0 => rows, axis = 1 => columns
print(cluster_belongings)

how_many_observations = np.sum(model.rows_, axis=0)
print(how_many_observations)

observations_to_clusters = model.row_labels_
print(observations_to_clusters)