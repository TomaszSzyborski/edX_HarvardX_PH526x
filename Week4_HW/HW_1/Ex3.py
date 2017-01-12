import pandas as pd
import numpy as np
from sklearn.cluster.bicluster import SpectralCoclustering
import matplotlib.pyplot as plt

#Load whisky
whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

#extracting flavors from whisky data frame
flavors = whisky.iloc[:,2:14]

#pairwise correlation of columns in flavors
corr_flavours = pd.DataFrame.corr(flavors)
corr_whisky = pd.DataFrame.corr(flavors.transpose())

#Create model
model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)

#Extract the labels
whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)

#Reorder the rows in increasing order by group labels
whisky = whisky.ix[np.argsort(model.row_labels_)]
print("Reordered:")
print(whisky.head())

#Reshuffle the indexes
whisky = whisky.reset_index(drop=True)
#Recalculation of correlation matrix
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
#truning correlations into numpy array
correlations = np.array(correlations)

cluster_colors = ["red", "orange", "green", "blue", "purple", "gray"]
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]
region_colors = {k:v for k, v in zip(regions, cluster_colors)}

distilleries = list(whisky.Distillery)
correlation_colors = []


distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i][j]<0.7:                     # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if whisky.Group[i] == whisky.Group[j]:                 # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.