import pandas as pd
import matplotlib.pyplot as plt

bird_data = pd.read_csv("../Case_Study_2/bird_tracking.csv")

grouped_birds = bird_data.groupby("bird_name")
mean_speeds = grouped_birds.speed_2d.mean()
mean_altitudes = grouped_birds.altitude.mean()

bird_data.date_time = pd.to_datetime(bird_data.date_time)
bird_data["date"] = bird_data.date_time.dt.date

grouped_bird_day = bird_data.groupby(by=["bird_name", "date"])
daily_speeds = grouped_bird_day.speed_2d.mean()

eric_daily_speed  = daily_speeds["Eric"]
sanne_daily_speed = daily_speeds["Sanne"]
nico_daily_speed  = daily_speeds["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.savefig("speed_each_bird.pdf")
