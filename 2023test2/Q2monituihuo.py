import math
import random
import import_ipynb
import pandas as pd
import matplotlib.pyplot as plt
from Q1 import red_ks,yel_ks,blu_ks
import numpy as np


# 输入X/X0,Y/Y0,Z/Z0，计算LAB

def calculate_lab(XYZ_divided):
    X_ratio, Y_ratio, Z_ratio = XYZ_divided
    L_star = 116 * np.cbrt(Y_ratio) - 16
    a_star = 500 * (np.cbrt(X_ratio) - np.cbrt(Y_ratio))
    b_star = 200 * (np.cbrt(Y_ratio) - np.cbrt(Z_ratio))
    return np.array([L_star,a_star,b_star])

def ks():
    # 配方的ks,1*16波长
    ks0 = [0.039492, 0.025906, 0.017964, 0.015092, 0.011439, 0.009515, 0.007961, 0.006947, 0.006284, 0.005889, 0.005238, 0.004948, 0.004626, 0.004247, 0.004100, 0.003617]
    arr = np.arange(16)
    
    red_des = round(np.random.uniform(0, 0.05), 4)
    yel_des = round(np.random.uniform(0, 0.05), 4)
    blu_des = round(np.random.uniform(0, 0.05), 4)

    # 应该是每个列直接相加而非横向连接
    npks = np.sum([ks0, red_ks(arr, red_des),yel_ks(arr, yel_des),blu_ks(arr, blu_des)] ,axis=0)
    R = 1 + npks - np.sqrt(npks**2 + 2*npks)
    return R,red_des,yel_des,blu_des


# 输入16*1的R,计算配方的LAB，return目标样和标准样的LAB

# 先ks=ks()然后用LAB(ks),return LAB
def LAB(R):
    dfXYZ = pd.read_excel("2023test2/附件1.xlsx")
    npXYZ = np.array(dfXYZ)
    Sxyz = npXYZ[2:18, 1:4]  # 16*3
    R = R.reshape(-1, 1)  # reshape R to 16*1 for broadcasting
    result = np.multiply(R, Sxyz) * 20 * 0.1  # Broadcasting happens here
    lab_xyz = np.sum(result, axis=0)  # 标准样的xyz，一维长度3

    # 标准样判断，Xj/X0, Yj/Y0, Zj/Z0
    x0 = 94.83
    y0 = 100.00
    z0 = 107.38
    y_divided = lab_xyz / [x0, y0, z0]
    
    # 读取目标样和标准样数据
    lab = calculate_lab(y_divided)
    return lab

# R,red_des,yel_des,blu_des = ks()
# lab = LAB(R)
# print(R)
# print(lab)

def simulated_annealing(i, initial_temp=5000, final_temp=0.1, cooling_rate=0.99, max_iter_per_temp=100):
    """Simulated annealing algorithm for minimizing color difference.
    
    Args:
        i (int): The index of the aim.
        initial_temp (float, optional): The initial temperature for the simulated annealing. Default is 5000.
        final_temp (float, optional): The final temperature for the simulated annealing. Default is 0.1.
        cooling_rate (float, optional): The cooling rate for the simulated annealing. Default is 0.99.
        max_iter_per_temp (int, optional): The maximum number of iterations per temperature. Default is 100.

    Returns:
        tuple: The best solution and the corresponding color difference.
    """
    
    # Initialize the current solution and best solution
    current_solution = ks()
    best_solution = current_solution
    current_cost = aim(i, current_solution)[3]
    best_cost = current_cost
    

    # Main loop
    temp = initial_temp
    while temp > final_temp:
        for _ in range(max_iter_per_temp):
            # Generate a new solution randomly
            R,red_des,yel_des,blu_des = ks()
            new_solution = ks()
            new_cost = aim(i, R, red_des, yel_des, blu_des)[3]


            # If the new solution is better, update the current solution and best solution
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution = new_solution
                current_cost = new_cost
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost

        # Cool down
        temp *= cooling_rate

    return best_solution, best_cost
    

def aim(i, R, red_des, yel_des, blu_des):
    lab_LAB=LAB(R)
    print(R,lab_LAB)
    aim_df = pd.read_excel("2023test2/目标样LAB.xlsx")
    aim_LAB = [np.array(aim_df)[i-1] for i in range(10)]
    print(aim_LAB) #索引i，然后是10个目标样的LAB长度3
    # 计算色差
    color_differences = []
    
    diff = aim_LAB[i-1] - lab_LAB
    delta_L, delta_a, delta_b = diff
    delta_E = np.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
    return red_des ,yel_des, blu_des,delta_E


# Test the function
print(simulated_annealing(1))
