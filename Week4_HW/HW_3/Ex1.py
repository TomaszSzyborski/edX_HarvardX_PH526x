import pandas as pd

data_filepath = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_974/datasets/'
df  = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df[df["village"] == 1]
df2 = df[df["village"] == 2]

print(df1.head())