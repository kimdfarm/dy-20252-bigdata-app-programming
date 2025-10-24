import numpy as np
import pandas as pd

cp= '../ch04/data/owid-covid-data.csv'
rd= pd.read_csv(cp)

sc =  ['iso_code' , 'location']
sd = rd[sc]

sdid = set