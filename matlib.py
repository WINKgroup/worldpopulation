import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('worldpopulation.csv')
dfNoNan = df.dropna()
dfNoNan = dfNoNan.replace('..', np.nan)
dfNoNan = dfNoNan.set_index('Country Code')
del dfNoNan['Country Name']
del dfNoNan['Series Code']
del dfNoNan['Series Name']

dfNoNan = dfNoNan.astype('float')
italySeries = dfNoNan.loc['ITA']

italySeries.plot()
plt.title('% popolazione urbana in Italia')
plt.xlabel('Anni')
plt.ylabel('%')

dfCompare = dfNoNan[['1990 [YR1990]', '2018 [YR2018]']]
dfCompare = dfCompare.rename(index={0: 'YR1990', 1: 'YR2018'})
dfCompare.plot.hist(bins=8, alpha=.5)

plt.title('Raffronto popolazione urbana mondiale')
plt.xlabel('% popolazione urbana')
plt.ylabel('numero Paesi')

plt.figure(3)
otherSeries = dfNoNan.copy()
otherSeries = otherSeries.drop('ITA')
otherSeries = otherSeries.mean(axis=0)

italySeries.plot()
otherSeries.plot()
plt.title('Raffronto tra % popolazione urbana in Italia e nel resto del Mondo')
plt.xlabel('Anni')
plt.ylabel('%')
plt.legend(['ITA', 'others'])
plt.ylim(0, 100)

plt.show()
