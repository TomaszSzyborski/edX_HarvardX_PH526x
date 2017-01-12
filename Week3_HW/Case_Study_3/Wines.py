import pandas as pd
import numpy as np
import random

data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")


numeric_data = data.drop("color", 1)

numeric_data = (numeric_data - np.mean(numeric_data, axis=0)) / np.std(numeric_data, axis=0)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:, 0]
y = principal_components[:, 1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()


def accuracy(predictions, outcomes):
    return (100 * np.mean(predictions == outcomes))

x = np.array(data.high_quality)
y = np.zeros(len(x))
print(accuracy(y,x))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)

print(accuracy(library_predictions,data['high_quality']))

n_rows = data.shape[0]
random.seed(123)
samples = random.sample(range(n_rows),10)
selection =  samples

print(selection)

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
predictors = predictors[training_indices,:]
outcomes = np.array(data["high_quality"])
print(predictors)
my_predictions = np.array([knn_predict(p,predictors,outcomes,k=5) for p in predictors[selection]])

print(my_predictions)
print(outcomes[selection])

percentage = accuracy(my_predictions, outcomes[selection])