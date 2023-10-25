import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.metrics import r2_score
import os

# 读取数据
df = pd.read_excel("2023华数B/附件2.xlsx")
x0 = np.array([0.05, 0.1, 0.5, 1, 2, 3, 4, 5])/100

# 定义行范围和对应的文件夹名
row_range = [(2, 9), (10, 17), (18, 25)]
folder_names = ["红", "黄", "蓝"]

# 设置 R^2 的增长阈值
r2_growth_threshold = 0.001

# 定义一个函数，将拟合参数转化为函数表达式字符串
def poly_2_expr(p):
    res = ""
    for i, coef in enumerate(p):
        if i == 0:
            res += f'{coef:.4f}*x**{len(p) - i - 1}'
        elif i == len(p) - 1:
            res += f' + {coef:.4f}'
        else:
            res += f' + {coef:.4f}*x**{len(p) - i - 1}'
    return res

# 遍历不同的行范围和文件夹名
for row_idx, folder_name in enumerate(folder_names):
    # 创建一个空的 DataFrame 用来保存拟合的函数表达式
    df_fit = pd.DataFrame(index=range(2, 18), columns=['400nm', '420nm', '440nm', '460nm', '480nm', '500nm', '520nm', '540nm', '560nm', '580nm', '600nm', '620nm', '640nm', '660nm', '680nm', '700nm'])
    
    # 创建3D图形对象
    fig = go.Figure()
    
    # 遍历不同的列
    for col in range(2, 18):
        row_start, row_end = row_range[row_idx]
        y0 = df.iloc[row_start:row_end + 1, col].values.astype('float64')

        # 初始化最优的模型参数
        best_degree = 0
        highest_r2 = float('-inf')

        # 遍历不同的多项式阶数
        for degree in range(1, 4):  # 从1阶开始到3阶
            # 线性拟合
            p = np.polyfit(x0, y0, degree)
            # 计算 R^2 值
            y_pred = np.polyval(p, x0)
            r2 = r2_score(y0, y_pred)
            # 判断 R^2 的增长是否低于阈值
            if degree > 1 and (r2 - highest_r2) < r2_growth_threshold:
                break
            if r2 > highest_r2:
                best_degree = degree
                highest_r2 = r2

        # 使用最优的阶数重新拟合数据
        p = np.polyfit(x0, y0, best_degree)

        # 计算拟合曲线上的点
        x_fit = np.linspace(min(x0), max(x0), 100)
        y_fit = np.polyval(p, x_fit)

        # 计算拟合曲线与XOZ面的垂足坐标
        x_perpendicular = -p[1] / (2 * p[0])  # 拟合曲线的顶点坐标（x坐标）
        y_perpendicular = np.polyval(p, x_perpendicular)  # 拟合曲线的顶点坐标（y坐标）
    
        # 添加拟合曲线到3D图形
        fig.add_trace(go.Scatter3d(x=x_fit, y=y_fit, z=np.repeat(col * 20 + 380, len(x_fit)), mode='lines'))

    
        # 保存拟合的函数表达式
        df_fit.loc[col] = poly_2_expr(p)

    # 设置3D图形的布局
    fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    width=700,
                    margin=dict(r=20, b=10, l=10, t=10))
    
    # 显示3D图形
    fig.show()

    # 保存拟合的函数表达式到Excel文件
    df_fit.to_excel(f'2023华数B/{folder_name}拟合.xlsx')
