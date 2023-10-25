# 程序文件Pex5_1.py
from scipy.optimize import linprog
import numpy as np

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
bound = ((None, None), (-3, None)) #x1 x2范围
res = linprog(c, A, b, None, None, bound)
print("目标函数的最小值：", res.fun)
print("最优解为：", res.x)#如果全输出就写res


# ----------换个语法-------------

c = np.array([-1, 4])
A = np.array([[-3,1],[1,2]]) # 不等号 用<=表示
b = np.array([6,4])
Aeq = None # 等号
beq = None
x1 = (None,None)# bound 
x2 = (-3,None)
bound = (x1,x2)

res = linprog(c, A, b, Aeq, beq, bound)
print("目标函数的最小值：", res.fun)
print("最优解为：", res.x)