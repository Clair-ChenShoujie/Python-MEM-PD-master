import pandas as pd
import numpy as np

# 读取目标样和标准样数据
df1 = pd.read_excel("2023华数B/目标样LAB.xlsx")
df2 = pd.read_excel("2023华数B/标准样LAB.xlsx")

data1 = df1.iloc[:, 0:3].values.astype('float64') # 目标样LAB
data2 = df2.iloc[:, 0:3].values.astype('float64') # 标准样LAB

# 嵌套循环遍历元素并计算色差
color_differences = []
for i in range(data2.shape[0]):
    for j in range(data1.shape[0]):
        diff = data1[j] - data2[i]
        print(f"目标样{j+1} - 标准样{i+1} :\t {diff}")
        # 提取三个差值并计算平方
        delta_L, delta_a, delta_b = diff
        delta_E = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
        print(f"色差 {delta_E}")
        color_differences.append([f"目标样{j+1}", f"标准样{i+1}", delta_E])

# 保存为DataFrame
df_color_differences = pd.DataFrame(color_differences, columns=['目标样', '标准样', '色差'])

# 保存为xlsx文件
df_color_differences.to_excel("2023华数B/色差.xlsx", index=False)
