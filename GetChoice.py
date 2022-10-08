import numpy as np
from GetPoss import GetPoss

def GetChoice(K):
    '''
    Function that uses the output of GetPoss to return the cell with the lowest number of possiblities.
    The exact output is a list containing X_coordinate, Y_coordinate
    and a list of all the possiblities, of the said cell.
    '''
    A = GetPoss(K)   #we call GetPoss and assign M in a new variable: A.

    h = np.zeros((9,9), dtype = int)

    for i in range(0,9):                     #we introduce h, a matrix that sums over every plans of A.
        for j in range(0,9):                 #h gives us the number of possibilites for each cell.
               for z in range(0,9):
                    h[i][j] += A[z][i][j]


    for i in range(0,9):                    #Cells that are already filled need to go out of our algorithm.
        for j in range(0,9):                #If a cell is already filled, we assigne 10 to its coordinate
            if K[i,j] != 0:                 #in h.
                h[i,j] = 10

    coo = np.where(h == np.amin(h))         #we find the min in h and its corresponding coordinate

    coo1str = str(coo[0])                   #we transforms the coordinate in simple integer:
    coo2str = str(coo[1])                   #coo1 is row coordinate and coo2 is column coordinate
    coo1 = int(coo1str[1])
    coo2 = int(coo2str[1])

    S = []                                  #we put each possible number in a list S
    for i in range(0,9):
        if A[i,coo1,coo2] == 1:
            S.append(i+1)
    coo_choices_final = [coo1, coo2, S]     #we define our output as defined at the start of the function
    return coo_choices_final
