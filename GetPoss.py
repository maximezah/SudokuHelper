import numpy as np #we will use numpy all along to generate and operate on matrices

def GetPoss(K):
    '''
    Function that take the current Sudoku matrix K and
    return a 9x9x9 boolean matrix (each plan is for 1 number)
    '''
    M = np.ones((9,9,9), dtype = int) #generation of M: a 9x9x9 matrix filled with 1's                                                #corresponds to a each possible input number (1 to 9)

    #we now need to change 1's in 0's in M where a specific number CANNOT be placed

    for i in range(1,10):         #we check each column: if a column contain a specific number, this column
        for j in range(0,9):      #becomes filled with 0's in the corresponding plan. We do so for each
            for z in range(0,9):    #plan.
                if K[j,z] == i:
                    M[(i-1),:,z] = 0

    for i in range(1,10):         #we check each rows (same as for columns)
        for j in range(0,9):
            for z in range(0,9):
                if K[j,z] == i:
                    M[(i-1),j,:] = 0

    for i in range(1,10):         #we check each 3x3 square: if a specific square contains a specific
        if i in K[0:3,0:3]:       #number,this square becomes filled with 0's in the corresponding plan.
            M[i-1,0:3,0:3]=0      #We do so for each plan.
        if i in K[0:3,3:6]:
            M[i-1,0:3,3:6]=0
        if i in K[0:3,6:9]:
            M[i-1,0:3,6:9]=0
        if i in K[3:6,0:3]:
            M[i-1,3:6,0:3]=0
        if i in K[3:6,3:6]:
            M[i-1,3:6,3:6]=0
        if i in K[3:6,6:9]:
            M[i-1,3:6,6:9]=0
        if i in K[6:9,0:3]:
            M[i-1,6:9,0:3]=0
        if i in K[6:9,3:6]:
            M[i-1,6:9,3:6]=0
        if i in K[6:9,6:9]:
            M[i-1,6:9,6:9]=0

    return M           #The function returns the matrix M, with 0's where number cannot be placed
                       #and 1's where they can be placed.
