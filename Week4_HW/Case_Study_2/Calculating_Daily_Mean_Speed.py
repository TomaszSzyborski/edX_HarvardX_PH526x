import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

bird_data = pd.read_csv("bird_tracking.csv")

timestamps=[]
for k in range(len(bird_data)):
    timestamps.append(datetime.datetime.strptime\
                          (bird_data.date_time.iloc[k][:-3],"%Y-%m-%d %H:%M:%S"))

bird_data["timestamp"] = pd.Series(timestamps, index=bird_data.index)


data = bird_data[bird_data.bird_name == "Eric"]
times = bird_data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        #compute daily_mean_speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8, 6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("Mean_Speed.pdf")
