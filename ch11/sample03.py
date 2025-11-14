import pandas as pd
import matplotlib.pyplot as plt

from ch11.common_function import save_csv

fm = './survey_raw.csv'
df_raw = pd.read_csv(fm)
sr = df_raw['Age']
save_csv(sr , 'data_age.csv')

df_raw = pd.read_csv(fm)
sr = df_raw['Country']
save_csv(sr , 'data_Country.csv')
