#程序文件名Pex7_6.py
from mpl_toolkits import mplot3d #导入三维绘图模块
import matplotlib.pyplot as plt #导入二维绘图模块
import numpy as np #导入数值计算模块
from scipy.interpolate import griddata #导入网格数据插值函数

x = np.array([129, 140, 103.5, 88, 185.5, 195, 105, 157.5, 107.5, 77, 81, 162, 162, 117.5]) #定义x坐标数组
y = np.array([7.5, 141.5, 23, 147, 22.5, 137.5, 85.5, -6.5, -81, 3, 56.5, -66.5, 84, -33.5]) #定义y坐标数组
z = -np.array([4, 8, 6, 8, 6, 8, 8, 9, 9, 8, 8, 9, 4, 9]) #定义z坐标数组，注意z数组取了负数
xy = np.vstack([x,y]).T #将x,y数组合并为一个14x2的矩阵，每一行是一个点的x,y坐标
xn = np.linspace(x.min(), x.max(), 100) #生成新的x坐标，从x的最小值到最大值，共100个点
yn = np.linspace(y.min(), y.max(), 100) #生成新的y坐标，从y的最小值到最大值，共100个点
xng, yng = np.meshgrid(xn, yn) #构造网格节点，xng和yng都是100x100的矩阵
zn = griddata(xy, z, (xng,yng), method='nearest') #用最近邻点插值方法对网格节点进行插值，得到新的高程数据zn

plt.rc('font', size=16) #设置字体大小为16
plt.rc('text', usetex=True) #设置使用LaTeX渲染文本
ax = plt.subplot(121, projection='3d') #创建一个1行2列的子图，选择第一个子图，设置为三维投影
ax.plot_surface(xng,yng ,zn ,cmap='viridis') #绘制三维曲面图，设置颜色映射为viridis
ax.set_xlabel('$x$') #设置x轴标签为x
ax.set_ylabel('$y$') #设置y轴标签为y
ax.set_zlabel('$z$') #设置z轴标签为z

plt.subplot(122) #创建一个1行2列的子图，选择第二个子图
c = plt.contour(xn ,yn ,zn ,8) #绘制等高线图，等高线数量为8
plt.clabel(c) #添加等高线标签

plt.savefig('figure7_6.png', dpi=500) #保存图片为figure7_6.png，分辨率为500dpi
plt.show() #显示图片
