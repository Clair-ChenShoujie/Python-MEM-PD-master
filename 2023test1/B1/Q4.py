import numpy as np
import pandas as pd
from scipy.optimize import linprog

# 读取附件2数据
data2 = pd.read_excel('2023test1\B1\附件2.xlsx')

# 创建一个新的列，名为 'city_pair'，值为 'Delivering city' 列的值和 'Receiving city' 列的值连接而成的
data2['city_pair'] = data2['Delivering city'] + '-' + data2['Receiving city']

# 使用 pivot_table 函数创建一个新的 DataFrame，索引为 'Date Y/M/D'，列为 'city_pair'，值为 'Express delivery quantity (PCS)'
data2_pivot = data2.pivot_table(index='Date Y/M/D', columns='city_pair', values='Express delivery quantity (PCS)')

# 将索引转换为 datetime 类型
data2_pivot.index = pd.to_datetime(data2_pivot.index)

# 读取附件3数据
data3 = pd.read_excel('2023test1\B1\附件3.xlsx')

# 获取所有城市
cities = list(set(data3['City A']).union(set(data3['City B'])))

# 构建成本矩阵
num_cities = len(cities)
cost_matrix = np.full((num_cities, num_cities), np.inf)

for index, row in data3.iterrows():
    city_a = cities.index(row['City A'])
    city_b = cities.index(row['City B'])
    fixed_cost = row['Fixed cost']
    rated_capacity = row['Rated capacity']
    key = row['City A'] + '-' + row['City B']
    if key not in data2_pivot.columns:
        continue
    cost_matrix[city_a, city_b] = fixed_cost * (1 + (data2_pivot.loc[:, key].sum() / rated_capacity)**3)
    cost_matrix[city_b, city_a] = cost_matrix[city_a, city_b]

# 检查cost_matrix是否包含inf或nan
if np.isinf(cost_matrix).any() or np.isnan(cost_matrix).any():
    # 使用一个大的有限值替换inf
    cost_matrix[np.isinf(cost_matrix)] = 1e10
    # 使用0替换nan
    cost_matrix[np.isnan(cost_matrix)] = 0

# 检查demand_matrix是否包含inf或nan
demand_matrix=[]
if np.isinf(demand_matrix).any() or np.isnan(demand_matrix).any():
    # 使用一个大的有限值替换inf
    demand_matrix[np.isinf(demand_matrix)] = 1e10
    # 使用0替换nan
    demand_matrix[np.isnan(demand_matrix)] = 0

# 定义线性规划问题
def min_transportation_cost(cost_matrix, demand_matrix):
    num_cities = cost_matrix.shape[0]
    c = cost_matrix.flatten()
    A_eq = []
    b_eq = []
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                constraint = np.zeros((num_cities, num_cities))
                constraint[i, j] = 1
                constraint[j, i] = -1
                A_eq.append(constraint.flatten())
                b_eq.append(demand_matrix[i, j])
                
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    result = linprog(c, A_eq=A_eq, b_eq=b_eq)
    if result.success:
        return result.fun
    else:
        print("Optimization failed:", result.message)
        return None


# 计算每日最低运输成本
daily_min_cost = []

for date in pd.date_range('2023-04-23', '2023-04-27'):
    demand_matrix = np.zeros((num_cities, num_cities))
    for city_pair, quantity in data2_pivot.loc[date].items():
        city_a, city_b = city_pair.split('-')
        demand_matrix[cities.index(city_a), cities.index(city_b)] = quantity
    # 检查demand_matrix是否包含inf或nan
    if np.isinf(demand_matrix).any() or np.isnan(demand_matrix).any():
        # 使用一个大的有限值替换inf
        demand_matrix[np.isinf(demand_matrix)] = 1e10
        # 使用0替换nan
        demand_matrix[np.isnan(demand_matrix)] = 0
    daily_min_cost.append(min_transportation_cost(cost_matrix, demand_matrix))

# 将结果填入表4
table4 = pd.DataFrame({'Date': pd.date_range('2023-04-23', '2023-04-27'), 'Minimum Transportation Cost': daily_min_cost})
print(table4)
