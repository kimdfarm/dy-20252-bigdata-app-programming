import pandas as pd
from deep_translator import GoogleTranslator
import matplotlib.pyplot as plt
import time

fm = './data_Country.csv'

def translate_to_korean_deep(text):
    if pd.isna(text):
        return text
    try:
        result = translator.translate(text)
        time.sleep(0.1)
        return result
    except Exception as e:
        print(f"번역 오류 발생: {e}, 텍스트: {text}")
        return text

df_raw = pd.read_csv(fm)

translator = GoogleTranslator(source='auto', target='ko')
st = df_raw.groupby('Country').size()

st = st.nlargest(20)

new_index_korean = pd.Series(st.index).apply(translate_to_korean_deep)
st.index = new_index_korean

try:
    plt.rc('font', family='Malgun Gothic')
except:
    pass

st.nlargest(20).plot.pie(figsize=(10,10))
plt.title('국가별 데이터 빈도 (한글)')
plt.tight_layout()
plt.show()
