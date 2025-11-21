import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



filename = '../ch11/survey_raw.csv'

df_raw = pd.read_csv(filename)

print('-'*50)
print(df_raw)
print('-'*50)
colname = 'LanguageHaveWorkedWith'
data_lan = df_raw[colname]
data_lang = data_lan.str.split(';')

print('-'*50)
print(data_lang)

data_lang2= data_lang.explode()
print('-'*50)
print(data_lang2)
data_lang3 = data_lang2.groupby(data_lang2).size()

print('-'*50)
print(data_lang3)

data_lang3.nlargest(20).plot.pie(figsize=(10,10), autopct='%1.2f%%')
plt.tight_layout()
# plt.show()
plt.savefig('./lang_data.png')
