import pandas as pd
import numpy as np
from pulp import *

# 读取目标样和标准样数据
df1 = pd.read_excel("2023华数B/目标样LAB.xlsx")
df2 = pd.read_excel("2023华数B/标准样LAB.xlsx")

data1 = df1.iloc[0:10, 0:3].values.astype('float64') # 目标样LAB
data2 = df2.iloc[:, 0:3].values.astype('float64') # 标准样LAB
num_rows_combined = df2.shape[0]

# 嵌套循环遍历元素并计算色差
color_differences = []
for i in range(data2.shape[0]):
    for j in range(data1.shape[0]):
        diff = data1[j] - data2[i]
        # print(f"目标样{j+1} - 标准样{i+1} :\t {diff}")
        # 提取三个差值并计算平方
        delta_L, delta_a, delta_b = diff
        delta_E = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
        # print(f"色差 {delta_E}")
        color_differences.append([f"目标样{j+1}", f"标准样{i+1}", delta_E])

# 保存为DataFrame
df_color_differences = pd.DataFrame(color_differences, columns=['目标样', '标准样', '色差'])

# 保存为xlsx文件
df_color_differences.to_excel("2023华数B/Q2色差.xlsx", index=False)
#df_color_differences.to_excel("2023华数B/Q2色差.xlsx", index=False)

# # 从xlsx文件中读取数据
# df_color_differences = pd.read_excel('2023华数B/色差.xlsx')

# # 建立一个名为 'ColorMatch' 的问题
# prob = LpProblem('ColorMatch', LpMinimize)

# # 定义决策变量，注意要定义为整数类型
# x = LpVariable.dicts('x', [(i,j) for i in range(1, 11) for j in range(1, num_rows_combined+1)], 0, 1, LpInteger)

# # 定义目标函数
# prob += lpSum([x[(i, j)] * df_color_differences.loc[(df_color_differences['目标样'] == '目标样{}'.format(i)) & (df_color_differences['标准样'] == '标准样{}'.format(j)), '色差'].values[0] for i in range(1, 11) for j in range(1, num_rows_combined+1)])

# # 加入约束条件1：每个目标样本都有且只有一个配方
# for i in range(1, 11):
#     prob += lpSum([x[(i, j)] for j in range(1, num_rows_combined+1)]) == 1

# # 加入约束条件2：确保总用量为10
# prob += lpSum([x[(i, j)] for i in range(1, 11) for j in range(1, num_rows_combined+19)]) == 10

# # 加入约束条件3：确保色差小于1
# for i in range(1, 11):
#     for j in range(1,num_rows_combined+1):
#         if df_color_differences.loc[(df_color_differences['目标样'] == '目标样{}'.format(i)) & (df_color_differences['标准样'] == '标准样{}'.format(j)), '色差'].values[0] > 1:
#             prob += x[(i, j)] == 0

# # 求解问题
# prob.solve()

# for v in prob.variables():
#     if value(v) != 0:
#         print(v.name, "=", v)
