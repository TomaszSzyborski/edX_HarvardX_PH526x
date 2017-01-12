import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
bird_data = pd.read_csv("bird_tracking.csv")

ix = bird_data.bird_name == "Eric"
speed = bird_data.speed_2d[ix]

#check if there are any NaN occurences
print(np.isnan(speed).any())

# count NaN instances in array
print(np.count_nonzero(np.isnan(speed)))
print(np.sum(np.isnan(speed)))

#cleaning the data
index_of_missing_observations = np.isnan(speed)

#reversing the index to have only clean data
good_inds = ~np.isnan(speed)

#plot
plt.hist(speed[good_inds], bins=np.linspace(0,30,20), normed=True)
plt.xlabel("2D speed m/s")
plt.ylabel("Frequency")
plt.savefig("speed.pdf")

#################
bird_data.speed_2d.plot(kind="hist", range=[0,30])
plt.xlabel("2D speed m/s")
plt.ylabel("Frequency")
plt.savefig("pd_speed.pdf")