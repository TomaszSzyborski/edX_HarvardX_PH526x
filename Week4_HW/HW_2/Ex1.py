
import pandas as pd

bird_data = pd.read_csv("../Case_Study_2/bird_tracking.csv")

# First, use `groupby` to group up the data.
grouped_birds = bird_data.groupby("bird_name")
# Now operations are performed on each group.
mean_speeds = grouped_birds.speed_2d.mean()
# The `head` method prints the first 5 lines of each bird.
print("Grouped birds:")
print(grouped_birds.head())
print("Mean speeds:")
print(mean_speeds.head())

# Find the mean `altitude` for each bird.
# Assign this to `mean_altitudes`.
mean_altitudes = grouped_birds.altitude.mean()
print(mean_altitudes.head())