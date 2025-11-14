import pandas as pd

from ch11.common_function import save_csv

fm = './survey_results_public.csv'

df_raw = pd.read_csv(fm)
print('-'*50)

print(df_raw.head())

print('-'*50)
print(df_raw.info())


column = ['Age', 'Country' , 'LanguageHaveWorkedWith','LearnCode']
df_raw = df_raw[column]


print('-'*50)
print(df_raw.info())

save_csv(df_raw , './survey_raw.csv')


