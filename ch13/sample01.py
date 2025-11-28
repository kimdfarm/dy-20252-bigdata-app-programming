import pandas as pd
import requests

# url = 'https://www.dongyang.ac.kr/dmu/4904/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZG11JTJGNjc3JTJGYXJ0Y2xMaXN0LmRvJTNG'
url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'
user_ahgent = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
               }
response = requests.get(url , headers=user_ahgent)

raw_data = response.text
dyty_data = pd.read_html(raw_data)
print(type(dyty_data))