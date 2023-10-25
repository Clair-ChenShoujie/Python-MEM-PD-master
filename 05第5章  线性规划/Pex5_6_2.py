import numpy as np
import pandas as pd
from scipy.optimize import linprog

d1 = pd.read_excel("E:\数学\数模\Python-MEM-PD-master/05第5章  线性规划\Pdata5_6.xlsx", header=None)
d2 = d1.values
c = d2[:-1, :-1].flatten()
d = d2[-1, :-1]
e = d2[:-1, -1]

A_ub = np.concatenate((np.eye(6), -np.eye(6)), axis=0)
b_ub = np.concatenate((e, np.zeros(6)), axis=0)
A_eq = np.concatenate((np.ones((1, 6)), np.zeros((1, 6))), axis=1)
b_eq = d

bound = (0, None)

res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=bound)

print("目标函数的最小值：", res.fun)
print("最优解为：\n", res.x.reshape(6, 8))
