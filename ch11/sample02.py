import pandas as pd

fm = './survey_raw.csv'


df_raw = pd.read_csv(fm)

print('-'*50)
print(df_raw.head())

print('-'*50)
print(df_raw['Age'])

sr = df_raw['Age']

print('-'*50)
print(sr.unique())

print('-'*50)
print(sr.drop_duplicates())

print(df_raw.groupby('Age'))

