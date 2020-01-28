from biblio import *
from random import *

##Creation du plateau de jeu
p = matriceNulle(10,10)


##Pose des bombes
Ind=[]
for i in range(10):
    x = randint(0,9)
    y = randint(0,9)
    Ind.append([x,y]) ## Recuperation indices des bombes
    if p[x][y]!=9:
        p[x][y]=9
    else:
        i-=1

for i in Ind:
    ##incrementer autour des bombes

afficher(p)