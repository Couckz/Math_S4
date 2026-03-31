from math import *

#Calcul de la decomposition de cholesky
def decompCholesky(A):
    L = [[0 for el in A[0]] for k in range(len(A))]
    for i in range(len(A)):
        for j in range(0,i+1):
            if j == i:
                li = 0
                for k in range(0,i):
                    li+=L[i][k]**2
                L[i][i] = sqrt(A[i][i]-li)
            else:
                li = 0
                for k in range(0,j):
                    li+=L[i][k]*L[j][k]
                L[i][j] = (A[i][j] - li)/L[j][j]
    return L

A = [[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-3], [0,3,-1,8]]
b = [6,25,-11,15]

#Ltrans(L)x = b 
#trans(L)x = Ltrans(L)x
def resCholesky(A,b):
    resultat = decompCholesky(A)
    n = len(A)
    y = [0]*n
    x = [0]*n
    #Descente
    for i in range(n):
        s = 0
        for k in range(i):
            s += resultat[i][k] * y[k]
        y[i] = (b[i] - s) / resultat[i][i]
    #Remonté
    for i in range(n-1, -1, -1):
        s = 0
        for k in range(i+1, n):
            s += resultat[k][i] * x[k]
        x[i] = (y[i] - s) / resultat[i][i]
    return x

print(resCholesky(A,b))


def decompLU(A):
    L = [[0 for i in range(len(A))] for k in range(len(A))]
    U = [[0 for j in range(len(A))] for l in range(len(A))]
    for i in range(len(A)):
        # Calcul de U
        for j in range(i, len(A)):
            s = 0
            for k in range(i):
                s += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - s
        # Calcul de L
        for j in range(i, len(A)):
            if i == j:
                L[i][i] = 1  
            else:
                s = 0
                for k in range(i):
                    s += L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - s) / U[i][i]
    return L, U

A = [[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-3], [0,3,-1,8]]
b = [6,25,-11,15]

def resLU(A,b):
    resultat = decompLU(A)
    L = resultat[0]
    U =resultat[1]
    solution = [0]*len(A)
    # Descente
    for i in range(len(A)):
        s = 0
        for k in range(i):
            s += L[i][k] * solution[k]
        solution[i] = b[i] - s   # car L[i][i] = 1
    # remontée
    for i in range(len(A)-1, -1, -1):
        s = 0
        for k in range(i+1, len(A)):
            s += U[i][k] * solution[k]
        solution[i] = (solution[i] - s) / U[i][i]
    return solution

print(resLU(A,b))