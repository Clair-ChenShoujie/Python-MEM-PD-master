import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima.arima import auto_arima

# 加载数据
data1 = pd.read_excel('2023test1/B1/attachment1.xlsx')
two_cities = data1[(data1['Delivering city'] == 'L') & (data1['Receiving city'] == 'K')]
two_cities_byTime = two_cities.groupby('Date Y/M/D')['Express delivery quantity (PCS)'].sum()
total = data1.groupby('Date Y/M/D')['Express delivery quantity (PCS)'].sum()

# 删除缺失值
two_cities_byTime = two_cities_byTime.dropna()
total = total.dropna()

# 时间序列图
#two_cities_byTime.plot() #Q2-1
total.plot() #Q2-2
plt.show()

# ACF 和 PACF 图
#plot_acf(two_cities_byTime) #Q2-1
#plot_pacf(two_cities_byTime) #Q2-1
plot_acf(total) #Q2-2
plot_pacf(total) #Q2-2
plt.show()

# 利用auto_arima自动寻找最优ARIMA模型参数
model_autoARIMA = auto_arima(total, start_p=0, start_q=0, #第一个参数是 two or total
                      test='adf',       # 使用adf检验来寻找最优的差分d
                      max_p=5, max_q=5, # 最大的AR和MA阶数
                      m=1,              # 频数
                      d=None,           # 没有开始的差分阶数
                      seasonal=False,   # 无季节性
                      start_P=0, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)

# 打印最优模型
print(model_autoARIMA.summary())

# # AIC, BIC and HQIC
# print(f"AIC of the model: {model_autoARIMA.aic()}")
# print(f"BIC of the model: {model_autoARIMA.bic()}")

# 预测某一天的数据
prediction = model_autoARIMA.predict(n_periods=2)
print(f"Prediction for April 18, 2019: \n{prediction}")
