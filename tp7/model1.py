from random import randrange


NB_SQUARES=4




def shuffle_board(n=NB_SQUARES, N=100):
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


def voisins(n, i, j):
    """Dans une grille n x n, indices (ligne, colonne) des voisins 
    dans la grille d'un sommet (i,j) de la grille"""
    return [(a,b) for (a, b) in [(i, j+1),(i, j-1), (i-1, j), (i+1,j)] 
            if a in range(n) and b in range(n)]

def caseVide(board, i, j):
    n=len(board)
    for line, col in voisins(n, i,j):
        if board[line][col]==0:
            return line,col
    return None

def find_empty(board):
    n=len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                return i,j

def print_board(board):
    print('\n'.join([' '.join(["%2s"%v for v in L ]) for L in board]))
    
def swap(board, i, j):
    c=caseVide(board, i, j)
    if c is None:
        return
    line, col=c
    board[line][col],board[i][j]=board[i][j],board[line][col]

def win(board):
    n=len(board)
    L=[]
    for R in board:
        L.extend(R)
    ok=[z for z in range(1,n*n)]+[0]
    
    return L==ok
