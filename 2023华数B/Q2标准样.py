import numpy as np
import pandas as pd

# 读取标准样求XYZ
df1 = pd.read_excel("2023华数B/附件1.xlsx")
df2 = pd.read_excel("2023华数B/Combined.xlsx")

results = []
num_rows_combined = df2.shape[0]

for j in range(num_rows_combined):
    result_row = []
    for i in range(1, 4):
        Sxyz = df1.iloc[2:19, i].values.astype('float64')  
        ks = df2.iloc[j, 0:16].values.astype('float64') 
        R = 1 + ks - np.sqrt(ks**2 + 2*ks) 
        result = np.multiply(Sxyz, R) * 20 * 0.1 
        result_row.append(np.sum(result))
    results.append(result_row)

df_results = pd.DataFrame(results, columns=['X', 'Y', 'Z'])

# 标准样判断
x0 = 94.83;y0 = 100.00;z0 = 107.38
y2_divided = df_results / [x0, y0, z0]
y2_divided.columns = ['Xj/X0', 'Yj/Y0', 'Zj/Z0']

# 初始化存储 L*, a*, b* 的 DataFrame
lab_df = pd.DataFrame(columns=['L*', 'a*', 'b*'])

# 对每一行数据进行遍历计算
for index, row in y2_divided.iterrows():
    X_ratio, Y_ratio, Z_ratio = row['Xj/X0'], row['Yj/Y0'], row['Zj/Z0']
    L_star = 116 * np.cbrt(Y_ratio) - 16
    a_star = 500 * (np.cbrt(X_ratio) - np.cbrt(Y_ratio))
    b_star = 200 * (np.cbrt(Y_ratio) - np.cbrt(Z_ratio))
    lab_df.loc[index] = [L_star, a_star, b_star]

# 保存结果到新的xlsx文件
lab_df.to_excel("2023华数B/标准样LAB.xlsx", index=False)