import pandas as pd
from pulp import *

# 从xlsx文件中读取色差数据和成本数据
data = pd.read_excel('2023华数B/Q4_5目标色差.xlsx')
cost_data = pd.read_excel('2023华数B/Q3成本.xlsx')

# 建立一个名为 'ColorMatch' 的问题
prob = LpProblem('ColorMatch', LpMinimize)

# 定义决策变量
x = LpVariable.dicts('x', [(i,j) for i in range(1, 6) for j in range(1, 729)], 0, 1, LpInteger)
y = LpVariable.dicts('y', [i for i in range(1, 729)], 0, 1, LpInteger)

# 计算色差和成本的平均值
average_delta = data['色差'].mean()
average_cost = cost_data['成本'].mean()
print("average_delta",average_delta)
print("average_cost",average_cost)

# 定义目标函数
Z1 = lpSum([x[(i, j)] * data.loc[(data['目标样'] == '目标样{}'.format(i)) & (data['标准样'] == '标准样{}'.format(j)), '色差'].values[0] for i in range(1, 6) for j in range(1, 729)]) / average_delta
Z2 = lpSum([y[j] * cost_data.loc[j-1, '成本'] for j in range(1, 729)]) / average_cost
prob += 0.2 * Z1 + 0.8 * Z2

# 加入约束条件1：每个目标样本都有5个配色方案
for i in range(1, 6):
    prob += lpSum([x[(i, j)] for j in range(1, 729)]) == 5

# 加入约束条件2：确保总用量为25
prob += lpSum([x[(i, j)] for i in range(1, 6) for j in range(1, 729)]) == 25
prob += lpSum([y[j] for j in range(1, 729)]) == 25

# 加入约束条件3：确保色差小于1
for i in range(1, 6):
    for j in range(1, 729):
        if data.loc[(data['目标样'] == '目标样{}'.format(i)) & (data['标准样'] == '标准样{}'.format(j)), '色差'].values[0] > 1:
            prob += x[(i, j)] == 0

# 加入约束条件4：确保选择的配方对应的 y_n 为 1
for i in range(1, 6):
    for j in range(1, 729):
        prob += y[j] >= x[(i, j)]

# 求解问题
prob.solve()

# 打印结果
for v in prob.variables():
    if value(v) != 0:
        print(v.name, "=", v.varValue)
