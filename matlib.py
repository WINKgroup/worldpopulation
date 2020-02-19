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
dfNoNan.columns = [x[:4] for x in dfNoNan.columns]
dfNoNan.columns = pd.to_datetime(dfNoNan.columns)

dfNoNan = dfNoNan.astype('float')
italySeries = dfNoNan.loc['ITA']

italySeries.plot()
plt.title('% popolazione urbana in Italia')
plt.xlabel('Anni')
plt.ylabel('%')
#plt.ylim(bottom=0, top=100)

dfCompare = dfNoNan.iloc[:,[0,-2]]

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