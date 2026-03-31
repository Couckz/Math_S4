from random import *
import test1
import time
import matplotlib.pyplot as plt
import numpy as np

#Définition d'un n
n = 4
b = [1 for i in range(n)] #Definition du b, vecteur 1xn comme demandé dans le tp

#Fonction qui gère le calcul de la matrice tridiagonale
def tridiag(n):
    diagonale = randint(0, 10)
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
    log_tempscalcul_cholesky= []
    log_tempscalcul_LU= []
    log_n = []
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
        
        log_tempscalcul_cholesky.append(np.log10(temps_cholesky))
        log_tempscalcul_LU.append(np.log10(temps_LU))
        log_n.append(np.log10(n))

    plt.plot(log_n, log_tempscalcul_cholesky, label="Temps de calcul pour Cholesky")
    plt.plot(log_n, log_tempscalcul_LU, label="Temps de calcul pour LU")
    plt.legend()
    plt.show()
    
temps_calcul(n)