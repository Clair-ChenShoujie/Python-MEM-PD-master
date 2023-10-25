import numpy as np

a = 4*1852
b = 2*1852
pace = 0.3*1852
theta = 120
half_theta = theta/2
alpha0 = 1.5
alpha0 = np.radians(alpha0)
half_theta = np.radians(half_theta)

beta_values = np.radians(np.arange(0, 181))
d_values = np.arange(10, 320, 10)

min_value = np.inf
min_parameters = [None, None]
min_num = np.inf

for beta in beta_values:
    for d in d_values:
        side = abs(a*np.cos(beta)) + b*np.sin(beta)
        front = a*np.sin(beta) + abs(b*np.cos(beta))

        n_side = 2*int(0.5*side/pace)+1
        n_half_front_ex0 = int(0.5*front/d)

        count_cast_x = pace*n_side*abs(np.cos(beta))
        count_cast_y = pace*n_side*abs(np.sin(beta))

        x_main = np.linspace(-count_cast_x/2, count_cast_x/2, n_side)
        y_main = np.linspace(-count_cast_y/2, count_cast_y/2, n_side)
        
        i_values = np.arange(-n_half_front_ex0, n_half_front_ex0 + 1)

        x_values = x_main[np.newaxis, :] - np.outer(i_values, d*np.sin(beta))
        y_values = y_main[np.newaxis, :] + np.outer(i_values, d*np.cos(beta))

        x_all = np.vstack((x_main, x_values))
        y_all = np.vstack((y_main, y_values))
        
        x_values = np.clip(x_values, -2, 2)
        y_values = np.clip(y_values, -1, 1)
        
        position = np.vstack((x_values.flatten(), y_values.flatten()))

        D = 110 + position[0, :] * np.tan(alpha0)
        D = D.reshape((2*n_half_front_ex0+1, n_side))

        tan_alpha_2 = np.tan(alpha0)*np.sin(beta)
        alpha2 = np.arctan(tan_alpha_2)

        W = np.zeros(D.shape)
        eta = np.zeros(D.shape)

        for i in range(D.shape[0]):
            for j in range(D.shape[1]):
                # 根据公式计算W的对应元素
                W[i, j] = np.cos(alpha2) * D[i, j] * np.sin(half_theta) * (1 / (np.sin(np.pi / 2 + alpha2 - half_theta)) + 1 / (np.sin(np.pi / 2 - alpha2 - half_theta)))
                eta[i, j] = d / W[i, j]
        
        s = (2*(n_half_front_ex0)+1)*side
        duan = abs(b*np.cos(beta))-a*np.sin(beta)
        n_duan = 2*int(0.5*duan/d)+1
        dd = n_duan * (a*abs(np.cos(beta))-b*np.sin(beta))
        c = (s-dd)/2
        
        # 检查约束条件
        if np.all((eta >= 0.1) & (eta <= 0.2)):
            print(beta)
            # 计算目标函数
            objective = c+dd
            print(objective,'\n')
            # 检查是否优于之前的最小值
            if objective < min_value:
                min_value = objective
                min_parameters = [np.degrees(beta), d]
                min_num = 2*int(n_half_front_ex0)+1

print("最小值: ", min_value)
print("最优参数 [beta (in degrees), d]: ", min_parameters)