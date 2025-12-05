import pandas as pd
import requests

fm = './stock_005930.csv'
df_raw = pd.read_csv(fm)

print("-"*50)
print(df_raw.info)

rc = {
    '날짜': 'date',
    '종가': 'end_price',
    '시가': 'start_price',
    '고가': 'highest_price',
    '저가': 'lowest_price',

}
drop_cols = ['전일비' , '거래량']
df_raw.rename(columns=rc , inplace=True)
df_raw.drop(columns=drop_cols , inplace=True)

print('-'*50)
print(df_raw.info())
df_raw.to_csv('./stock_005930_data.csv'  )
