import pandas as pd
import requests
import matplotlib.pyplot as plt
fm = './stock_005930_data.csv'
df_raw = pd.read_csv(fm)
print("-"*50)
print(df_raw.info)
val1 = 10
val2 = 5

print('-'*50)


df_raw['middle'] = df_raw['highest_price'] - ((df_raw['highest_price'] - df_raw['lowest_price']) / 2)
df_raw['month'] = df_raw['date'].str[0:7]
df_raw.set_index('date' , inplace=True)

df_raw[:50].boxplot(column='middle' , by=['month'])
plt.show()