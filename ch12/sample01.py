import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



filename = '../ch11/survey_raw.csv'

df_raw = pd.read_csv(filename)

print('-'*50)
print(df_raw)
print('-'*50)
colname = 'LanguageHaveWorkedWith'
data_lang = df_raw[colname]
data_lang_dropna = data_lang.dropna()
print('type',type(data_lang))

print('-'*50)
print(data_lang.head())
print('-'*50)
llst = []
for c in data_lang:

    print(type(c))
    print(c)
    '''try:
        data_split = c.split(';')
        print(type(data_split))
        print(data_split)
    except:
        pass'''
    if type(c) != str:
        continue
    data_split = c.split(';')
    print(type(data_split))
    print(data_split)

    for cc in data_split:
        print(cc)
        llst.append(cc)
print('-'*50)
print(llst)
