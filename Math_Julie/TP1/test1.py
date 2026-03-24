from random import *
import numpy as np
from sympy import *

points_x = [0,1,2]
points_y = [1,3,9]
print(points_x)
x = symbols('x')

def li_Lagrange(points_x, points_y):
    x = symbols('x')
    li = []
    res = 0
    for j in range(len(points_x)):
        li_num = 1
        li_den = 1
        for i in range(len(points_x)):
            if i != j:
                print(li_num)
                li_num = (x-points_x[i])*li_num
                li_den = (points_x[j]-points_x[i])*li_den
        li.append(sympify(li_num/li_den))
        
    for k in range(len(points_y)):
        res += sympify(li[k]*points_y[k])
    return sympify(res)

print("le résultat est ", li_Lagrange(points_x, points_y))
