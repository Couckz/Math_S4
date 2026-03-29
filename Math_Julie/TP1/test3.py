import math #Importation du module math
from sympy import * #Importation du module sympy
def tcheby_points(a, b, n):
    points_tchebychev = [] #Création du tableau qui contiendra tous les points de tchebychev
    for i in range(n+1):
        x = (a + b)/2 + (b - a)/2 * math.cos((2*i + 1) * math.pi / (2*(n+1))) #Calcul de tous les xn de Tchebychev
        points_tchebychev.append(x)
    return points_tchebychev
#Dans ce code, la fonction choisie pour les test est : f(x) = 1/25x^2
#Définition de l'intervalle d'étude
a, b = -1, 1
#Définiton du nombre de points de Tchebychev calculé
n = 4
# Définition de trois points dont les coordonnées (x,y) sont respectivement les valeurs de points_x et points_y
# On choisit pour l'études des points par lesquels passent la fonction choisie. Les abscisses sont respectivement les points de Tchebychev
points_x = tcheby_points(a, b, n)
points_y = [1/(1+25*i**2) for i in points_x]

#Définition de la fonction désirée
def Poly_Lagrange(points_x, points_y):
    x = symbols('x') #"Symbols" est une fonction de sympy qui définit la variable utilisée pour les calculs formels, ici x. 
    li = [] #Définition d'une liste qui contiendra tous les polynômes "li" de Lagrange
    Polynome_Interpolé = 0 #Définition d'une variable qui contiendra le polynôme interpolé
    pol_choisit = 1/(1+25*x**2) #Définition du polynôme choisit
    #Itération sur les indices des points, servant à calculer les "li" de Lagrange
    for j in range(len(points_x)):
        li_num = 1 #Définition de la variable qui contiendra le numérateur du li calculé pour le points indicé j
        li_den = 1 #Définition de la variable qui contiendra le dénumérateur du li calculé pour le points indicé j
        #Interation une deuxième fois sur les indices des points. 
        #Essentielle pour éviter l'intervention du terme x-xi dans le calcul du "li" de Lagrange
        for i in range(len(points_x)): 
            #Test pour éviter le terme xi-xi dans le calcul des li de Lagrange, d'où l'intervention de la deuxième boucle
            if i != j:
                li_num = (x-points_x[i])*li_num # Implémentation du calcul du numérateur pour le li de lagrange pour le point j
                li_den = (points_x[j]-points_x[i])*li_den # Implémentation du calcul du dénominateur pour le li de lagrange pour le point j
        li.append(sympify(li_num/li_den)) #Ajout du li calculé en simplifiant son expression formellement par la fonction sympify
    #Boucle servant à calculer le polyome interpolé 
    for k in range(len(points_y)):
        Polynome_Interpolé += sympify(li[k]*points_y[k])
    print(sympify(expand(Polynome_Interpolé)))
    #Affichage du polynôme interpolé et du polynôme choisit
    plot((Polynome_Interpolé, (x, min(points_x)-1, max(points_x)+1), "Polynome de lagrange"), 
        (pol_choisit, (x, min(points_x)-1, max(points_x)+1), "Fonction choisie" ), legend=True)
    return sympify(expand(Polynome_Interpolé)) #Retourner l'expression simplifier (sympify) et développée (expand) du polynôme interpolé 
#Affichage du polynômé interpolé 
print("le résultat est ", Poly_Lagrange(points_x, points_y))