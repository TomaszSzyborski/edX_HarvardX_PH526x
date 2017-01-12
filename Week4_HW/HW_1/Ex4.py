import pandas as pd
import numpy as np
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from sklearn.cluster.bicluster import SpectralCoclustering

#Load whisky
whisky = pd.read_csv("../Case_Study_1/whiskies.txt")
whisky["Region"] = pd.read_csv("../Case_Study_1/regions.txt")

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

source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": correlation_colors,
        "alphas": correlations.flatten(),
        "correlations": correlations.flatten()
    }
)

output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = figure(title="Whisky Correlations",
                 x_axis_location="above", tools="resize,hover,save",
                 x_range=list(reversed(distilleries)), y_range=distilleries)
fig.grid.grid_line_color = None
fig.axis.axis_line_color = None
fig.axis.major_tick_line_color = None
fig.axis.major_label_text_font_size = "5pt"
fig.xaxis.major_label_orientation = np.pi / 3

fig.rect('x', 'y', .9, .9, source=source,
     color='colors', alpha='alphas')
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Whiskies": "@x, @y",
    "Correlation": "@correlations",
}

show(fig)
