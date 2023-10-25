import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

List = [(0,1,1),(0,2,2),(0,4,7),(0,6,4),(0,7,8),(1,2,2),(1,3,3),
        (1,7,7),(2,3,1),(2,4,5),(3,4,3),(3,5,6),(4,5,4),(4,6,3),
        (5,6,6),(5,7,4),(6,7,2)]

G = nx.Graph()
G.add_weighted_edges_from(List)

source = 3
target = 7

p = nx.dijkstra_path(G, source=source, target=target, weight='weight')  #求最短路径；
d = nx.dijkstra_path_length(G, source, target, weight='weight') #求最短距离

print("最短路径为：", p, "；最短距离为：", d)

# 绘制最短路径图
pos = nx.spring_layout(G)  # 选择布局

# 获取最短路径中的所有节点
path_nodes = p

# 获取最短路径中的所有边
path_edges = list(zip(p, p[1:]))

# 将最短路径中的节点和边标记为红色
node_colors = ['red' if node in path_nodes else 'blue' for node in G.nodes()]
node_sizes = [500 if node in path_nodes else 300 for node in G.nodes()]
edge_colors = ['red' if edge in path_edges else 'black' for edge in G.edges()]
edge_widths = [2 if edge in path_edges else 1 for edge in G.edges()]

nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=node_sizes, width=edge_widths)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Shortest Path Highlighted')
plt.axis('off')  # 去掉坐标轴
plt.show()
