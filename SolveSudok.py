import numpy as np
from GetChoice import *
from CheckSolved import *

recurs = 0 #we initialize recurs (count the number of recursions = number of cells to fill) at 0, 

def SolveSudok(K):
    '''
    Main solving function that will use the others function to solve a grid K
    '''
    global recurs
    fill = GetChoice(K)                            #fill will be a list with x_axis, y_axis and poss. value

    if CheckSolved(K)==1:
        recurs = 0                                 #recursion are counted only when sudoku is finished(backward)
        return True                                #if sudoku is finished, we return true

    for f in range(0,len(fill[2])):                #we iterate over each possible value of each cell
        if CheckSolved(K) == 0:
            K[fill[0]][fill[1]] = fill[2][f]

            if SolveSudok(K):                      #we call the recursion
                recurs += 1
                return (True, K, recurs)
        K[fill[0]][fill[1]] = 0                    #if mistake, we get the cell back to empty (so = 0)

    return False
