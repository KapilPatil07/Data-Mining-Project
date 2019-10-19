import pandas as pd
import numpy as np
#df = pd.read_csv('ABCD.csv')
#p1='^[0-9]'

#df.head()
#new_df = df.replace(p1, 0)
#df1 = df.mean(axis=0, skipna = 9999)
#new_df = df.fillna({'DewPointHighF' : 0})
#df['DewPointHighF'] = df['DewPointHighF'].fillna((df['DewPointHighF'].mean()))
#new_df = df.mean(df.fillna(0),axis=0, inplace= True)
#new_df.fillna(new_df.mean(axis = 0))
#col_mean = np.nanmean("DewPointHighF", axis = 0)
#print ("columns mean", str(col_mean))
#mean = new_df["DewPointHighF"].mean()
#new_df["DewPointHighF"].replace(np.NaN, mean)
#new_df.to_csv('Missing_value1.csv')


# importing libraries 
import pandas as pd 
import numpy as np 
  
# read the data in a pandas dataframe 
data = pd.read_csv("austin_weather.csv") 
  
# drop or delete the unnecessary columns in the data. 
data = data.drop(['Events', 'Date', 'SeaLevelPressureHighInches',  
                  'SeaLevelPressureLowInches'], axis = 1) 
  
# some values have 'T' which denotes trace rainfall 
# we need to replace all occurrences of T with 0 
# so that we can use the data in our model 
data = data.replace('T', 0.00) 
  
# the data also contains '-' which indicates no  
# or NIL. This means that data is not available 
# we need to replace these values as well. 
data = data.replace('-', 73.00)
#new_df = data.mean(data.fillna(0),axis=0, inplace= True)

data.to_csv('austin_final.csv',mode = 'w', index=False)
mean1=data['HumidityHighPercent'].mean()
# save the data in a csv file 
#new_df.to_csv('austin_final.csv') 
