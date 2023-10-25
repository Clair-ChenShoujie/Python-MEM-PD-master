#程序文件Pex8_5.py
from scipy.integrate import odeint
from sympy.abc import t
import numpy as np
import matplotlib.pyplot as plt
# 定义了一个二阶常微分方程，并转换成一阶
def Pfun(y,x):
    y0, y1=y #y0=原函数y,y1=一阶导y'
    return np.array([y1, -2*y0-2*y1])
x=np.arange(0, 10, 0.1)  #创建时间点
sol1=odeint(Pfun, [0.0, 1.0], x)  #求数值解：函数，初始值，自变量
print("x={}\n对应的数值解y={}".format(x, sol1.T))
plt.rc('font',size=16); plt.rc('font',family='SimHei')
plt.plot(x, sol1[:,0],'r*',label="数值解")
plt.plot(x, np.exp(-x)*np.sin(x), 'g', label="符号解曲线") #代入符号解
plt.legend(); plt.savefig("figure8_5.png"); plt.show()
