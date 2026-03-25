from random import *
import sympy as symp
from numpy import *
import matplotlib.pyplot as plt

points_x = linspace(-1,1,3) 
points_y = [1/(1+25*i**2) for i in points_x]
print(points_x)
x = symp.symbols('x')

def li_Lagrange(points_x, points_y):
    x = symp.symbols('x')
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
        li.append(symp.sympify(li_num/li_den))
        
    for k in range(len(points_y)):
        res += symp.sympify(li[k]*points_y[k])
    print(symp.expand(res))
    pol_choisit = 1/(1+25*x**2)
    symp.plot((res, (x, min(points_x)-1, max(points_x)+1), "Polynome de lagrange"), (pol_choisit, (x, min(points_x)-1, max(points_x)+1), "Fonction choisie" ), legend=True)
    symp.plot((symp.log(symp.Abs((symp.sympify(pol_choisit-res)))), (x, log10(min(points_x)-1), log10(max(points_x)+1)), "Erreur représentée" ) )
    return symp.sympify(symp.expand(res))

print("le résultat est ", li_Lagrange(points_x, points_y))