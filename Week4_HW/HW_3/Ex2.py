import pandas as pd
data_filepath = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_974/datasets/'

pid1 = pd.read_csv(data_filepath + "key_vilno_1.csv", header=None)
pid2 = pd.read_csv(data_filepath + "key_vilno_2.csv", header=None)

print(pid1)
print(pid2)