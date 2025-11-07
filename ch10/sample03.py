import os

import pandas as pd
import matplotlib.pyplot as plt

from ch06.common import is_windows_platform, is_mac_platform, get_font_name, init_plt


def get_covid_data(file_path):
    df = pd.read_csv(file_path,encoding='utf-8')
    index_df = df.set_index('date')
    #TODO 1111
    try:
        population = df['population'].iat[0]
        return index_df['total_cases'] , population
    except:
        return index_df['total_cases'] , None

kor_df ,kp= get_covid_data('../ch06/save/korea.csv')
usa_df ,up= get_covid_data('..//data//hi_covid_data.csv')

index_data = kor_df.index
print(index_data)

init_plt()
# 인구비율 구하기
rate = round(kp / up , 2)
covid_df = pd.DataFrame(
    {
        '대한민국':kor_df,
        '하와이':usa_df * rate,
    }
    ,index=index_data
)
covid_df.plot.line()

plt.show()