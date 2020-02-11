from biblio import *
from random import *
from tkinter import *

##Creation du plateau de jeu
r = matriceNulle(10,10)
n,p = dimensions(r)

root = Tk()
root.title("Démineur")



def generePlateau(r,C):  
    
    C = C.x,C.y
    print(C)
    Ind=[]

    for i in range(10):
        x = randint(0,9)
    y = randint(0,9)
    ## Recuperation indices des bombes
    if r[x][y]!="X":
        r[x][y]="X"
        Ind.append([x,y])
    else:
        i-=1

    for i in Ind:
        a=i[0]
        b=i[1]
        s=-1
        t=-1
        for i in range(3):
            for j in range(3):
                if(0<=a+s<=n-1 and 0<=b+t<=n-1 and r[a+s][b+t]!="X"):
                    r[a+s][b+t]+=1
                t+=1    
            s+=1
            t=-1

def startPlaying():
    for i in range(n):
        for j in rangr(p):
            if(r[i][j]==0):
                c=0


def Game(r):
    lbl = Label(root,text="Click on a box to start playing !", font=("arial",16,"italic"))
    lbl.grid(row=0,column=0, columnspan=9,pady=3)
    #can = Canvas(root, width=1000,height=1000, bg="white")
    #can.grid()
    button=[]
    X,Y = 50,50
    for i in range(n):
        for j in range(p):
            button.append("1")
            if r[i][j]==1:
                button[i+j] = Button(root,text=r[i][j],fg="green",width=3,font=("arial",18,"bold"),bd=4)
                button[i+j].grid(row=i+1, column=j)
            if r[i][j]==2:
                button[i+j] = Button(root,text=r[i][j],fg="blue",width=3,font=("arial",18,"bold"),bd=4)
                button[i+j].grid(row=i+1, column=j)
            if r[i][j]==3:
                button[i+j] = Button(root,text=r[i][j],fg="red",width=3,font=("arial",18,"bold"),bd=4)
                button[i+j].grid(row=i+1, column=j)
            if r[i][j]==4:
                button[i+j] = Button(root,text=r[i][j],fg="dark violet",width=3,font=("arial",18,"bold"),bd=4)
                button[i+j].grid(row=i+1, column=j)         
            if r[i][j]==0 or r[i][j]=="X":
                button[i+j] = Button(root,text=r[i][j],width=3,font=("arial",18,"bold"),bd=4)
                button[i+j].grid(row=i+1, column=j)

root.bind("<Motion>", lambda C:generePlateau(r,C))
Game(r)
mainloop()