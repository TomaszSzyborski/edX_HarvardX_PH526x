import datetime
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
bird_data = pd.read_csv("bird_tracking.csv")

# Examples
# time_1 = datetime.datetime.today()
# time_2 = datetime.datetime.today()
# time_delta_1 = time_2 - time_1

date_str = bird_data.date_time[0]
date_str = date_str[:-3]

#date_object = datetime.datetime.strptime(date_str[:-3],"%Y-%m-%d %H:%M:%S")

timestamps=[]
for k in range(len(bird_data)):
    timestamps.append(datetime.datetime.strptime\
                          (bird_data.date_time.iloc[k][:-3],"%Y-%m-%d %H:%M:%S"))

print(timestamps[:10])

#adding proper timestamp rather than date_time in the dataframe
bird_data["timestamp"] = pd.Series(timestamps, index=bird_data.index)

#getting timestamp arithmetic
print(bird_data.timestamp[4] - bird_data.timestamp[3])

#checking how much time has elapsed since beginning of data collection
times = bird_data.timestamp[bird_data.bird_name =="Eric"]
elapsed_time = [time - times[0] for time in times]
print(elapsed_time)

#count days
sample_days = elapsed_time[1000] / datetime.timedelta(days=1)
print(sample_days)

#count hours
sample_hours = elapsed_time[1000] / datetime.timedelta(hours=1)
print(sample_hours)

#plot
plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observations")
plt.ylabel("Time elapsed (days)")

plt.savefig("time.pdf")