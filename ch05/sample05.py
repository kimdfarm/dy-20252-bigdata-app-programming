import numpy as np
import pandas as pd

def get_covid_data(ic):
    fp = '../ch04/data/owid-covid-data.csv'
    df= pd.read_csv(fp)
    fd = df[df.iso_code == ic]
    id = fd.set_index('date')
    return id['total_cases']
kd =get_covid_data('KOR')
print(kd)