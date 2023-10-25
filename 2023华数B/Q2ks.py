# 读取数据
import numpy as np
import pandas as pd

num_simulations = 100  # number of simulations
############################
# 单色
df2 = pd.read_excel("2023华数B/附件2.xlsx",sheet_name="标准ks", header=None)
ks_single = df2.iloc[0:3, 0:16].values.astype('float64')  # k/s

result = np.empty((3, num_simulations, ks_single.shape[1]), dtype=float)  # 创建一个空的三维数组,一维颜色，二维浓度，三维波长

np.random.seed(0)  # for reproducibility
# 对每个颜色数组进行操作
for i in range(ks_single.shape[0]):
    for j in range(num_simulations):
        v = np.random.uniform(0, 0.051)/100
        result[i, j, :] = np.multiply(ks_single[i, :], v)

# 将三维数组转换为二维数组，然后转换为 Pandas DataFrame
result_flat = result.reshape(-1, result.shape[-1])
result_df = pd.DataFrame(result_flat)

# 保存到 Excel
result_df.to_excel("2023华数B/Q2单色.xlsx", index=False)

#############################
# 双色

df2 = pd.read_excel("2023华数B/附件2.xlsx", sheet_name="标准ks", header=None)
ks1 = df2.iloc[0:3, 0:16].values.astype('float64')  # k/s
ks0 = [0.039492, 0.025906, 0.017964, 0.015092, 0.011439, 0.009515, 0.007961, 0.006947, 0.006284, 0.005889, 0.005238, 0.004948, 0.004626, 0.004247, 0.004100, 0.003617]

results = []

# 红黄
for j in range(num_simulations):
    red_des = np.random.uniform(0, 0.051)/100  # 红浓度
    for i in range(num_simulations):
        yel_des = np.random.uniform(0, 0.051)/100  # 黄浓度
        ks = ks0 + red_des * ks1[0, :] + yel_des * ks1[1, :]
        results.append(ks)

# 红蓝
for j in range(num_simulations):
    red_des = np.random.uniform(0, 0.051)/100  # 红浓度
    for k in range(num_simulations):
        blu_des = np.random.uniform(0, 0.051)/100  # 蓝浓度
        ks = ks0 + red_des * ks1[0, :] + blu_des * ks1[2, :]
        results.append(ks)

# 黄蓝
for i in range(num_simulations):
    yel_des = np.random.uniform(0, 0.051)/100  # 黄浓度
    for k in range(num_simulations):
        blu_des = np.random.uniform(0, 0.051)/100  # 蓝浓度
        ks = ks0 + yel_des * ks1[1, :] + blu_des * ks1[2, :]
        results.append(ks)

# 创建DataFrame对象
df = pd.DataFrame(results)

# 将数据写入Excel文件
df.to_excel('2023华数B/二色.xlsx', index=False)

##################################
# 三色
df2 = pd.read_excel("2023华数B/附件2.xlsx", sheet_name="标准ks", header=None)
ks1 = df2.iloc[0:3, 0:16].values.astype('float64')  # k/s
ks0 = [0.039492, 0.025906, 0.017964, 0.015092, 0.011439, 0.009515, 0.007961, 0.006947, 0.006284, 0.005889, 0.005238, 0.004948, 0.004626, 0.004247, 0.004100, 0.003617]

results = []

# 红黄蓝
for k in range(num_simulations):
    red_des = np.random.uniform(0, 0.051)/100  # 红浓度
    for j in range(num_simulations):
        yel_des = np.random.uniform(0, 0.051)/100  # 黄浓度
        for i in range(num_simulations):                
            blu_des = np.random.uniform(0, 0.051)/100  # 蓝浓度
            ks = ks0 + red_des * ks1[0, :] + yel_des * ks1[1, :] + blu_des * ks1[2, :]
            results.append(ks)
            
# 创建DataFrame对象
df = pd.DataFrame(results)

# 将数据写入Excel文件
df.to_excel('2023华数B/三色.xlsx', index=False)

# ##################################
# # 合并
# # 读取三个文件
# df_single = pd.read_excel("2023华数B/Q2单色.xlsx")
# df_double = pd.read_excel("2023华数B/二色.xlsx")
# df_triple = pd.read_excel("2023华数B/三色.xlsx")

# # 删除每个数据帧的第一行（属性行）
# df_double = df_double.iloc[1:]
# df_triple = df_triple.iloc[1:]

# # 合并数据帧
# df_combined = pd.concat([df_single, df_double, df_triple])

# # 写入Excel
# df_combined.to_excel("2023华数B/Combined.xlsx", index=False)
