import pandas as pd
import requests
import matplotlib.pyplot as plt

from prophet import Prophet
fm = '../ch14/stock_005930_data.csv'
df_raw = pd.read_csv(fm)
print("-"*50)
print(df_raw.head())
print("-"*50)

df_raw['ds'] = pd.to_datetime(df_raw['date'])
df_raw['y'] = pd.to_datetime(df_raw['end_price'])

df_data = df_raw[['ds' , 'y']]
print("-"*50)
print(df_data)
model = Prophet()
print("-"*50)
print("데이터 학습")
model.fit(df_data)

focail = model.make_future_dataframe(periods=365)
forest = model.predict(focail)
print(focail.tail())
fig1 = model.plot(forest)
fig2 = model.plot_components(forest)
plt.show()
