from random import *
import numpy as np
from sympy import *


points_x = [1,2,3]
points_y = [randint(1,100)  for i in range(3)]
print(points_x)
x = symbols('x')

def polyLagrange(points_x):
    x = symbols('x')
    li_num = [1]
    li_den = [1]
    li = []
    for j in range(len(points_x)):
        for i in range(len(points_x)):
            if i != j:
                print(li_num)
                li_num.append(sympify(((x-points_x[i])*np.prod(li_num))))
                li_den.append(sympify(points_x[j]-points_x[i])*np.prod(li_den))
            else:
                li.append(1)
        li.append(sympify(li_num[j]/li_den[j]))
    return li

print(polyLagrange(points_x=points_x))