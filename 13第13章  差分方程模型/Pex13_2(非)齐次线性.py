#程序文件Pex13_2.py
import sympy as sp
sp.var('k'); sp.var('y',cls=sp.Function)
f = y(k+1)-y(k)-3-2*k
f1 = sp.rsolve(f, y(k)); 
f2 = sp.simplify(f1)
print(f2)

# or 用func定义函数y

from sympy import Function, rsolve
from sympy.abc import k
y = Function('y')
f = y(k+1)-y(k)-3-2*k
f1 = sp.rsolve(f, y(k)); 
#f2 = sp.simplify(f1)
print(f2)



""" # 常系数(非)齐次线性差分方程解法模板
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