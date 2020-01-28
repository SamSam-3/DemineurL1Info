from tkinter import *
from math import *

def passage(x,y, a, b):
    return (a+x, b-y)

def produit(k, n, p):
    return k*n % p

def segment(cnv, k, n, p, base, a, b):
    # base : les coordonnées des points du cercle
    # on trace le produit prod=k*n
    # k -> A
    # prod -> B
    prod=produit(k, n, p)
    xA, yA=base[k]
    xB, yB=base[prod]    
    A=passage(xA, yA, a, b)
    B=passage(xB, yB, a, b)
    cnv.create_line(A, B)
    
def dot(cnv, C, R=6, color='red'):
    xC, yC=C
    return cnv.create_oval(xC-R,yC-R,xC+R, yC+R, fill=color, outline=color)
  
def draw_base(cnv, p, base, a, b):
    # Les sommets sur le cercle
    for k in range(p):
        x, y=base[k]
        X, Y=passage(x, y, a, b)
        dot(cnv, (X, Y), R=2, color='black')
    
def points(p,n,R):
    p=int(p)
    print(p)
    draw(n,p,R)

def table(p, n, R):
    n = int(n)
    print(n)
    draw(n,p,R)

def draw(n, p, R):
    
    R=200
    a=b=1.2*R

    # Les points du cercle
    base=[(R*cos(2*k*pi/p), R*sin(2*k*pi/p)) for k in range(p)]
    draw_base(cnv, p, base, a, b)

    # Tracé de la table
    for k in range(p):
        segment(cnv, k, n, p, base, a, b)    
    master.mainloop()


master=Tk()

n=2
p=2
R=200
a=b=1.2*R
cnv=Canvas(width=2*a, height=2*b,bg='ivory')
cnv.pack(side="left")

point = Scale(orient="horizontal",label="Nbr de points : ", width=12, from_=2, to=500, command=lambda p: points(p,n,R))
point.pack(padx=10, pady=40)
point.set(2)
mult = Scale(orient="horizontal",label="Table multiplicat° :  ", width=12, from_=2, to=50, command=lambda n: table(p,n,R))
mult.pack(padx=10, pady=40)
mult.set(5)

draw(n,p,R)