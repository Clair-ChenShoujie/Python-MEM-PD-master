import numpy as np
import pandas as pd

per = np.array([60,65,63])
red_des = np.array([0.05, 0.1, 0.5, 1, 2, 3, 4, 5])/100  # 红浓度
yel_des = np.array([0.05, 0.1, 0.5, 1, 2, 3, 4, 5])/100  # 黄浓度
blu_des = np.array([0.05, 0.1, 0.5, 1, 2, 3, 4, 5])/100  # 蓝浓度

results = []

# 单色：24列浓度*2*不同的单价
for j in range(len(per)):
    for i in range(len(red_des)):
      cost = 2 * per[j] * red_des[i]
      results.append(cost)

# 双色：192列浓度*2*不同单价
# 红黄
for j in range(len(red_des)):
    for i in range(len(yel_des)):
        cost = 2 * red_des[j] * per[0] + 2 * yel_des[i] * per[1]
        results.append(cost)

# 红蓝
for j in range(len(red_des)):
    for k in range(len(blu_des)):
        cost = 2 * red_des[j] * per[0] + 2 * blu_des[k] * per[2]
        results.append(cost)

# 黄蓝
for i in range(len(yel_des)):
    for k in range(len(blu_des)):
        cost = 2 * yel_des[i] * per[1] + 2 * blu_des[k] * per[2]
        results.append(cost)
        
# 三色：8*8*8列浓度，乘2，乘不同单价
for k in range(len(blu_des)):
    for j in range(len(red_des)):
        for i in range(len(yel_des)):
            cost =  2 * red_des[j] * per[0] + 2 * yel_des[i] * per[1] + 2 * blu_des[k] * per[2]
            results.append(cost)

# 保存成本数据
df = pd.DataFrame(results)
df.to_excel('2023华数B/Q3成本.xlsx', index=False)

