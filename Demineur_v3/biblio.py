"""Petite bibliothèque de fonctions matricielles
complétée au fur et à mesure"""

from random import randrange

def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()        
        

def matriceNulle(n, p):
    "Constructeur de matrice de dimensions données"
    M=[]
    for i in range(n):
        L=[]
        for j in range(p):
            L.append(0)
        M.append(L)
    return M

def dimensions(A):
    return [len(A), len(A[0])]

def sontEgales(A,B):
    n,p=dimensions(A)
    s,t=dimensions(B)
    if n!=s or p!=t:
        return False
    for i in range(n):
        for j in range(p):
            if A[i][j] != B[i][j]:
                return False
    return True

def identite(n) :
    I = matriceNulle(n,n)
    for i in range(n) :
        I[i][i] = 1
    return I

def matriceAleatoire(n,p, a, b):
    A=matriceNulle(n,p)
    for i in range(n):
        for j in range(p):
            A[i][j] = randrange(a, b+1)
    return A


