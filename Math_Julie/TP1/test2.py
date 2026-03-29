from random import *
import sympy as symp
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import math


# Définition de trois points dont les coordonnées (x,y) sont respectivement les valeurs de points_x et points_y
# On choisit pour l'études des points par lesquels passent la fonction choisie 

n = 5

points_x = linspace(-1,1,n) 
points_y = [1/(1+25*i**2) for i in points_x]

def li_Lagrange(points_x, points_y):
    x = symp.symbols('x') #"Symbols" est une fonction de sympy qui définit la variable utilisée pour les calculs formels, ici x. 
    li = []  #Définition d'une liste qui contiendra tous les polynômes "li" de Lagrange
    Polynome_Interpolé = 0 #Définition d'une variable qui contiendra le polynôme interpolé
    pol_choisit = 1/(1+25*x**2)
    #Itération sur les indices des points, servant à calculer les "li" de Lagrange
    for j in range(len(points_x)):
        li_num = 1  #Définition de la variable qui contiendra le numérateur du li calculé pour le points indicé j
        li_den = 1 #Définition de la variable qui contiendra le dénumérateur du li calculé pour le points indicé j
        
        #Interation une deuxième fois sur les indices des points. 
        #Essentielle pour éviter l'intervention du terme x-xi dans le calcul du "li" de Lagrange
        for i in range(len(points_x)):
            #Test pour éviter le terme xi-xi dans le calcul des li de Lagrange, d'où l'intervention de la deuxième boucle
            if i != j:
                li_num = (x-points_x[i])*li_num # Implémentation du calcul du numérateur pour le li de lagrange pour le point j
                li_den = (points_x[j]-points_x[i])*li_den # Implémentation du calcul du dénominateur pour le li de lagrange pour le point j
        li.append(symp.sympify(li_num/li_den)) #Ajout du li calculé en simplifiant son expression formellement par la fonction sympify
    
    #Boucle servant à calculer le polyome interpolé 
    for k in range(len(points_y)):
        Polynome_Interpolé += symp.sympify(li[k]*points_y[k])
    #print(symp.sympify(symp.expand(Polynome_Interpolé)))
    #Affichage du polynôme interpolé et du polynôme choisit
    #symp.plot((Polynome_Interpolé, (x, min(points_x)-1, max(points_x)+1), "Polynome de lagrange"), 
        #(pol_choisit, (x, min(points_x)-1, max(points_x)+1), "Fonction choisie" ), legend=True)
    return pol_choisit, symp.sympify(symp.expand(Polynome_Interpolé)), len(points_x)

def erreur(tuple):
    pass
print("le résultat est ", li_Lagrange(points_x, points_y))