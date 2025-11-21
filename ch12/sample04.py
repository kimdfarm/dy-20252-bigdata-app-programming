import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



filename = '../ch12/data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(filename)

filename2 = '../ch12/data/seoul-metro-station-info.csv'
df_raw2 = pd.read_csv(filename2)

col = 'station_code'
cols = ['station_code'  ,'people_in'  ,'people_out']

df_raw = df_raw[cols]


print('-'*50)
print(df_raw.head())

stationsum = df_raw.groupby(col).sum(numeric_only=True)
print('-'*50)
print(stationsum)


print('-'*50)
df_raw2.info()
cols2 = ['station.code'  ,'geo.latitude'  ,'geo.longitude']
df_station_raw = df_raw2[cols2]
df_station_raw = df_station_raw.set_index('station.code')

join_data = stationsum.join(df_station_raw)

print('-'*50)
print(join_data)

join_data.to_csv('./data/seoul-metro-inout.csv')
