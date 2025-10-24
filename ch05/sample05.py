import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_covid_data(ic):
    fp = '../ch04/data/owid-covid-data.csv'
    df= pd.read_csv(fp)
    fd = df[df.iso_code == ic]
    id = fd.set_index('date')
    return id['total_cases']

def get_W(ic ,de="KOR"):
    fp = '../ch04/data/owid-covid-data.csv'
    df = pd.read_csv(fp)
    fd = df[df.iso_code == ic]['population']
    fa = df[df.iso_code == "KOR"]['population']
    re = round(fd.iat[0]/ fa.iat[0] , 2)

    fx = df[df.iso_code == ic].set_index('date')


    return fx['total_cases']*re


k =get_covid_data('KOR')
u = get_covid_data('USA')
f = get_covid_data('FRA')
g = get_covid_data('GBR')
p = get_covid_data('POL')


kd = k.index
kr = get_W("KOR")
ur = get_covid_data('USA')
fr = get_covid_data('FRA')
gr = get_covid_data('GBR')
pr = get_covid_data('POL')

data = {
    'kor': kr ,
    'usa': ur,
    'fra': fr,
    'gbr': gr,
    'pol':pr
}
cd= pd.DataFrame(data,index=kd)
cd[:].plot.line(rot=45)

plt.show()



