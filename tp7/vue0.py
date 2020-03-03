from model0 import shuffle_board
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

master=Tk()
cnv=Canvas(master, width=CANVAS_SIDE, height=CANVAS_SIDE, bg='ivory')
cnv.pack(side='left')

btn=Button(master, text="Mélanger", command=melanger)
btn.pack()

board=None
n=NB_SQUARES

melanger()

master.mainloop() 

