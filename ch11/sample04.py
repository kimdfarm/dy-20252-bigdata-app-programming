import pandas as pd
import matplotlib.pyplot as plt
fm = './data_age.csv'


df_raw = pd.read_csv(fm)

st = df_raw.groupby('Age').size()
index_code = [
     'Under 18 years old',
     '18-24 years old',
     '25-34 years old',
     '35-44 years old',
     '45-54 years old',
     '55-64 years old',
     '65 years or older',
    'Prefer not to say'
]


st = st.reindex(index_code)
'''st.plot.line()
plt.show()'''
#  st.plot.bar(rot=45)
st.plot.barh(rot=45)
plt.tight_layout()
plt.show()
