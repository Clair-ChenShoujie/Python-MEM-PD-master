#程序文件Pex18_6.py
#非平稳时间序列则常用于分析和预测那些具有明显趋势或周期性变化的数据，例如股票价格、经济增长率等。

import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import pylab as plt
from statsmodels.tsa.arima_model import ARIMA

plt.rc('axes',unicode_minus=False)
plt.rc('font',size=16); plt.rc('font',family='SimHei')
df=pd.read_csv('E:\数学\数模\Python-MEM-PD-master/18第18章  时间序列分析/austa.csv')
plt.subplot(121); plt.plot(df.value.diff())
plt.title('一次差分')
ax2=plt.subplot(122)
plot_acf(df.value.diff().dropna(), ax=ax2,title='自相关')

md=ARIMA(df.value, order=(2,1,0))
mdf=md.fit(disp=0)
print(mdf.summary())

residuals = pd.DataFrame(mdf.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="残差", ax=ax[0])
residuals.plot(kind='kde', title='密度', ax=ax[1])
plt.legend(''); plt.ylabel('')          

mdf.plot_predict()  #原始数据与预测值对比图
plt.show()

