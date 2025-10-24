import numpy as np
import pandas as pd



def get_covid_data(file_path):
    df = pd.read_csv(file_path,encoding='utf-8')
    index_df = df.set_index('date')
    return index_df['total_cases']

def get_population(file_path):
    kor = pd.read_csv(file_path)
    korid = kor.set_index('date')
    return  korid['population']['2020-01-05']

korp = get_population('../ch05/data/korea.csv')
usap = get_population('../ch05/data/usa.csv')

print(usap/korp)

print(round(usap, 2)/round(korp,2))