import pandas as pd
import numpy as np
# 填充空缺值为Nan
# 读取数据
data1 = pd.read_excel('2023test1/B1/附件2.xlsx')

# 将日期列设置为Datetime类型
data1['Date Y/M/D'] = pd.to_datetime(data1['Date Y/M/D'])

# 定义填充函数
def fill_missing_dates(df):
    df.set_index('Date Y/M/D', inplace=True)
    df = df.reindex(pd.date_range(start=df.index.min(), end=df.index.max()))
    df['Delivering city'].ffill(inplace=True)
    df['Receiving city'].ffill(inplace=True)
    return df

# 创建一个新的DataFrame来保存结果
new_data = pd.DataFrame()

# 对每一个城市对进行分组，并执行填充函数
for _, group in data1.groupby(['Delivering city', 'Receiving city']):
    group_filled = fill_missing_dates(group)
    new_data = pd.concat([new_data, group_filled])

new_data.reset_index(inplace=True)
new_data.rename(columns={'index':'Date Y/M/D'}, inplace=True)

# 保存结果
new_data.to_excel('2023test1/B1/Q3时间序列.xlsx', index=False)

###################################
# 读取数据
data1 = pd.read_excel('2023test1/B1/Q3时间序列.xlsx')

# 将 Express delivery quantity (PCS) 列非空的值设为 1，空值设为 0
data1['Express delivery quantity (PCS)'] = np.where(data1['Express delivery quantity (PCS)'].notnull(), 1, 0)

# 创建ExcelWriter对象，用于写入多个sheet
with pd.ExcelWriter('2023test1/B1/Q3时间序列城市对.xlsx') as writer:
    # 对'Delivering city'和'Receiving city'进行分组
    for (delivering_city, receiving_city), group in data1.groupby(['Delivering city', 'Receiving city']):
        # 只保留'Date Y/M/D'和'Express delivery quantity (PCS)'这两列
        group = group[['Date Y/M/D', 'Express delivery quantity (PCS)']]
        # 将分组的数据写入一个新的sheet，sheet的名字由'Delivering city'和'Receiving city'拼接而成
        group.to_excel(writer, sheet_name=f'{delivering_city}_{receiving_city}', index=False)
