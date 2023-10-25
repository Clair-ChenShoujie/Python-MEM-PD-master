import numpy as np
import pandas as pd

# 读取目标样数据
df1 = pd.read_excel("2023华数B/附件1.xlsx")
df3 = pd.read_excel("2023华数B/附件3.xlsx")
sums = []

# 遍历X,Y,Z列
results = np.zeros((10, 3))
for j in range(1, 11):
    for i in range(1, 4):
        data1 = df1.iloc[2:19, i].values.astype('float64')
        data2 = df3.iloc[j, 1:17].values.astype('float64')

        # 进行元素相乘
        result = np.multiply(data1, data2) * 20 * 0.1
        print("样品",j,"\n",format(i), result,"\n")
        results[j-1, i-1] = np.sum(result)

# 输出结果
for j in range(10):
    print(f"目标样本{j+1}的结果：", results[j])

# 保存为xlsx文件
df_results = pd.DataFrame(results, columns=['X', 'Y', 'Z'])
df_results.to_excel("2023华数B/目标样XYZ.xlsx", index=False)