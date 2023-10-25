#程序文件Pex18_3
import numpy as np
import pandas as pd
y=np.loadtxt('E:/数学/数模/Python-MEM-PD-master/18第18章  时间序列分析/Pdata18_3.txt')

# y,alpha,s1[0],s2[0]
n=len(y); alpha=0.3; yh=np.zeros(n)
s1=np.zeros(n); s2=np.zeros(n)
s1[0]=y[0]; s2[0]=y[0]

for i in range(1,n):
    # 公式
    s1[i]=alpha*y[i]+(1-alpha)*s1[i-1]
    s2[i]=alpha*s1[i]+(1-alpha)*s2[i-1]
    yh[i]=2*s1[i-1]-s2[i-1]+alpha/(1-alpha)*(s1[i-1]-s2[i-1])
    
# 直线趋势模型
at=2*s1[-1]-s2[-1]; bt=alpha/(1-alpha)*(s1[-1]-s2[-1])
m=np.array([1,2]) #预测未来n年，这里是1，2
yh2=at+bt*m

print("直线趋势方程","y=",at,"+",bt,"*m")
print("预测值为：",yh2)
d=pd.DataFrame(np.c_[s1,s2,yh])
f=pd.ExcelWriter("Pdata18_3.xlsx")
d.to_excel(f); f.close()


