import numpy as np
import pandas as pd
from scipy.interpolate import RectBivariateSpline
from math import cos, sin, radians
from scipy.optimize import minimize

data = pd.read_excel('2023国赛/attachment.xlsx', header=None, index_col=None)
values = data.values
x = np.arange(values.shape[1])  # x坐标等于列数
y = np.arange(values.shape[0])  # y坐标等于行数
interp_func = RectBivariateSpline(y, x, values)

# 定义临界边的角度
theta = 120

# 海域范围限制
x_limit = 4*1852
y_limit = 5*1852

def objective(d):
    # 根据步长计算测线数量
    n = int(5*1852 / d)+1
    # 根据步长和测线数量计算所有测线在海域内的长度的和
    total_length = 0
    for i in range(n):
        x, y = 0, i*d
        while x < x_limit and y < y_limit:
            dx, dy = cos(radians(theta)), sin(radians(theta))
            z = interp_func.ev(y + dy, x + dx)
            total_length += np.sqrt((x + dx - x)**2 + (y + dy - y)**2 )
            x += z
            y += z

    # 计算覆盖率
    coverage = 1 - d / total_length
    # 将覆盖率考虑进目标函数中，用一个权重参数进行平衡
    weight = 1
    return weight * total_length + (1 - weight) * (1 - coverage)

d = 0.02*1852

# 用BFGS梯度下降法找到最优的测线间距
result = minimize(objective, d, method='BFGS')
optimal_d = result.x[0]

# 输出结果
print('Optimal line spacing:', optimal_d)

# 重新计算最优测线间距下的测线总长度、漏测海区占总待测海域面积的百分比和重叠率超过20%部分的总长度
n = int(np.ceil(5*1852 / optimal_d))
total_length = n * 4*1852

# 计算覆盖率
coverage = 1 - optimal_d / total_length
# 计算漏测海区面积
total_leakage = (1 - coverage) * (x_limit * y_limit)

# 计算重叠率超过20%部分的总长度
length_over_20 = 0
if coverage > 0.2:
    length_over_20 = (coverage - 0.2) * total_length

print('Total length of measuring lines:', total_length)
print('Percentage of missed sea area:', total_leakage / (x_limit * y_limit) * 100)
print('Total length of overlap over 20%:', length_over_20)