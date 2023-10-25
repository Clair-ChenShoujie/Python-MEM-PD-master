#程序文件Pex10_2_1.py
import numpy as np
import networkx as nx
import pylab as plt
a=np.zeros((5,5))
a[0,1:5]=[9, 2, 4, 7]; a[1,2:4]=[3,4]
a[2,[3,4]]=[8, 4]; #输入邻接矩阵的上三角元素
a[3,4]=6; print(a); np.savetxt("Pdata10_2.txt",a) #保存邻接矩阵供以后使用

i,j=np.nonzero(a)  #提取顶点的编号（索引）作为起点和终点
w=a[i,j]  #提出a中的非零元素，边的权重
edges=list(zip(i,j,w)) #将边的起点、终点和权重打包成元组，并转换成列表

G=nx.Graph()
G.add_weighted_edges_from(edges) #向图G中添加带权边

key=range(5); s=[str(i+1) for i in range(5)]
s=dict(zip(key,s))  #创建一个字典s，用于将节点编号映射到节点标签

plt.rc('font',size=18)

# 绘制图G
plt.subplot(121); nx.draw(G,font_weight='bold',labels=s) 

# 绘制带权重标注的图G

plt.subplot(122); pos=nx.shell_layout(G)  #布局设置
nx.draw_networkx(G,pos,node_size=260,labels=s)
w = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,font_size=12,edge_labels=w) 

plt.savefig("figure10_2.png", dpi=500); 
plt.show()

""" 
创建一个空的无向图G。
向图G中添加带权边。
设置图G的布局。
使用draw_networkx方法绘制图G。
使用get_edge_attributes方法获取边的权重。
使用draw_networkx_edge_labels方法绘制边的权重标注。
"""
G = nx.Graph()
G.add_weighted_edges_from(edges)
pos = nx.shell_layout(G)
nx.draw_networkx(G, pos, node_size=260, labels=s)
w = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, font_size=12, edge_labels=w)
"""
其中，edges是一个包含边的起点、终点和权重的元组列表，s是一个将节点编号映射到节点标签的字典。
"""