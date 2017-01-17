import pandas as pd
from collections import Counter
import numpy as np

data_filepath = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_974/datasets/'

df  = pd.read_stata(data_filepath + "individual_characteristics.dta")

df1 = df[df["village"] == 1]
df2 = df[df["village"] == 2]

#dictionaries of values from pandas DataFrame

sex1      = pd.Series(df1.resp_gend.values,index=df1.pid).to_dict()
caste1    = pd.Series(df1.caste.values,index=df1.pid).to_dict()
religion1 = pd.Series(df1.religion.values,index=df1.pid).to_dict()

sex2      = pd.Series(df2.resp_gend.values,index=df2.pid).to_dict()
caste2    = pd.Series(df2.caste.values,index=df2.pid).to_dict()
religion2 = pd.Series(df2.religion.values,index=df2.pid).to_dict()

def chance_homophily(chars):
    chars_counts_dict = Counter(chars.values())
    chars_counts = np.array(list(chars_counts_dict.values()))
    chars_props  = chars_counts / sum(chars_counts)
    return sum(chars_props**2)


print("Village 1 chance of same sex:", chance_homophily(sex1))
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))
print("Village 2 chance of same sex:", chance_homophily(sex2))
print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))
