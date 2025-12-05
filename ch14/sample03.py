import pandas as pd
import requests
import matplotlib.pyplot as plt
fm = './stock_005930_data.csv'
df_raw = pd.read_csv(fm)
df_raw.set_index('date' , inplace=True)
print("-"*50)
print(df_raw.info)


print('-'*50)


df_raw.plot.line()
plt.show()