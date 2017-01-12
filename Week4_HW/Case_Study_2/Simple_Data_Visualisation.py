import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
bird_data = pd.read_csv("bird_tracking.csv")

ix = bird_data.bird_name == "Eric"

print(ix)

x, y = bird_data.longitude[ix], bird_data.latitude[ix]

plt.figure(figsize=(7, 7))
plt.plot(x, y, ".")

plt.savefig("eric_track.pdf")

bird_names = pd.unique(bird_data.bird_name)
print(bird_names)

plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    ix = bird_data.bird_name == bird_name
    x, y = bird_data.longitude[ix], bird_data.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc = "lower right")

plt.savefig("three_birds.pdf")