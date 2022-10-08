import numpy as np
from GetPoss import GetPoss

def CheckSolved(K):
    '''
    Function that return 0 if sudoku not finished AND no mistakes,
    1 if Sudoku finished and -1 if mistake in sudoku
    '''
    r = np.zeros((9,9), dtype = int)
    A = GetPoss(K)

    for i in range(0,9):                    #we introduce r, a matrix that sums over every plans of A.
            for j in range(0,9):            #h gives us the number of possibilites for each cell.
                   for z in range(0,9):
                        r[i][j] += A[z][i][j]

    for i in range(0,9):                    #if a cell is already filled in our sudoku, we change its
        for j in range(0,9):                #corresponding cell in r to 10
            if K[i,j] != 0:
                r[i,j] = 10

    confirm = 0
    for i in range(0,9):                    #we check that no cell in r is 0
            for j in range(0,9):
                if r[i][j] == 0:
                    confirm = 1

    if np.sum(K) == 405:                    #if sum of all sudoku cells is 405: sudoku is finished
        return 1
    elif confirm == 1:                      #if there is at least one 0 in r, MISTAKE (bc cell with 0 poss.)
        return -1
    else:                                   #otherwise we continue
        return 0
