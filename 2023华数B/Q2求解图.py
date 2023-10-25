import matplotlib.pyplot as plt

# 获取解决方案
solution = [(1, 2), (10, 154), (2, 89), (3, 89), (4, 18), (5, 18), (6, 2), (7, 34), (8, 217), (9, 18)]

# 解析目标样和配方
target_samples = [i[0] for i in solution]
formulas = [i[1] for i in solution]

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(target_samples, formulas)
plt.xlabel('Target Sample')
plt.ylabel('Formula')
plt.title('Matching between Target Sample and Formula')

# 添加坐标点的数据标签
for i, j in zip(target_samples, formulas):
    plt.text(i, j, f'({i}, {j})', ha='center', va='bottom')

plt.show()
