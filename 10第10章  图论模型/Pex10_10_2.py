import numpy as np
import networkx as nx
import pylab as plt

#定义邻接矩阵，0表示节点间没有边
Adj_matrix = np.array([
    [0, 20, 0, 0, 15, 0],
    [0,  0, 20, 40, 25, 0],
    [0,  0, 0, 30, 10, 0],
    [0,  0, 0, 0, 0, 0],
    [0,  0, 0, 0, 0, 15],
    [0,  0, 0, 0, 0, 0]
])

G = nx.from_numpy_array(Adj_matrix, create_using=nx.DiGraph)

d=nx.dijkstra_path_length(G, 0, 5, weight='weight') #求最短距离
print("所求的费用最小值为：",d)

p=nx.dijkstra_path(G, source=0, target=5, weight='weight')  #求最短路径；
print("最短路径为:",np.array(p)+1)  #python下标从0开始

q=np.array([80,90,30,20,60,10])
m=d@q  #计算运力，这里使用矩阵乘法
mm=m.min()  #求运力的最小值
ind=np.where(m==mm)[0]+1  #python下标从0开始，np.where返回值为元组
print("运力m=",m,'\n最小运力mm=',mm,"\n选矿厂的设置位置为：",ind)

s=dict(zip(range(6),range(1,7))) #构造用于顶点标注的标号字典
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w=nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,font_weight='bold',labels=s,node_color='r')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(p,p[1:]))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            edge_color='r',width=3)
plt.show()
