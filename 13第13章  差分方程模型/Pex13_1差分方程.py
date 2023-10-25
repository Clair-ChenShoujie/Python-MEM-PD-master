#程序文件Pex13_1.py
from sympy import Function, rsolve
from sympy.abc import n
y = Function('y')
f=y(n+2)-y(n+1)-y(n)
ff=rsolve(f, y(n),{y(1):1,y(2):1})
print(ff)


""" 

from sympy import Function, rsolve
from sympy.abc import n

# 定义符号函数
y = Function('y')

# 定义递归方程
f = ... # 递归方程

# 求解递归方程
ff = rsolve(f, y(n), ...) # 初始条件（可选）

# 打印结果

print(ff) """
