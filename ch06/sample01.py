import pandas as pd

covid_file_path = '..//ch04//data//owid-covid-data.csv'
df = pd.read_csv(covid_file_path)

selected_coulmns = ['iso_code','location','date','total_cases','population']
selected_df = df[selected_coulmns]

south_korea_df = selected_df[selected_df.location =="South Korea"]
print("-"*50)
print(south_korea_df.head())

korea_date_index_df = south_korea_df.set_index('date')
print('-'*50)
print(korea_date_index_df.head())

# korea_date_index_df.to_csv('../ch06/save/korea.csv',encoding='utf-8')

America = selected_df[selected_df.location =="United States"]
print("-"*50)
print(America.head())

America_index_df = America.set_index('date')
print('-'*50)
print(America_index_df.head())

#  America_index_df.to_csv('../ch06/save/usa.csv',encoding='utf-8')
