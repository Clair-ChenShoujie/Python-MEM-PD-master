#程序文件Pex12_7.py
import numpy as np
import statsmodels.api as sm

#以下为可修改内容
a=np.loadtxt("E:/数学/数模/Python-MEM-PD-master/12第12章  回归分析/Pdata12_7_1.txt") #加载表中x,ni,mi的9行3列数据
x=a[:,0]# 第一列 自变量收入
pi=a[:,2]/a[:,1]# 第三列除第二列 因变量实际买房比例
X=sm.add_constant(x); yi=np.log(pi/(1-pi))
md=sm.OLS(yi,X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果
b=md.params  #提出所有的回归系数
""" 
a = np.loadtxt("data.txt") # 加载数据文件
x1 = a[:,0] # 提取第一个自变量
x2 = a[:,1] # 提取第二个自变量
x3 = a[:,2] # 提取第三个自变量
y = a[:,3] # 提取因变量
X = sm.add_constant(np.column_stack((x1, x2, x3))) # 构建增广矩阵
md = sm.OLS(y, X).fit() # 构建并拟合模型
b = md.params # 提取回归系数
 """
p0=1/(1+np.exp(-np.dot(b,[1,9])))
""" 
# 这里的[1,9]的9，就是x_value，即第9年
p0 = 1 / (1 + np.exp(-np.dot(b, [1, x1_value, x2_value, x3_value])))
 """
print("所求概率p0=%.4f"%p0)
np.savetxt("E:/数学/数模/Python-MEM-PD-master/12第12章  回归分析/Pdata12_7_2.txt", b)  #把回归系数保存到文本文件
