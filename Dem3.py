from biblio import *
from random import *
from tkinter import *

# - Separer partie vue/partie algo 


##Creation du plateau de jeu
r = matriceNulle(10,10)
n,p = dimensions(r)

root = Tk()
root.title("Démineur")

can = Canvas(root, width=700,height=700, bg="white")
can.pack(side="bottom")

oui = PhotoImage(file="button.png")

nbrBomb = 25
total = n*p

img=[]
bomb=[]

def generePlateau(r):  

    Ind=[]

    for i in range(nbrBomb):
        x = randint(0,9)
        y = randint(0,9)
    ## Recuperation indices des bombes
        if r[x][y]!="X":
          r[x][y]="X"
          Ind.append([x,y])
          bomb.append((x*10)+y)
        else:
            i-=1

    # Incrementer autour des bombes
    for i in Ind:
        a,b=i[0],i[1]
        s,t=-1,-1
        for i in range(3):
            for j in range(3):
                if(0<=a+s<=n-1 and 0<=b+t<=n-1 and r[a+s][b+t]!="X"):
                    r[a+s][b+t]+=1 # Incrementation autour bombe
                t+=1    
            s+=1
            t=-1

#devoile la case cliqué
def devoile(event):
    i,j = int(event.x/70),int(event.y/70)
    t = (j*10)+i
    if(t in bomb):
        for h in range(total):
            can.delete(img[h])
    else:
        can.delete(img[t])    

#recouvre le plateau pour cacher les indices
def couverture():
    x=0
    y=0
    s=0

    for i in range(n):
        for j in range(p):
            img.append("")
            img[s] = can.create_image(x+35,y+35,image=oui)
            s+=1
            x+=70
        x=0
        y+=70

    return img


# Plateau de jeu graphique
def Game(r):
    lbl = Label(root,text="Click on a box to start playing !", font=("arial",16,"italic"))
    lbl.pack()
    
    x=0
    y=0

    for i in range(n):
        for j in range(p):
            can.create_rectangle((x,y),(x+70,y+70), fill="gray",outline='black')
            if r[i][j]==1:
                can.create_text((x+35,y+35), text=r[i][j], font=("arial",16,"italic"), fill="white")
            if r[i][j]==2:
                can.create_text((x+35,y+35), text=r[i][j], font=("arial",16,"italic"), fill="blue")
            if r[i][j]==3:
                can.create_text((x+35,y+35), text=r[i][j], font=("arial",16,"italic"), fill="green")
            if r[i][j]==4:
                can.create_text((x+35,y+35), text=r[i][j], font=("arial",16,"italic"), fill="dark violet")
            if r[i][j]==5:
                can.create_text((x+35,y+35), text=r[i][j], font=("arial",16,"italic"), fill="yellow")
            if r[i][j]=="X":
                can.create_text((x+35,y+35), text=r[i][j], font=("arial",16,"italic"))
            x+=70
        x=0
        y+=70

generePlateau(r) # Genère le plateau construit | matrice r remplie
Game(r) # Aspect graphique
afficher(r) # Affiche la matrice
couverture()
root.bind("<Button-1>", devoile)
mainloop()
