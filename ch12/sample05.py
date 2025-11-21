import folium
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

filename = '../ch12/data/seoul-metro-inout.csv'
df_raw = pd.read_csv(filename)
df_raw = df_raw.set_index('station_code')
print('-'*50)
print(df_raw)

map = folium.Map(location=[37.50018 , 126.8676], zoom_start=16)
data_in = df_raw[['geo.latitude' , 'geo.longitude','people_in']]
#data_in = df_raw[['geo.latitude' , 'geo.longitude','people_out']]
HeatMap(data = data_in).add_to(map)
map.show_in_browser()
map.save('./map_in.html')