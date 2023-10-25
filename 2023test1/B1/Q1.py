import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_excel('2023test1/B1/attachment1.xlsx')
data2 = pd.read_excel('2023test1/B1/Q1时间序列.xlsx')
data3 = pd.read_excel('2023test1/B1/α值.xlsx')

########################################
# 按照收货和发货地，对每个城市的快递数量求和
total_receiving = data1.groupby('Receiving city')['Express delivery quantity (PCS)'].sum()
total_delivering = data1.groupby('Delivering city')['Express delivery quantity (PCS)'].sum()
cities = sorted(list(set(data1['Receiving city'].unique()) | set(data1['Delivering city'].unique())))
print(total_receiving)
print(total_delivering)

########################################
trend = data3.groupby('city')['α'].sum()
print(trend)

########################################
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
    # 计算与该城市相关性系数大于0.7的城市个数
    count = sum(correlation[city] > 0.8)
    # 将结果保存到字典中
    city_correlation_count[city] = count

# 输出结果
for city, count in city_correlation_count.items():
     print(f'城市{city}与其他城市相关性系数大于0.8的城市个数是{count}')

################################
# 定义熵权法函数
def entropy_weight(cities, total_receiving, total_delivering, trend, city_correlation_count):
    data = pd.DataFrame({'city': cities,
                         'total_receiving': [total_receiving.get(city, 0) for city in cities],
                         'total_delivering': [total_delivering.get(city, 0) for city in cities],
                         'trend': [trend.get(city, 0) for city in cities],
                         'city_correlation_count': [city_correlation_count.get(city, 0) for city in cities]})
    data.set_index('city', inplace=True)

    # 归一化
    data = (data - data.min()) / (data.max() - data.min())

    # 计算熵值
    P = data / data.sum()
    E = -(P * np.log(P)).sum()

    # 计算权重
    weights = (1 - E) / (4 - len(cities) * E)

    # 计算每个城市的得分
    data['score'] = (data * weights).sum(axis=1)

    # 对城市按得分排序
    ranking = data['score'].sort_values(ascending=False)

    return ranking

# 使用熵权法计算城市的重要性
city_importance = entropy_weight(cities, total_receiving, total_delivering, trend, city_correlation_count)

# 输出前五名城市
print(city_importance.head(5))

# 可视化前五名城市的重要性
city_importance.head(5).plot(kind='bar')
plt.title('Top 5 Cities by Importance')
plt.xlabel('City')
plt.ylabel('Importance')
plt.show()
