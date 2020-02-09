import pandas as pd
import numpy as np

df = pd.read_csv('worldpopulation.csv')
print("Riga relativa all'Italia:", df.loc[ df['Country Code'] == 'ITA' ])

dfNoNan = df.dropna()
dfNoNan = dfNoNan.set_index('Country Code')

df2018 = dfNoNan['2018 [YR2018]']
df2018 = df2018.replace('..', np.nan)
df2018 = df2018.dropna()
df2018 = df2018.astype('float')
df2018 = df2018.sort_values(ascending=False)
print("Top 20 max percentuale di popolazione urbana:", df2018[0:20])
