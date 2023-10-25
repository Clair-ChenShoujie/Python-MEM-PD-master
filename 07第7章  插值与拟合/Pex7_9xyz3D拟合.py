#程序文件Pex7_9.py
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Pfun(t, a, b, c):
    return a*np.exp(b*t[0])+c*t[1]**2

x0=np.array([6, 2, 6, 7, 4, 2, 5, 9])
y0=np.array([4, 9, 5, 3, 8, 5, 8, 2])
z0=np.array([5, 2, 1, 9, 7, 4, 3, 3])
xy0=np.vstack((x0,y0))

popt, pcov=curve_fit(Pfun, xy0, z0)
print("a，b，c的拟合值为：", popt)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x0,y0,z0) #画出散点图

x = np.linspace(min(x0), max(x0), 30)
y = np.linspace(min(y0), max(y0), 30)
x,y = np.meshgrid(x,y)
z = Pfun(np.vstack((x.flatten(),y.flatten())),*popt).reshape(x.shape)

ax.plot_surface(x,y,z,alpha=0.5)
plt.show()
