import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

filename = '../ch12/data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(filename)
filename2 = '../ch12/data/seoul-metro-station-info.csv'

df_raw2 = pd.read_csv(filename2)
cols2 = ['station.code'  ,'geo.latitude'  ,'geo.longitude']
df_station_raw = df_raw2[cols2]
df_station_raw = df_station_raw.set_index('station.code')

cols = ['station_code'  ,'people_in'  ,'people_out']
print('-'*50)
print(df_raw.info())

df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'])

print('-'*50)
print(df_raw.info())
print('-'*50)
print(df_raw)
df_in = df_raw[cols][df_raw['timestamp'].dt.hour < 9].groupby('station_code').sum()
print(df_in)

join_in = df_in.join(df_station_raw)
print(join_in)
map = folium.Map(location=[37.50018 , 126.8676], zoom_start=16)

HeatMap(data = join_in[['geo.latitude' ,'geo.longitude', 'people_in']]).add_to(map)

map.show_in_browser()