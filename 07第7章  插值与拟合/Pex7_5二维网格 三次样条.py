#程序文件名Pex7_5.py
from mpl_toolkits import mplot3d #导入三维绘图模块
import matplotlib.pyplot as plt #导入二维绘图模块
import numpy as np #导入数值计算模块
from numpy.linalg import norm #导入范数函数
from scipy.interpolate import interp2d #导入二维插值函数

z = np.loadtxt("E:/数学/数模/Python-MEM-PD-master/07第7章  插值与拟合/Pdata7_5.txt") #加载高程数据，z是一个13x15的矩阵
x = np.arange(0, 1500, 100) #生成x坐标，从0到1400，间隔为100，共15个点
y = np.arange(1200, -100, -100) #生成y坐标，从1200到0，间隔为-100，共13个点
f = interp2d(x, y, z, 'cubic') #用三次样条插值函数f对高程数据进行插值
xn = np.linspace(0, 1400, 141) #生成新的x坐标，从0到1400，间隔为10，共141个点
yn = np.linspace(0, 1200, 121) #生成新的y坐标，从0到1200，间隔为10，共121个点
zn = f(xn, yn) #用插值函数f计算新的高程数据，zn是一个121x141的矩阵

m = len(xn) #获取新的x坐标的长度，即141
n = len(yn) #获取新的y坐标的长度，即121
s = 0 #初始化区域面积为0
for i in np.arange(m-1): #遍历新的x坐标的每一个点，除了最后一个
    for j in np.arange(n-1): #遍历新的y坐标的每一个点，除了最后一个
        p1 = np.array([xn[i], yn[j], zn[j,i]]) #定义第一个顶点p1，是一个三维向量，包含x,y,z坐标
        p2 = np.array([xn[i+1], yn[j], zn[j,i+1]]) #定义第二个顶点p2，是p1右边相邻的点
        p3 = np.array([xn[i+1], yn[j+1], zn[j+1,i+1]]) #定义第三个顶点p3，是p2右上方相邻的点
        p4 = np.array([xn[i], yn[j+1], zn[j+1,i]]) #定义第四个顶点p4，是p1上方相邻的点
        p12 = norm(p1-p2) #计算p1和p2之间的距离，即向量p1-p2的范数
        p23 = norm(p3-p2) #计算p2和p3之间的距离，即向量p3-p2的范数
        p13 = norm(p3-p1) #计算p1和p3之间的距离，即向量p3-p1的范数
        p14 = norm(p4-p1) #计算p1和p4之间的距离，即向量p4-p1的范数
        p34 = norm(p4-p3) #计算p3和p4之间的距离，即向量p4-p3的范数
        L1 = (p12 + p23 + p13) / 2 #计算由p1,p2,p3组成的三角形的半周长
        s1 = np.sqrt(L1 * (L1 - p12) * (L1 - p23) * (L1 - p13)) #用海伦公式计算由p1,p2,p3组成的三角形的面积
        L2 = (p13 + p14 + p34) / 2 #计算由p1,p3,p4组成的三角形的半周长
        s2 = np.sqrt(L2 * (L2 - p13) * (L2 - p14) * (L2 - p34)) #用海伦公式计算由p1,p3,p4组成的三角形的面积
        s = s + s1 + s2 #将两个三角形的面积累加到区域面积中
print("区域的面积为：", s) #打印区域面积的结果

plt.rc('font', size=16) #设置字体大小为16
plt.rc('text', usetex=True) #设置使用LaTeX渲染文本
plt.subplot(121) #创建一个1行2列的子图，选择第一个子图
contr = plt.contour(xn, yn, zn) #绘制等高线图
plt.clabel(contr) #添加等高线标签
plt.xlabel('$x$') #设置x轴标签为x
plt.ylabel('$y$', rotation=90) #设置y轴标签为y，旋转90度
ax = plt.subplot(122, projection='3d') #创建一个1行2列的子图，选择第二个子图，设置为三维投影
X, Y = np.meshgrid(xn, yn) #生成网格点坐标矩阵
ax.plot_surface(X, Y, zn, cmap='viridis') #绘制三维曲面图，设置颜色映射为viridis
ax.set_xlabel('$x$') #设置x轴标签为x
ax.set_ylabel('$y$') #设置y轴标签为y
ax.set_zlabel('$z$') #设置z轴标签为z
plt.savefig('figure7_5.png', dpi=500) #保存图片为figure7_5.png，分辨率为500dpi
plt.show() #显示图片
