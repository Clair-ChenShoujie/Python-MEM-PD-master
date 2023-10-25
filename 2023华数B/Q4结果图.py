import matplotlib.pyplot as plt
import seaborn as sns

results = {
    'x_(1,_154)': 1.0,
    'x_(1,_17)': 1.0,
    'x_(1,_2)': 1.0,
    'x_(1,_225)': 1.0,
    'x_(1,_33)': 1.0,
    'x_(2,_17)': 1.0,
    'x_(2,_18)': 2.0,
    'x_(2,_281)': 1.0,
    'x_(2,_89)': 1.0,
    'x_(3,_1)': 1.0,
    'x_(3,_17)': 1.0,
    'x_(3,_2)': 1.0,
    'x_(3,_225)': 1.0,
    'x_(3,_89)': 1.0,
    'x_(4,_155)': 1.0,
    'x_(4,_17)': 1.0,
    'x_(4,_18)': 1.0,
    'x_(4,_281)': 1.0,
    'x_(4,_89)': 1.0,
    'x_(5,_1)': 1.0,
    'x_(5,_154)': 1.0,
    'x_(5,_18)': 1.0,
    'x_(5,_281)': 1.0,
    'x_(5,_89)': 1.0,
}

# 提取样本和配方编号
samples = [int(key.split('_')[1][1:-1]) for key in results.keys()]
formulas = [int(key.split('_')[2][0:-1]) for key in results.keys()]

# 使用seaborn设置美化图表
sns.set_theme()

# 对每个样本创建一个子图
fig, axs = plt.subplots(1, 5, figsize=(20, 10), sharey=True)

# 遍历每个样本
for i in range(1, 6):
    # 提取当前样本的配方
    sample_formulas = [formula for sample, formula in zip(samples, formulas) if sample == i]
    
    # 对当前样本创建条形图
    barplot = sns.barplot(x=list(range(len(sample_formulas))), y=sample_formulas, ax=axs[i-1], palette="Blues_d")
    axs[i-1].set_title('Sample {}'.format(i), fontsize=16)
    axs[i-1].set_xlabel('Formula Index', fontsize=14)
    for tick in axs[i-1].xaxis.get_major_ticks():
        tick.label.set_fontsize(12) 
    for tick in axs[i-1].yaxis.get_major_ticks():
        tick.label.set_fontsize(12)

    # 在条形图上添加文本标签
    for rect in barplot.patches:
        height = rect.get_height()
        axs[i-1].text(rect.get_x() + rect.get_width() / 2., height,
                '%d' % int(height), ha='center', va='bottom', fontsize=12)

# 设置y轴标签
axs[0].set_ylabel('Formula Number', fontsize=14)

# 自动调整子图间距和边距
plt.tight_layout()
plt.show()
