import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.metrics import r2_score
import os
x0 = np.array([0.05, 0.1, 0.5, 1, 2, 3, 4, 5])/100

# 设置 R^2 的增长阈值
r2_growth_threshold = 0.001

################################################# 红
df1 = pd.read_excel("2023test2/附件2.xlsx",sheet_name="红ks", header=None)
polyfit_red = {}

for column in df1.columns:
    y = df1[column].values
    # best_degree = 0
    # highest_r2 = float('-inf')
    # # 遍历不同的多项式阶数
    # for degree in range(1, 4):  # 从1阶开始到3阶
    #     p = np.polyfit(x0, y, degree)# 线性拟合
    #     y_pred = np.polyval(p, x0)# 计算 R^2 值
    #     r2 = r2_score(y, y_pred)
    #     if degree > 1 and (r2 - highest_r2) < r2_growth_threshold: break    # 判断 R^2 的增长是否低于阈值
    #     if r2 > highest_r2: 
    #         best_degree = degree
    #         highest_r2 = r2
    # # 使用最优的阶数重新拟合数据
    p = np.polyfit(x0, y, 1)
    polyfit_red[column] = p
    print(p)
print()
################################################ 黄色
df2 = pd.read_excel("2023test2/附件2.xlsx",sheet_name="黄ks", header=None)
polyfit_yel = {}

for column in df2.columns:
    y = df2[column].values
    # best_degree = 0
    # highest_r2 = float('-inf')
    # for degree in range(1, 4):
    #     p = np.polyfit(x0, y, degree)
    #     y_pred = np.polyval(p, x0)
    #     r2 = r2_score(y, y_pred)
    #     if degree > 1 and (r2 - highest_r2) < r2_growth_threshold:
    #         break
    #     if r2 > highest_r2:
    #         best_degree = degree
    #         highest_r2 = r2
    p = np.polyfit(x0, y, 1)
    polyfit_yel[column] = p
    print(p)
print()
################################################## 蓝色
df3 = pd.read_excel("2023test2/附件2.xlsx",sheet_name="蓝ks", header=None)
polyfit_blu = {}

for column in df3.columns:
    y = df3[column].values
    # best_degree = 0
    # highest_r2 = float('-inf')
    # for degree in range(1, 4):
    #     p = np.polyfit(x0, y, degree)
    #     y_pred = np.polyval(p, x0)
    #     r2 = r2_score(y, y_pred)
    #     if degree > 1 and (r2 - highest_r2) < r2_growth_threshold:
    #         break
    #     if r2 > highest_r2:
    #         best_degree = degree
    #         highest_r2 = r2
    p = np.polyfit(x0, y, 1)
    polyfit_blu[column] = p
    print(p)
###################################################### ks函数，#第一个是0到16左闭右开波长索引，第二个是浓度
# 参数是数组（16个波长的索引，浓度）
def red_ks(arr, x):
    result = []
    for column_name in arr:
        p = polyfit_red[column_name]
        result.append(np.polyval(p, x))
    return result
def yel_ks(arr, x):
    result = []
    for column_name in arr:
        p = polyfit_yel[column_name]
        result.append(np.polyval(p, x))
    return result
def blu_ks(arr, x):
    result = []
    for column_name in arr:
        p = polyfit_blu[column_name]
        result.append(np.polyval(p, x))
    return result
#################################################################
