import numpy as np

L = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1])*1852
beta_values = [0,45,90,135,180,225,270,315]
for beta in beta_values:
    beta = np.radians(beta)
    det_d = L*np.cos(beta)
    alpha0 = 1.5
    alpha0 = np.radians(alpha0)
    D = 120 + det_d*np.tan(alpha0)
    tan_alpha_2 = np.tan(alpha0)*np.sin(beta)
    alpha2 = np.arctan(tan_alpha_2)
    theta = 120
    half_theta = theta/2
    half_theta = np.radians(half_theta)

    W = []
    for i in range(0, 8):
        W.append(np.cos(alpha2)*D[i]*np.sin(half_theta)*(1/(np.sin(np.pi/2+alpha2-half_theta))+1/(np.sin(np.pi/2-alpha2-half_theta))))

    print(f'beta: {np.degrees(beta)},\nW: {W}\n')