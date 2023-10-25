import pandas as pd
import numpy as np

# 读取数据
data1 = pd.read_excel('2023test1/B1/attachment1.xlsx')
data2 = pd.read_excel('2023test1/B1/Q1时间序列.xlsx')
data3 = pd.read_excel('2023test1/B1/α值.xlsx')

# 按照收货和发货地，对每个城市的快递数量求和
total_receiving = data1.groupby('Receiving city')['Express delivery quantity (PCS)'].sum()
total_delivering = data1.groupby('Delivering city')['Express delivery quantity (PCS)'].sum()

# 提取所有城市
cities = sorted(list(set(data1['Receiving city'].unique()) | set(data1['Delivering city'].unique())))

# 计算α值的权重
trend = data3.groupby('city')['α'].sum()
trend_weights = trend / trend.sum()

# 将数据按日期和城市分组，计算每天每个城市的快递总量
grouped = data2.groupby(['Date Y/M/D', 'City'])['Total Quantity'].sum().reset_index()

# 将数据转换为每列是一个城市，每行是一个日期的格式
pivot_df = grouped.pivot(index='Date Y/M/D', columns='City', values='Total Quantity')

# 计算所有城市之间的相关性
correlation = pivot_df.corr()

# 初始化一个字典来保存每个城市与其他城市相关性系数大于0.8的城市个数
city_correlation_count = {}

# 遍历所有城市
for city in correlation.columns:
    # 计算与该城市相关性系数大于0.8的城市个数
    count = sum(correlation[city] > 0.8)
    # 将结果保存到字典中
    city_correlation_count[city] = count

# 定义权重
weights = {
    'receiving': 0.25,
    'delivering': 0.25,
    'trend': 0.25,
    'correlation': 0.25
}

# 计算收货和发货地的权重
receiving_weights = total_receiving / total_receiving.sum()
delivering_weights = total_delivering / total_delivering.sum()

# 计算相关性系数大于0.8的城市个数的权重
correlation_count_values = list(city_correlation_count.values())
correlation_count_weights = np.array([count / sum(correlation_count_values) for count in correlation_count_values])

# 对齐权重数组的长度
receiving_weights = receiving_weights.reindex(cities, fill_value=0)
delivering_weights = delivering_weights.reindex(cities, fill_value=0)
trend_weights = trend_weights.reindex(cities, fill_value=0)

# 综合权重
final_weights = (weights['receiving'] * np.array(receiving_weights)) + (weights['delivering'] * np.array(delivering_weights)) + (weights['trend'] * np.array(trend_weights)) + (weights['correlation'] * correlation_count_weights)

# 输出权重
for city, weight in zip(cities, final_weights):
    print(f'城市{city}的权重为{weight}')
