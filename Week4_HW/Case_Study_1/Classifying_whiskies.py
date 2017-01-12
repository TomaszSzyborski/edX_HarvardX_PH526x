import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

print(whisky.head())

#extracting flavors from whisky data frame
flavors = whisky.iloc[:,2:14]

print(flavors.head())

#pairwise correlation of columns in flavors
corr_flavours = pd.DataFrame.corr(flavors)

print(corr_flavours)

def corr_flavours(flavors):
    corr_flavours = pd.DataFrame.corr(flavors)
    plt.figure(figsize=(10,10))
    plt.pcolor(corr_flavours)
    plt.colorbar()
    plt.savefig("corr_flavour.pdf")

def corr_whisky(flavors):
    corr_whisky = pd.DataFrame.corr(flavors.transpose())
    plt.figure(figsize=(10,10))
    plt.pcolor(corr_whisky)
    plt.axis("tight")
    plt.colorbar()
    plt.savefig("corr_whisky.pdf")

#corr_flavours(flavors)
#corr_whisky(flavors)

