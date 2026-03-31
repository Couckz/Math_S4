from random import *
import test1
import time
import matplotlib.pyplot as plt
import numpy as np

#Définition d'un n
n = 100
b = [1 for i in range(n)] #Definition du b, vecteur 1xn comme demandé dans le tp

#Fonction qui gère le calcul de la matrice tridiagonale
def tridiag(n):
    diagonale = randint(50, 100)
    matrice = []
    for i in range(n):
        ligne = [0]*n 
        ligne[i] = diagonale
        if i > 0:
            ligne[i-1] = -1 
        if i < n-1:
            ligne[i+1] = -1 
        matrice.append(ligne)
    return matrice

#Pour une valeur de n donné, on démare pour cholesky et LU un timer à t=temps actuel et on l'arrête quand la fonction a finit de s'executer
#Le temps d'execution correspond tout simplement au temps final moins le temps d'execution
t1 = time.time()
test1.resCholesky(tridiag(n), b)
t2 = time.time()

temps_cholesky = t2 - t1

t3 = time.time()
test1.resLU(tridiag(n), b)
t4= time.time()

temps_LU = t4 - t3

print("Durée résolution cholesky : ", temps_cholesky)
print("Durée résolutoin par LU :", temps_LU)

#Fonction qui trace le log du temps d'execution en fonction du log de n
def temps_calcul(n):
    n_valeur = [i for i in range(0,n+1)]
    tempscalcul_cholesky= []
    tempscalcul_LU= []
    liste_n = []
    for n in n_valeur:
        matrice = tridiag(n)
        
        t1 = time.time()
        test1.resCholesky(matrice, b)
        t2 = time.time()
        temps_cholesky = t2 - t1
        
        
        t3 = time.time()
        test1.resLU(matrice, b)
        t4 = time.time()
        temps_LU = t4 - t3
        
        tempscalcul_cholesky.append(temps_cholesky)
        tempscalcul_LU.append(temps_LU)
        liste_n.append(n)
        
    plt.title("Temps de calcul en fonction de n, pour n = 100")
    plt.plot(liste_n, tempscalcul_cholesky, label="Temps de calcul pour Cholesky")
    plt.plot(liste_n, tempscalcul_LU, label="Temps de calcul pour LU")
    plt.legend()
    plt.show()
    
temps_calcul(n)

#pour calculer l'erreur on teste si Ax-b = 0. On a besoin de réaliser un produit matriciel
def erreur(n):
    log_erreur_cholesky = []
    log_erreur_LU = []
    log_n = []
    n_valeur = [i for i in range(2,n+1)]
    #On fait varier n et on calcule le polynôme interpolé pour chaque n, et on garde le log de l'erreur correspondant à chaque n en mémoire
    for n in n_valeur:
        b = np.array([1 for i in range(n)])
        matrice_tridiagonale = np.array(tridiag(n))
        solution_cholesky = np.array(test1.resCholesky(matrice_tridiagonale, b))
        solution_LU = np.array(test1.resLU(matrice_tridiagonale, b))
        erreur_cholesky = np.max(np.abs(np.dot(matrice_tridiagonale, solution_cholesky) - b))
        erreur_LU = np.max(np.abs(np.dot(matrice_tridiagonale, solution_LU) - b))
        log_erreur_cholesky.append(np.log10(np.abs(erreur_cholesky)))
        log_erreur_LU.append(np.log10(np.abs(erreur_LU)))
        log_n.append(np.log10(n))
    plt.plot(log_n, log_erreur_cholesky, label="Log de l'erreur de cholesky en fonction du log de n")
    plt.plot(log_n, log_erreur_LU, label="Log de l'erreur LU en fonction du log de n")
    plt.legend()
    plt.title(f"Logarithme de l'erreur en fonction du logarithme de n, pour n = {n} ")
    plt.show()

erreur(10)