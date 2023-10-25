from sklearn.cluster import KMeans
import numpy as np

# 构造数据样本点集X，并计算K-means聚类
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# n_clusters聚类中心的数量，其他都是默认值
kmeans = KMeans(n_clusters=2, random_state=0 , n_init=10).fit(X)

# 输出及聚类后的每个样本点的标签（即类别），预测新的样本点所属类别
print(kmeans.labels_)
print(kmeans.predict([[0, 0], [4, 4], [2, 1]]))
