import pandas as pd
import os



hfp = '..//data//Weekly_United_States_COVID-19_Cases_and_Deaths_by_State_-_ARCHIVED_20251107.csv'
df = pd.read_csv(hfp)

dfg  =df[df['state']=='HI']
print(dfg.head())
dfg.info()
'''if os.path.exists(hfp):
    os.remove(hfp)
dff.to_csv(hfp)'''