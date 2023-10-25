import numpy as np

alpha = 1.5
theta = 120
half_theta = theta/2
alpha = np.radians(alpha)
half_theta = np.radians(half_theta)

d = 200
det_D = d * np.tan(alpha)
D = [70 + 4 * det_D - i * det_D for i in range(9)]
print(D)

W = []
eta = []
for i in range(0, 9):
    W.append(np.cos(alpha)*D[i]*np.sin(half_theta)*(1/(np.sin(np.pi/2+alpha-half_theta))+1/(np.sin(np.pi/2-alpha-half_theta))))
    eta.append(1-d/W[i])

print(W)
print(eta)