import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

from ch06.common import is_windows_platform, is_mac_platform, get_font_name

jumsu1 = [3.5,4.0 , 4.5, 3.8]
jumsu2 = [3.0,4.5 , 4.0, 3.2]
jumsu3 = [2.0,3.0 , 2.0, 4.0]

year = [2024,2025,2026,2027]
rc('font',family=get_font_name())
plt.rcParams['axes.unicode_minus'] = False

jumsu_df = pd.DataFrame(
    {
        'jumsu1':jumsu1,
        'jumsu2':jumsu2,
        'jumsu3':jumsu3,
    }
    ,index=year
)
lines = jumsu_df.plot.line()
plt.show()
