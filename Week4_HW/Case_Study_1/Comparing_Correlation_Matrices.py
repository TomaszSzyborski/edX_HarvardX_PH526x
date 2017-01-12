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
print("Groups:")
print(whisky.head())
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

#plot
plt.figure(figsize=(14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")