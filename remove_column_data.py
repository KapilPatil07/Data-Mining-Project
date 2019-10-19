import pandas as pd
data = pd.read_csv('austin_weather.csv')
data=data.drop(['Events','Date'], axis=1)
#data.to_csv('ABCD.csv')
data.to_csv('ABCD.csv',mode = 'w', index=False)
#orders.drop("Events", axis=1, inplace=True)
#orders.head(5)
