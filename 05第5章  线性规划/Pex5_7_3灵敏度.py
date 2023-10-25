from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

# 定义你的模型输入参数
problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-np.pi, np.pi]]*3
}

# 生成样本
param_values = saltelli.sample(problem, 1000)

# 在模型中运行参数，获取输出
Y = Ishigami.evaluate(param_values)

# 进行Sobol分析
Si = sobol.analyze(problem, Y)

print(Si)
