import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

from ch06.common import is_windows_platform, is_mac_platform, get_font_name, init_plt


def get_covid_data(file_path):
    df = pd.read_csv(file_path,encoding='utf-8')
    index_df = df.set_index('date')
    return index_df['total_cases']

kor_df = get_covid_data('../ch06/save/korea.csv')
usa_df = get_covid_data('../ch06/save/usa.csv')
index_data = kor_df.index
print(index_data)

init_plt()
covid_df = pd.DataFrame(
    {
        '대한민국':kor_df,
        '미국':usa_df,
    }
    ,index=index_data
)
covid_df.plot.line()

plt.show()