#程序文件Pex12_2_1.py
# 基于公式
import numpy as np; import statsmodels.api as sm
a=np.loadtxt("E:/数学/数模/Python-MEM-PD-master/12第12章  回归分析/Pdata12_1.txt")
d={'x1':a[:,0],'x2':a[:,1],'y':a[:,2]}
md=sm.formula.ols('y~x1+x2',d).fit()  #构建并拟合模型，修改公式即可
print(md.summary(),'\n------------\n')  #显示模型所有信息
ypred=md.predict({'x1':a[:,0],'x2':a[:,1]})  #计算预测值
print(ypred)  #输出预测值