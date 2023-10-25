#程序文件Pex5_6.py
import cvxpy as cp
import numpy as np
import pandas as pd
d1=pd.read_excel("E:/数学/数模/Python-MEM-PD-master/05第5章  线性规划/Pdata5_6.xlsx",header=None)
d2=d1.values; c=d2[:-1,:-1]
d=d2[-1,:-1].reshape(1,-1); e=d2[:-1,-1].reshape(-1,1)

x=cp.Variable((6,8)) #决策变量x，6行8列

obj=cp.Minimize(cp.sum(cp.multiply(c,x)))  #构造目标函数，c和x的逐元素乘积之和。

con=[cp.sum(x,axis=1,keepdims=True)<=e, #(这是同一句代码) axis参数，指定沿着哪个轴执行数组操作，二维数组有2个轴
cp.sum(x,axis=0,keepdims=True)==d,x>=0] #构造约束条件，包括每行之和小于等于e、每列之和等于d，x大于等于0。

prob=cp.Problem(obj,con)  #构造模型

prob.solve(solver='GLPK_MI',verbose =True)    #求解模型
print("最优值为：",prob.value)
print("最优解为：\n",x.value)

