#程序文件Pex18_4
#季节模型常用于分析和预测那些具有明显季节性变化的数据，例如旅游业收入、零售业销售额等。
import numpy as np
a=np.loadtxt('E:/数学/数模/Python-MEM-PD-master/18第18章  时间序列分析/Pdata18_4.txt')
m,n=a.shape
amean=a.mean()  #计算所有数据的平均值
cmean=a.mean(axis=0)   #逐列求均值
r=cmean/amean   #计算季节系数
w=np.arange(1,m+1) #年份序号
yh=w.dot(a.sum(axis=1))/w.sum()  #计算下一年的预测值
yj=yh/n   #计算预测年份的季度平均值
yjh=yj*r  #计算季度预测值
print("下一年度各季度的预测值为：",yjh)
