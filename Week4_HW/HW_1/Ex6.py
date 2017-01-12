from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure
import pandas as pd
import numpy as np

#Load whisky
from sklearn.cluster import SpectralCoclustering

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

def location_plot(title, colors):
    output_file(title + ".html")
    location_source = ColumnDataSource(
        data={
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
        }
    )

    fig = figure(title=title,
                 x_axis_location="above", tools="resize, hover, save")
    fig.plot_width = 400
    fig.plot_height = 500
    fig.circle(x="x", y="y", size=9, source=location_source,color='colors', line_color=None)

    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type=HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
    }
    show(fig)


region_colors ={'Campbelltown': 'purple',
 'Highlands': 'orange',
 'Islands': 'blue',
 'Islay': 'gray',
 'Lowlands': 'green',
 'Speyside': 'red'}

region_cols = [region_colors[region] for region in list(whisky.Region)]
location_plot("Whisky Locations and Regions", region_cols)