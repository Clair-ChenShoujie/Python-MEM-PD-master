#程序文件名Pex7_8.py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

y = lambda x, a, b, c: a*x**2+b*x+c

x0 = np.arange(0, 1.1, 0.1)
y0 = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])

popt, pcov = curve_fit(y, x0, y0)

print("拟合的参数值：", popt)
print("预测值分别为：", y(np.array([0.25, 0.35]), *popt))

plt.scatter(x0, y0) #画出散点图
x = np.linspace(0, 1, 100)
plt.plot(x, y(x, *popt)) #画出拟合的曲线
plt.show()