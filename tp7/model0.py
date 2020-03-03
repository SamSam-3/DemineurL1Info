from random import randrange

NB_SQUARES=4

def shuffle_board(n=NB_SQUARES, N=100):
    # Renvoie un plateau bien mélangé
    # N : Nombre de mélanges

    def echange(board, empty):
        i, j=empty
        V=[(a,b) for (a, b) in
                [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
                if a in range(n) and b in range(n)]    
        ii, jj=V[randrange(len(V))]
        board[ii][jj], board[i][j]=board[i][j],board[ii][jj]
        return ii, jj
    
    board=[[n*lin+col+1 for col in range(n)]
        for lin in range(n)]
    board[n-1][n-1]=0
    empty=(n-1,n-1)

    for i in range(N):
        empty=echange(board, empty)
        
    return board

def voisins(n,i,j):
    D=[]

    if(i-1)>=0:
        D.append(board[i-1][j])
    if(j-1)>=0:
        D.append(board[i][j-1])
    if(j+1)<=3:    
        D.append(board[i][j+1])
    if(i+1)<=3:
        D.append(board[i+1][j])

    return D

def caseVide(board, i, j):
    n=len(board)
    for line, col in voisins(n, i,j):
        if board[line][col]==0:
            return line,col
    return None

def find_empty():
    for i in range(NB_SQUARES):
        for j in range(NB_SQUARES):
            if board[i][j]==0:
                x = [i,j]
    return x                

def print_board(board):
    print('\n'.join([' '.join(["%2s"%v for v in L ]) for L in board]))
    
board = shuffle_board(4,100)
x = find_empty()
print_board(board) 

print()
print(x)
print(voisins(NB_SQUARES,0,0))
print(caseVide(board,0,0)) 


