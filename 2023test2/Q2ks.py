# 读取数据
import numpy as np
import pandas as pd
from Q1 import red_ks,yel_ks,blu_ks

num_simulations = 50  
des = 1

##################################
# 三色

ks0 = [0.039492, 0.025906, 0.017964, 0.015092, 0.011439, 0.009515, 0.007961, 0.006947, 0.006284, 0.005889, 0.005238, 0.004948, 0.004626, 0.004247, 0.004100, 0.003617]
arr = np.arange(16)

red_des = np.random.uniform(0, 0.05, (num_simulations, num_simulations, num_simulations)) * des
yel_des = np.random.uniform(0, 0.01, (num_simulations, num_simulations, num_simulations)) * des
blu_des = np.random.uniform(0, 0.01, (num_simulations, num_simulations, num_simulations)) * des

ks0 = np.array(ks0)

ks = np.array([ks0 + red_ks(arr, red) + yel_ks(arr, yel) + blu_ks(arr, blu) for red, yel, blu in zip(red_des.ravel(), yel_des.ravel(), blu_des.ravel())])
df2 = pd.DataFrame(ks)

# 将数据写入Excel文件
df2.to_excel('2023test2/三色ks.xlsx', index=False)