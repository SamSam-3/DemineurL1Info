from random import sample, randrange
from tkinter import *

COLORS=["ivory", "lime green", "red", "gray75"]

def random_forest(p, n):
    # génération aléatoire des arbres dans la parcelle
    units=[(line,col) for col in range(n) for line in range(n)]
    ntrees=int(n**2*p)
    trees=sample(units,ntrees)
    states=[[0]*n for _ in range(n)]
    for (i,j) in trees:
        states[i][j]=1    
    return states, trees

def voisins(n, i, j):
    """Dans une grille n x n, indices (ligne, colonne) des voisins 
    dans la grille d'un sommet (i,j) de la grille"""
    return [(a,b) for (a, b) in [(i, j+1),(i, j-1), (i-1, j), (i+1,j)] if a in range(n) and b in range(n)]

def update_states(states, fires):
    # Modèle
    # Modifie le plateau en son nouvel état
    # renvoie les positions des arbes en feu
    n=len(states)
    to_fire=[]
    for (line, col) in fires:
        for (i, j) in voisins(n, line, col):
            if states[i][j]==1:
                to_fire.append((i, j))
    for (line, col) in to_fire:
        if states[line][col]==1:
            states[line][col]=2
    for (line, col) in fires:
        states[line][col]=3
    
    return list(set(to_fire)) 
                
def fill(cnv, states, unit):
    # Vue Tkinter
    # dessine sol et arbres
    n=len(states)    
    for line in range(n):
        for col in range(n):
            A=(unit*col, unit*line)
            B=(unit*(col+1), unit*(line+1))
            state=states[line][col]
            color=COLORS[state]
            cnv.create_rectangle(A, B, fill=color, outline='')

def start_fire(states, trees):
    # Modèle
    "Met le feu aléatoirement (code = 2) à l'arbre en position (i,j)"
    i,j= trees[randrange(len(trees))]
    states[i][j]=2
    return (i,j)

def set_fire(event):
    # La fonction associée au clic de souris
    # pour mettre le feu
    # A écrire par vous-même
    
    i = side*n//event.y
    j = side*n//event.x    
    fires=[(i,j)]
    print(i,j)
    i,j=start_fire(states,trees)
    pass
    
def propagate():
    # Vue Tkinter
    # Animation du feu
    global fires, nfires
    fires=update_states(states, fires)
    k=len(fires)
    nfires+=k
    cnv.delete("all")
    fill(cnv, states, unit)
    cnv.after(200, propagate)
    if k==0:
        return

p=0.60
n=50
unit=10
nfires=0

root = Tk()
side=unit*n

cnv = Canvas(root, width=unit*n, height=unit*n, background="ivory") 
cnv.pack(padx=10, pady=10, side=LEFT)

states, trees=random_forest(p, n)
fires=[]
# on remplit la parcelle
fill(cnv, states, unit)


propagate()
root.bind("<Button-1>",set_fire)
# on anime

root.mainloop()
