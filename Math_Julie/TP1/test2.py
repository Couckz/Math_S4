import numpy as np
import matplotlib.pyplot as plt
import math
n = 20
points_x = np.linspace(-1,1,n) 
points_y = [1/(1+25*i**2) for i in points_x]
    
def li_Lagrange(points_x, points_y):
    li = []  #Définition d'une liste qui contiendra tous les polynômes "li" de Lagrange
    Polynome_Interpolé = [] #Définition d'une variable qui contiendra le polynôme interpolé
    X = np.linspace(-1, 1, 300)
    Y = [1/(1+25*x**2) for x in X]
    for x in X: 
        P_évalué = 0
        for j in range(len(points_x)):
            li = 1
            for i in range(len(points_x)):
                if i != j:
                    li *= (x - points_x[i]) / (points_x[j] - points_x[i])
            P_évalué += points_y[j] * li
        Polynome_Interpolé.append(P_évalué)
    
    return Polynome_Interpolé, Y, X
    
def affichage(points_x, points_y):
    resultat = li_Lagrange(points_x, points_y)
    plt.plot(resultat[2], resultat[1], label="fonction choisie")
    plt.plot(resultat[2], resultat[0], label="Polynome interpolé")
    plt.title(f"Polynomé interpolé et polynôme choisit, pour n = {n}")
    plt.legend()
    plt.show()

#Fonction qui gère le calcul de l'erreur
def erreur(n):
    n_valeur = [i for i in range(2,n+1)]
    log_erreur = []
    log_n = []
    for n in n_valeur:
        points_x = np.linspace(-1,1,n) 
        points_y = [1/(1+25*i**2) for i in points_x]
        resultat = li_Lagrange(points_x, points_y)
        Polynome = np.array(resultat[0])
        Fonction = np.array(resultat[1])
        erreur = np.max(np.abs(Fonction - Polynome))
        log_erreur.append(np.log10(erreur))
        log_n.append(np.log10(n))
    plt.plot(log_n, log_erreur)
    plt.title(f"Logarithme de l'erreur en fonction du logarithme de n, pour  n = {n}")
    plt.show()

affichage(points_x, points_y)
erreur(n)