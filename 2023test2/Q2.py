import numpy as np
import pandas as pd
from Q1 import red_ks,yel_ks,blu_ks
from pulp import *

num_simulations = 10 
des = 0.5

##################################
# 三色
ks0 = [0.039492, 0.025906, 0.017964, 0.015092, 0.011439, 0.009515, 0.007961, 0.006947, 0.006284, 0.005889, 0.005238, 0.004948, 0.004626, 0.004247, 0.004100, 0.003617]
arr = np.arange(16)

red_des = np.random.uniform(0, 0.05, (num_simulations, num_simulations, num_simulations)) * des
yel_des = np.random.uniform(0, 0.01, (num_simulations, num_simulations, num_simulations)) * des
blu_des = np.random.uniform(0, 0.01, (num_simulations, num_simulations, num_simulations)) * des

ks0 = np.array(ks0)

ks = np.array([ks0 + red_ks(arr, red) + yel_ks(arr, yel) + blu_ks(arr, blu) for red, yel, blu in zip(red_des.ravel(), yel_des.ravel(), blu_des.ravel())])
df2 = pd.DataFrame(ks)


##############################################
# 读取标准样求XYZ
df1 = pd.read_excel("2023test2/附件1.xlsx")

Sxyz = df1.iloc[2:19, 1:4].values.astype('float64')  
ks = df2.values.astype('float64') 
R = 1 + ks - np.sqrt(ks**2 + 2*ks) 
result = np.dot(R, Sxyz) * 20 * 0.1 
df_results = pd.DataFrame(result, columns=['X', 'Y', 'Z'])

# 标准样判断
x0 = 94.83
y0 = 100.00
z0 = 107.38
y2_divided = df_results / [x0, y0, z0]
y2_divided.columns = ['Xj/X0', 'Yj/Y0', 'Zj/Z0']

def calculate_lab(row):
    X_ratio, Y_ratio, Z_ratio = row['Xj/X0'], row['Yj/Y0'], row['Zj/Z0']
    L_star = 116 * np.cbrt(Y_ratio) - 16
    a_star = 500 * (np.cbrt(X_ratio) - np.cbrt(Y_ratio))
    b_star = 200 * (np.cbrt(Y_ratio) - np.cbrt(Z_ratio))
    return pd.Series([L_star, a_star, b_star], index=['L*', 'a*', 'b*'])

lab_df = y2_divided.apply(calculate_lab, axis=1)


#### 

# 读取目标样和标准样数据
aim_df = pd.read_excel("2023test2/目标样LAB.xlsx")

data1 = aim_df.iloc[0:10, 0:3].values.astype('float64') # 目标样LAB
data2 = lab_df.iloc[:, 0:3].values.astype('float64') # 标准样LAB
num_rows_combined = lab_df.shape[0]

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

# # 保存为xlsx文件
# df_color_differences.to_excel("2023test2/Q2色差.xlsx", index=False)

# ###

# # 从xlsx文件中读取数据
# df_color_differences = pd.read_excel('2023test2/色差.xlsx')

# 建立一个名为 'ColorMatch' 的问题
prob = LpProblem('ColorMatch', LpMinimize)

# 定义决策变量，注意要定义为整数类型
x = LpVariable.dicts('x', [(i,j) for i in range(1, 11) for j in range(1, num_rows_combined+1)], 0, 1, LpInteger)

# 定义目标函数
prob += lpSum([x[(i, j)] * df_color_differences.loc[(df_color_differences['目标样'] == '目标样{}'.format(i)) & (df_color_differences['标准样'] == '标准样{}'.format(j)), '色差'].values[0] for i in range(1, 11) for j in range(1, num_rows_combined+1)])

# 加入约束条件1：每个目标样本都有且只有一个配方
for i in range(1, 11):
    prob += lpSum([x[(i, j)] for j in range(1, num_rows_combined+1)]) == 1

# 加入约束条件2：确保总用量为10
prob += lpSum([x[(i, j)] for i in range(1, 11) for j in range(1, num_rows_combined+1)]) == 10

# # 加入约束条件3：确保色差小于1
# for i in range(1, 11):
#     for j in range(1,num_rows_combined+1):
#         if df_color_differences.loc[(df_color_differences['目标样'] == '目标样{}'.format(i)) & (df_color_differences['标准样'] == '标准样{}'.format(j)), '色差'].values[0] > 1:
#             prob += x[(i, j)] == 0

# 求解问题
prob.solve()

for v in prob.variables():
    if value(v) != 0:
        print(v.name, "=", v)