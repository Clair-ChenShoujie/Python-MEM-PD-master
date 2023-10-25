import pandas as pd
import numpy as np

# 读取标准样比值数据
df = pd.read_excel("2023华数B/标准样比值.xlsx")

# 初始化存储 L*, a*, b* 的 DataFrame
lab_df = pd.DataFrame(columns=['L*', 'a*', 'b*'])

# 对每一行数据进行遍历计算
for index, row in df.iterrows():
    X_ratio, Y_ratio, Z_ratio = row['Xj/X0'], row['Yj/Y0'], row['Zj/Z0']
    L_star = 116 * np.cbrt(Y_ratio) - 16
    a_star = 500 * (np.cbrt(X_ratio) - np.cbrt(Y_ratio))
    b_star = 200 * (np.cbrt(Y_ratio) - np.cbrt(Z_ratio))
    lab_df.loc[index] = [L_star, a_star, b_star]

# 保存结果到新的xlsx文件
lab_df.to_excel("2023华数B/标准样LAB.xlsx", index=False)
