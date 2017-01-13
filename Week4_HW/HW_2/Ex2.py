import datetime

import pandas as pd

bird_data = pd.read_csv("../Case_Study_2/bird_tracking.csv")

grouped_birds = bird_data.groupby("bird_name")
mean_speeds = grouped_birds.speed_2d.mean()
mean_altitudes = grouped_birds.altitude.mean()

# Convert birddata.date_time to the `pd.datetime` format.
bird_data.date_time = pd.to_datetime(bird_data.date_time)

# Create a new column of day of observation
bird_data["date"] = bird_data.date_time.dt.date

# Check the head of the column.
print(bird_data.date.head())

grouped_by_dates = bird_data.groupby("date")
mean_altitudes_per_day = grouped_by_dates.altitude.mean()
