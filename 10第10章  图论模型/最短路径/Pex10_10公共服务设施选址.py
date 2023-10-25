#程序文件Pex10_10.py
import numpy as np
import networkx as nx

List=[(0,1,20),(0,4,15),(1,2,20),(1,3,40),
      (1,4,25),(2,3,30),(2,4,10),(4,5,15)]
G=nx.Graph()
G.add_nodes_from(range(6))
G.add_weighted_edges_from(List)
c=dict(nx.shortest_path_length(G,weight='weight'))
d=np.zeros((6,6))
for i in range(6):
    for j in range(6): d[i,j]=c[i][j]
print(d)

q=np.array([80,90,30,20,60,10])
m=d@q  #计算运力，这里使用矩阵乘法
mm=m.min()  #求运力的最小值
ind=np.where(m==mm)[0]  #python下标从0开始，np.where返回值为元组
print("运力m=",m,'\n最小运力mm=',mm,"\n选矿厂的设置位置为：",ind+1) #索引4，位置5
