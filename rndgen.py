import numpy as np
import pygame
import random
from copy import deepcopy
import time

from SolveSudok import *

################################################################
def verify(grille, pos, num):
    '''
    Function verify checks that a number can be put into a cell
    '''
    #we check in line
    for i in range(9):
        if grille[i][pos[1]] == num and (i, pos[1]) != pos:
            return False
    #we check in column
    for j in range(9):
        if grille[pos[0]][j] == num and (pos[0], j) != pos:
            return False
    #we check in 3x3 square
    b_i = pos[0] - pos[0] % 3
    b_j = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):
            if grille[b_i + i][b_j + j] == num and (b_i + i,b_j + j) != pos:
                return False
    #if line, col and 3x3 square allright, we return true
    return True

################################################################
def rnd_gen(level_difficulty=5):
    '''
    Function rnd_gen will generate randomly a grid, the argument is the level of difficulty.
    The higher the argument, the higher the diffculty
    '''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #we generate a grid filled with 0's
        grille = np.zeros((9,9), dtype = int)
        #we will fill some cells in the grid (the higher the argument of rnd_gen, the less cells are filled)
        for i in range(9):
            for j in range(9):
                if random.randint(1,10) >= level_difficulty:
                    grille[i][j] = random.randint(0,9)
                    #we verify that the inputed number can be put in the cell
                    if verify(grille, (i,j), grille[i][j]):
                        continue
                    else:
                        grille[i][j] = 0

        rndsavedgrille = deepcopy(grille)
        #we verify that the sudoku is solvable, if yes we return the grid
        if SolveSudok(grille):
            return rndsavedgrille

################################################################
def solvefunc(surface, grille, cells):
    '''
    Function solvefunc will be used to fill in the cells from a sudoku when Solve button is clicked on
    (this function is very similar to SolveSudok, except for the animations)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    fill = GetChoice(grille)

    if CheckSolved(grille) == 1:
        return True

    for i in fill[2]:
        if CheckSolved(grille) == 0:
            grille[fill[0]][fill[1]] = i
            cells[fill[0]][fill[1]].value = i
            cells[fill[0]][fill[1]].printnum_incell(surface,(0,0,255))
            time.sleep(0.01) #we froze the screeen for 0.01 seconds, for animations purposes
            pygame.display.update()
            if solvefunc(surface, grille, cells):
                return True
        grille[fill[0]][fill[1]] = 0
        cells[fill[0]][fill[1]].value = 0
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(fill[0]*60+107,fill[1]*60+35, 50,50))
        pygame.display.update()
        time.sleep(0.01)

    return False

################################################################
def usersolvefunc(surface, grille, cells):
    '''
    Function usersolvefunc is identical to solvefunc, except for the fact that we take into
    account the 'inversion' from fillin
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    fill = GetChoice(grille)

    if CheckSolved(grille) == 1:
        return True

    for i in fill[2]:
        if CheckSolved(grille) == 0:
            grille[fill[0]][fill[1]] = i
            cells[fill[1]][fill[0]].value = i     # we can see here the inversion due to fillin
            cells[fill[1]][fill[0]].printnum_incell(surface,(0,0,255))
            time.sleep(0.001)
            pygame.display.update()
            if usersolvefunc(surface, grille, cells):
                return True
        grille[fill[0]][fill[1]] = 0
        cells[fill[1]][fill[0]].value = 0
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(fill[1]*60+107,fill[0]*60+35, 50,50))
        pygame.display.update()
        time.sleep(0.001)

    return False
