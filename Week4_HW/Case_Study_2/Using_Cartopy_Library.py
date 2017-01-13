import datetime
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature


import pandas as pd
bird_data = pd.read_csv("bird_tracking.csv")

date_str = bird_data.date_time[0]
date_str = date_str[:-3]

timestamps=[]
for k in range(len(bird_data)):
    timestamps.append(datetime.datetime.strptime\
                          (bird_data.date_time.iloc[k][:-3],"%Y-%m-%d %H:%M:%S"))

bird_data["timestamp"] = pd.Series(timestamps, index=bird_data.index)
bird_names = pd.unique(bird_data.bird_name)

proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))

#Add features to map
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

for name in bird_names:
    ix = bird_data['bird_name'] == name
    x, y = bird_data.longitude[ix], bird_data.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)

plt.legend(loc="upper left")
plt.savefig("map.pdf")