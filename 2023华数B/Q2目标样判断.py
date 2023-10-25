import pandas as pd
df1 = pd.read_excel("2023华数B/目标样XYZ.xlsx")# 读取目标样数据
y = df1.iloc[0:10, 0:3] 
x0 = 94.83;y0 = 100.00;z0 = 107.38# 定义初始值
y1_divided = y / [x0, y0, z0]# 计算除法结果
print(y1_divided)
y1_divided.columns = ['Xj/X0', 'Yj/Y0', 'Zj/Z0']
# 保存为xlsx文件，包括属性和数据
with pd.ExcelWriter("2023华数B/目标样比值.xlsx") as writer:
    y1_divided.to_excel(writer, index=False, sheet_name="Sheet1")