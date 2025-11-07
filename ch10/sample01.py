import pandas as pd
import os
# 파일 경로
file_path = '..//data//hawaii-covid-data.csv'
df_raw = pd.read_csv(file_path)

# 데이터 확인
print('-'*50)
print(df_raw.head())

print('-'*50)
print(df_raw.info())

# 'population' 컬럼을 0으로 설정
df_raw['population'] = 0

# 필요한 컬럼만 선택하여 복사
hi_column = ['submission_date', 'tot_cases', 'population']
dfrf = df_raw[hi_column].copy()  # .copy()를 사용하여 깊은 복사

# 'submission_date' 컬럼을 날짜 형식으로 변환 (경고 해결)
dfrf['date'] = pd.to_datetime(dfrf['submission_date'], format='%m/%d/%Y')

# 'population' 컬럼 값을 1441553으로 변경
df_raw['population'] = 1441553

print('-'*50)
print(df_raw.info())

# 새로운 DataFrame에서 'date' 컬럼 포함
hi_column = ['date', 'tot_cases', 'population']
dff = dfrf[hi_column]  # df_raw가 아닌 dfrf 사용

print('-'*50)
print(dff.info())

# 'date'를 인덱스로 설정
dff.set_index('date', inplace=True)

print('-'*50)
print(dff.head())

# 저장할 경로 지정
hfp = '..//hi_covid_data.csv'
if os.path.exists(hfp):
    os.remove(hfp)
dff.to_csv(hfp)