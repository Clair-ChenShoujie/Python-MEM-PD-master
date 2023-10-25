#程序文件Pex13_4.py
import numpy as np
from numpy.linalg import eig, inv
from matplotlib.pyplot import bar, show, legend, rc, plot
rc('font',size=16); rc('font',family='SimHei')

# 1
L=np.array([[0,4,3],[0.5,0,0],[0,0.25,0]])#转移矩阵
X=1000*np.ones((3,1)); TX=np.zeros((3,5))#初始人口数量1000，未来五年的人口数量

for i in range(5): X=L.dot(X); TX[:,i]=X.flatten()
print("TX=",TX)#range参数为5，计算未来5年人口数量

for i in range(3): bar(np.arange(1,6)-0.25+i/4,TX[i],width=0.2)#arrange(1,未来年份+1)
legend(('幼龄组','二龄组','三龄组')); show()
""" 在这行代码中，np.arange(1,6) 生成一个从 1 到 5 的一维数组，表示条形图的 x 坐标。
-0.25+i/4 是一个偏移量，用来调整每个条形图的位置，使得不同年龄组的条形图不会重叠。
TX[i] 表示第 i 个年龄组未来 5 年每一年的人口数量，用来设置条形图的高度。
width=0.2 表示条形图的宽度为 0.2 """

# 2
val,vec=eig(L)  #计算特征值及对应的特征向量
cv=inv(vec).dot(1000*np.ones(3)); c=abs(cv[0])#1k是初始人口数量，3是组数量
print("特征值=",val,"\n特征向量为：\n",vec,'\nc=',c)#这里最大特征值1.5对应特征向量是[0.9474,0.3158,0.0526]T

s=int(input("输入s的值:")); m=10  #s是每年人口减少的数量（死亡,迁移），计算m=10年
TY=[]; Y=np.ones(3)*1000; TY=np.zeros((m,3))
for i in range(1,m+1):
    Y=L.dot(Y)-s*np.ones(3); TY[i-1,:]=Y.flatten()
plot(np.arange(1,m+1),TY)
legend(('幼龄组','二龄组','三龄组')); show()

""" 
这段代码使用 numpy 和 matplotlib 库来模拟一个人口增长模型并绘制条形图和折线图。

首先，导入所需的库和函数。然后，定义矩阵 `L`，它表示人口增长的转移矩阵。定义初始人口数量 `X` 为一个 3x1 的矩阵，所有元素都为 1000。定义矩阵 `TX` 用来存储每一年的人口数量。

接下来，使用一个 for 循环来计算未来 5 年的人口数量。在每次循环中，首先使用 `dot` 函数计算矩阵 `L` 和矩阵 `X` 的乘积，并将结果赋值给 `X`。然后使用 `flatten` 函数将矩阵 `X` 压平为一维数组，并将结果存储在矩阵 `TX` 的第 `i` 列。

在循环结束后，打印出矩阵 `TX` 的值。然后使用另一个 for 循环绘制条形图。在每次循环中，使用 `bar` 函数绘制条形图。最后使用 `legend` 函数添加图例并使用 `show` 函数显示图形。

接下来，代码计算矩阵 `L` 的特征值和特征向量，并打印出结果。然后提示用户输入变量 `s` 的值，并定义变量 `m=10` 表示计算未来 10 年的人口数量。

接下来，使用一个 for 循环来计算未来 10 年的人口数量。在每次循环中，首先计算新的人口数量并存储在矩阵 `TY` 中。最后使用 `plot` 函数绘制折线图并使用 `legend` 和 `show` 函数添加图例并显示图形。
 """