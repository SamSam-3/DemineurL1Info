from tkinter import *

root=Tk()
cnv = Canvas(root, width=500,height=500, bg="blue")
cnv.pack(side="bottom",anchor="sw")

def tour():
    i=0
    if i%2==0:
        joueur="Rouge"    
    else:
        joueur="Jaune"
    lbl = Label(root, width=25,height=4, text="C'est au tour du joueur "+joueur,justify="right").pack(side="bottom", padx=2, pady=2,anchor="se", expand=1)

def Token():
    #Finir de placer les pieces et incrementer la def joeur

x,y=20,20
for i in range(8):
    btn = Button(width=8,height=2,bg="gray",text=i,relief=FLAT,comamnd=)
    btn.pack(side="left")
    for j in range(8):
        cnv.create_oval((x,y),(x+50,y+50),fill="white")
        x+=70
    y+=70
    x=20


tour()    
mainloop()