from model1 import shuffle_board, caseVide, swap, win
from tkinter import *

CANVAS_SIDE=400
NB_SQUARES=4
R=CANVAS_SIDE//NB_SQUARES

def fill_board(cnv, board, n=NB_SQUARES):
    cnv.delete(ALL)    
    for i in range(n):
        for j in range(n):
            v=board[i][j]
            if v:
                cnv.create_rectangle(j*R, i*R, (1+j)*R, (1+i)*R, fill="lavender")
                cnv.create_text(j*R+R//2, i*R+R//2, text=v,  font=('courier', CANVAS_SIDE//10, 'bold'))

                
def pos2lineCol(x, y):
    n= CANVAS_SIDE/NB_SQUARES
    p= CANVAS_SIDE/NB_SQUARES
    for i in range(NB_SQUARES):
        for j in range(NB_SQUARES):
            if n*i <= x <= n*(i+1) and p*j <= y <= p*(j+1):
                s = [i,j]
    return s         

def melanger():
    global board
    # ok : un plateau terminé
    ok=[[n*lin+col+1 for col in range(n)]
        for lin in range(n)]
    ok[n-1][n-1]=0
    
    
    while True:
        board=shuffle_board(n)
        # être certain que le plateau a bien été mélangé
        if board!=ok:
            break
        
    fill_board(cnv, board)

    
def clic(event):
    print(pos2lineCol(event.x,event.y))


master=Tk()
cnv=Canvas(master, width=CANVAS_SIDE, height=CANVAS_SIDE, bg='ivory')
cnv.pack(side='left')

btn=Button(master, text="Mélanger", command=melanger)
btn.pack()

master.bind("<Button-1>", clic)
board=None
n=NB_SQUARES

melanger()
master.mainloop() 

