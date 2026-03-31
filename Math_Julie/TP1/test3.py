import math
import numpy as np
import matplotlib.pyplot as plt


#Dans ce code, la fonction choisie pour les test est : f(x) = 1/25x^2
#Définition de l'intervalle d'étude

a, b = -1, 1
n = 4

#Définition de la fonction "tcheby_points"
def tcheby_points(a, b, n):
    points_tchebychev = [] #Création du tableau qui contiendra tous les points de tchebychev
    for i in range(n+1):
        x = (a + b)/2 + (b - a)/2 * math.cos((2*i + 1) * math.pi / (2*(n+1))) #Calcul de tous les xn de Tchebychev
        points_tchebychev.append(x)
    return points_tchebychev


# Définition de trois points dont les coordonnées (x,y) sont respectivement les valeurs de points_x et points_y
# On choisit pour l'études des points par lesquels passent la fonction choisie. Les abscisses sont respectivement les points de Tchebychev
points_x = tcheby_points(a, b, n)
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
    #Retourne le polynome interpolé, l'axe des ordonnées et l'axe des abscisses de telle sorte à éviter le redondance de code dans la fonction affichage
    return Polynome_Interpolé, Y, X
    
#Fonction qui gère l'affichage
def affichage(points_x, points_y):
    resultat = li_Lagrange(points_x, points_y)
    plt.plot(resultat[2], resultat[1], label="fonction choisie")
    plt.plot(resultat[2], resultat[0], label="polynome interpolé")
    plt.title(f"Fonction choisie et polynome interpolé avec tchebychev pour n = {n}")
    plt.legend()
    plt.show()

#Fonction qui gère le calcul de l'erreur et le traçage des courbes correpsondantes
def erreur(n):
    n_valeur = [i for i in range(2,n+1)]
    log_erreur = []
    log_n = []
    #On fait varier n et on calcule le polynôme interpolé pour chaque n, et on garde le log de l'erreur correspondant à chaque n en mémoire
    for n in n_valeur:
        points_x = tcheby_points(a, b, n)
        points_y = [1/(1+25*i**2) for i in points_x]
        resultat = li_Lagrange(points_x, points_y)
        Polynome = np.array(resultat[0])
        Fonction = np.array(resultat[1])
        erreur = np.max(np.abs(Fonction - Polynome))
        log_erreur.append(np.log10(erreur))
        log_n.append(np.log10(n))
    plt.plot(log_n, log_erreur)
    plt.title(f"Logarithme de l'erreur en fonction du logarithme de n, pour n = {n} ")
    plt.show()

affichage(points_x, points_y)
erreur(n)