import pandas as pd

# 加载数据
data1 = pd.read_excel('2023test1/B1/attachment1.xlsx')
two_cities_byTime = data1.groupby('Date Y/M/D')['Express delivery quantity (PCS)'].sum()
two_cities_byTime.to_excel('2023test1/B1/Q2时间序列.xlsx', index=False)