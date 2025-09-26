import pandas as pd
from pandas.core.methods.describe import select_describe_func

covid_file_path = './data/owid-covid-data.csv'
df = pd.read_csv(covid_file_path)
print(df)
covid_file_path1 = './data/data_bar.csv'
df1 = pd.read_csv(covid_file_path1,sep='|', encoding='EUC-KR')
print(df.info())
print(df.head())

selected_coulmns = ['iso_code','location','date','total_cases','population']

selected_df = df[selected_coulmns]

print(selected_df.head())
location = df['location']
selected_location = selected_df['location']

print('-'*50)

print(location.unique())

print('-'*50)


south_korea = selected_df[selected_df.location == 'South Korea']
print('-'*50)
print(south_korea.head())
