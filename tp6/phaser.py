# Implémentation de 
# https://phaser.io/examples/v2/arcade-physics/multi-angle-to-pointer

from tkinter import Tk, Canvas
from random import randrange
from turtle import Vec2D as vect

MAX_X=MAX_Y=600

root=Tk()
cnv=Canvas(root, width=MAX_X, height=MAX_Y, bg="gray")
cnv.pack()

# La longueur de chaque flèche
L=60

# les N extrémités des flèches
N=6
points=[(randrange(MAX_X),randrange(MAX_Y)) for _ in range(N)]



def origin(B, C, L):
    """
    Calcule l'origine A de la flèche connaissant :
    - l'extrémité B de la flèche
    - un point C visé par la flèche
    - la longueur L de la flèche
    """
    v=vect(*C)-vect(*B)
    k=-L/abs(v)
    A=k*v+vect(*B)
    return A
    
def shot(C):
    # C = poit de convergence des flèches
    # Dessine les flèches et les pointillés
    # depuis chaque point de la liste points
    cnv.delete("all")
    C = C.x,C.y
    
    for B in points:
        A=origin(B, C, L)
        # Créatopn de la flèche
        cnv.create_line(A,B, width=7, fill="green yellow", arrow='last', arrowshape=(18,30, 8))
        # Création des pointillés
        cnv.create_line(B,C, fill="green yellow", dash=3)
     
    
        
        
# Dessin statique : la cible des flèches est un point aléatoire
#shot((randrange(MAX_X),randrange(MAX_X)))
root.bind("<Motion>", shot)


root.mainloop() 
