import numpy as np
from lmfit import Model
import matplotlib.pyplot as plt

def y(x, m, r):
    return m / (1 + (m / 3.9 - 1) * np.exp(-r * (x - 1790)))

x0 = np.arange(1790, 2010, 10)
y0 = np.array([3.9, 5.3, 7.2, 9.6, 12.9, 17.1, 23.2, 31.4,
               38.6, 50.2, 62.9, 76.0, 92.0, 106.5, 123.2, 131.7,
               150.7, 179.3, 204.0, 226.5, 251.4, 281.4])

# 初始值范围
m_vals = np.linspace(1000, 20000, 10)
r_vals = np.linspace(0.1, 1.0, 10)

model = Model(y)
best_fit = None
min_error = float('inf')

for m_init in m_vals:
    for r_init in r_vals:
        try:
            result = model.fit(y0, x=x0, m=m_init, r=r_init)
            error = np.sum((y0 - result.best_fit) ** 2)

            if error < min_error:  # 保存最佳拟合
                min_error = error
                best_fit = result
        except:
            continue

if best_fit is not None:
    print("拟合的参数值：", best_fit.params)
    print("预测值分别为：", best_fit.eval(x=np.array([2030])))

    plt.scatter(x0, y0)  # 画出散点图
    x = np.linspace(1790, 2010, 22)
    plt.plot(x, best_fit.best_fit)  # 画出拟合的曲线
    plt.show()



coefficients = np.polyfit(x0, y0, deg=3) # 3表示多项式的最高次数
p = np.poly1d(coefficients)

print("多项式拟合的参数值：", coefficients)

print("预测值分别为：", p(2030))

plt.scatter(x0, y0) #画出散点图
x = np.linspace(1790, 2010, 22)
plt.plot(x, p(x)) #画出拟合的曲线
plt.show()
