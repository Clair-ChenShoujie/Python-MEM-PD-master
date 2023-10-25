import pandas as pd
import numpy as np
from pulp import *
import matplotlib.pyplot as plt

# 从xlsx文件中读取数据
data = pd.read_excel('2023华数B/色差.xlsx')

# 建立一个名为 'ColorMatch' 的问题
prob = LpProblem('ColorMatch', LpMinimize)

# 定义决策变量，注意要定义为整数类型
x = LpVariable.dicts('x', [(i,j) for i in range(1, 11) for j in range(1, 729)], 0, 1, LpInteger)

# 定义目标函数
prob += lpSum([x[(i, j)] * data.loc[(data['目标样'] == '目标样{}'.format(i)) & (data['标准样'] == '标准样{}'.format(j)), '色差'].values[0] for i in range(1, 11) for j in range(1, 729)])

# 加入约束条件1：每个目标样本都有且只有一个配方
for i in range(1, 11):
    prob += lpSum([x[(i, j)] for j in range(1, 729)]) == 1

# 加入约束条件2：确保总用量为10
prob += lpSum([x[(i, j)] for i in range(1, 11) for j in range(1, 729)]) == 10

""" # 加入约束条件3：确保色差小于1
for i in range(1, 11):
    for j in range(1, 729):
        if data.loc[(data['目标样'] == '目标样{}'.format(i)) & (data['标准样'] == '标准样{}'.format(j)), '色差'].values[0] > 1:
            prob += x[(i, j)] == 0
 """
# 求解问题
prob.solve()

for v in prob.variables():
    if value(v) != 0:
        print(v.name, "=", v)

