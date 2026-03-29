import numpy as np
import matplotlib.pyplot as plt
import math

n = 5 #Nombre de points d'interpolation considéré
points_x = np.linspace(-1,1,n) #Creation d'un intervalle de points avec le nombre de points considéré
points_y = [5*i**4 + i**2 + 7 for i in points_x] #Calcul des images de ces points par la fonction choisie
    
def li_Lagrange(points_x, points_y):
    li = []  #Définition d'une liste qui contiendra tous les polynômes "li" de Lagrange
    Polynome_Interpolé = [] #Définition d'une variable qui contiendra les valeurs évalués en points_x[i] du polynome interpolé
    X = np.linspace(-1, 1, 300) #Définition d'un axe des abscisses 
    Y = [5*x**4 + x**2 + 7 for x in X] #Définition d'un axe des ordonnées
    for x in X: 
        P_évalué = 0 #Valeur du polynome interpolé évalué 
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
    
affichage(points_x, points_y)
