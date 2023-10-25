import pandas as pd
import numpy as np
import scipy.stats as stats

# 读取附件2数据
data2 = pd.read_excel('2023test1\B1\附件2.xlsx')

# 创建一个新的列，名为 'city_pair'，值为 'Delivering city' 列的值和 'Receiving city' 列的值连接而成的
data2['city_pair'] = data2['Delivering city'] + '-' + data2['Receiving city']

# 使用 pivot_table 函数创建一个新的 DataFrame，索引为 'Date Y/M/D'，列为 'city_pair'，值为 'Express delivery quantity (PCS)'
data2_pivot = data2.pivot_table(index='Date Y/M/D', columns='city_pair', values='Express delivery quantity (PCS)')

# 将索引转换为 datetime 类型
data2_pivot.index = pd.to_datetime(data2_pivot.index)

# 剔除无发货需求数据和无法正常发货数据
data2_pivot = data2_pivot.dropna(axis=1)

# 将数据按季度分组
data2_pivot_quarterly = data2_pivot.resample('Q').agg(['min', 'mean', 'std'])

# 计算固定需求常数
fixed_demand_constants = data2_pivot_quarterly.loc[:, ('min', slice(None))]

# 计算每个季度每个“发货-收货”站点城市对的非固定需求
non_fixed_demand = data2_pivot - fixed_demand_constants.values

non_fixed_demand_quarterly = non_fixed_demand.resample('Q').agg(['mean', 'std'])

# 选择可能的概率分布
distributions = [stats.norm, stats.poisson]

# 初始化结果字典
results = {}

# 使用最大似然估计估计每个季度的非固定需求概率分布
for distribution in distributions:
    dist_name = distribution.__class__.__name__
    results[dist_name] = {}
    for quarter, quarter_data in non_fixed_demand.groupby(pd.Grouper(freq='Q')):
        params = distribution.fit(quarter_data.stack())  # Use .stack() to flatten the data
        results[dist_name][quarter] = {'params': params, 'mean': params[0], 'std': params[1]}

# 将结果填入表5
table5_non_fixed_demand = pd.DataFrame.from_dict(
    {(i, j): results[i][j] for i in results.keys() for j in results[i].keys()},
    orient='index'
).reset_index().rename(columns={'level_0': 'Distribution', 'level_1': 'Quarter'})

# 打印填充后的表5
print(table5_non_fixed_demand)
