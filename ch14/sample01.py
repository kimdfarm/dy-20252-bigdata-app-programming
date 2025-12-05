import pandas as pd
import requests
from io import StringIO
# url = 'https://www.dongyang.ac.kr/dmu/4904/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZG11JTJGNjc3JTJGYXJ0Y2xMaXN0LmRvJTNG'
atb = pd.DataFrame()
for i in range(1 , 738):

    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={i}'

    user_ahgent = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
                   }
    response = requests.get(url , headers=user_ahgent)

    raw_data = response.text
    dyty_data = pd.read_html(StringIO(raw_data))
    print(type(dyty_data))

    table_data = dyty_data[0]
    print(table_data)

    atb = pd.concat([atb , table_data])
    print( i , "/ 737")
atb.dropna(inplace=True)

print('-'*50)
print(atb.info())
print(atb.head())
atb.to_csv('./stock_005930.csv' , index=False)