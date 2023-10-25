# 程序文件Pex7_10.py
from mpl_toolkits import mplot3d
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def Pfun(t, m1, m2, s):
    return np.exp(-((t[0] - m1) ** 2 + (t[1] - m2) ** 2) / (2 * s ** 2))

m = 200
n = 300
x = np.linspace(-6, 6, m) # -6到6的m个等间隔数字
y = np.linspace(-8, 8, n) # -8到8的m个等间隔数字
x2, y2 = np.meshgrid(x, y) #转换为二维网格，两个(n, m)二维数组
x3 = np.reshape(x2, (1, -1)) #转换为一维数组
y3 = np.reshape(y2, (1, -1)) #转换为一维数组
xy = np.vstack((x3, y3)) #x3 y3压缩成一维数组

z = Pfun(xy, 1, 2, 3)
zr = z + 0.2 * np.random.normal(size=z.shape)  # 噪声数据
popt, pcov = curve_fit(Pfun, xy, zr)  # 拟合参数 xy自变量(一维) zr因变量
print("三个参数的拟合值分别为：", popt)

zn = Pfun(xy, *popt)  #计算拟合函数的值
zn2 = np.reshape(zn, x2.shape) #一维转成二维
plt.rc("font", size=16)
ax = plt.axes(projection="3d")  #创建一个三维坐标轴对象
ax.plot_surface(x2, y2, zn2, cmap="gist_rainbow")
plt.savefig("figure7_10.png", dpi=500)
plt.show()
