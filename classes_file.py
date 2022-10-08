import numpy as np
import pygame
from rndgen import *

################################################################
class button():
    '''
    class used to generate button on the screen
    '''
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x #x and y represents position of button on the screen
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def printbutt(self,surface):
        '''
        printbutt is used to print a button on the screen
        '''
        #we draw a corresponding rectangle
        pygame.draw.rect(surface, self.color, (self.x,self.y,self.width,self.height), 0)
        #if we want text, we add it with the built-in method blit
        if self.text != '':
            font = pygame.font.Font('Police/8-bit-operator/8bitOperatorPlus-Regular.ttf', 30)
            ecrir = font.render(self.text, True, (255,255,255))
            surface.blit(ecrir,(self.x + (self.width/2 - ecrir.get_width()/2), self.y + (self.height/2 - ecrir.get_height()/2)))

    def mouseon(self, pos = (0,0)):
        '''
        mouseon return True if mouse is on the button, False otherwise
        '''
        pos = pygame.mouse.get_pos() #built-in method that return a tuple with mouse coordinate
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

################################################################
class text():
    '''
    class used to generate text
    '''
    def __init__(self, color, x, y, size, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.text = text
    def printtxt(self, surface, pol = 'Police/8-bit-operator/8bitOperatorPlus-Regular.ttf'):
        '''
        printtxt print text on the screen
        '''
        font = pygame.font.Font(pol, self.size)
        surf = font.render(self.text, True, self.color)
        textRect = surf.get_rect()
        textRect.center = (self.x, self.y)
        surface.blit(surf, textRect)

################################################################
#class used to generate sudoku grids
class rndgrid():
    '''
    class used to generate sudoku grids
    '''
    def __init__(self, width, height, level_difficulty = 5):
        self.ugrille = rnd_gen(level_difficulty) #we use the rnd_gen function to have a randomly filled grid
        self.tgrille = np.zeros((9,9), dtype = int) #an empty grid used to not have mistake in the error counter
                                                    #it allows us count error without having to change ugrille.
        #we define each cell in the class cell below
        self.cells = [[Cell(self.ugrille[i][j], i ,j, width, height) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height
        self.errpron = 0 #counter of errors

    def printgrid(self, surface):
        '''
        printgrid prints the grid on the screen,
        with the help function printnum_incell for the numbers in cells.
        It also print the counter of errors
        '''
        #we will print lines, thicker for the 'main' lines
        saut = self.width / 9
        for i in range(9+1):
            if i % 3 == 0 or i == 0:
                trait = 4
            else:
                trait = 1
            pygame.draw.line(surface, (0,0,0), (100, 30+i*saut), (100+self.width, 30+i*saut), trait)
            pygame.draw.line(surface, (0,0,0), (100+i*saut, 30), (100+i*saut, 30+self.height), trait)
        for i in range(9):
            for j in range(9):
                self.cells[i][j].printnum_incell(surface)
        #we add the number of errors in the right low part of the sceen
        ffont = pygame.font.Font('Police/8-bit-operator/8bitOperatorPlus-Regular.ttf',20)
        fill = ffont.render('Number of errors:  '+str(self.errpron), True, (0,0,0))
        surface.blit(fill,(730,450))


    def mouseon(self, pos = (0,0)):
        '''
        mouseon returns the coordinate of the cell in the sudoku grid where the mouse is,
        if the mouse is on the sudoku grid, returns (-10,-10) otherwise
        '''
        pos = pygame.mouse.get_pos()
        saut= self.width / 9
        if 100 < pos[0] < 100+self.width and 30 < pos[1] < 30+self.height:
            return (int((pos[0]-100)//saut),int((pos[1]-30)//saut))
        else:
            return (-10,-10)

################################################################
#this class is very similar to rndgrid, expect for the fact that ugrille is not generated via rnd_gen
class usergrid():
    '''
    class used to generate sudoku grids
    '''
    def __init__(self, width, height):
        self.ugrille = np.zeros((9,9), dtype = int) #ugrille is an empty grid at start, will be filled in in fillin screen (GUI.py)
        self.tgrille = np.zeros((9,9), dtype = int)
        self.cells = [[Cell(self.ugrille[i][j], i ,j, width, height) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height
        self.errpron = 0

    def printgrid(self, surface):
        '''
        printgrid prints the grid on the screen,
        with the help function printnum_incell for the numbers in cells.
        It also print the counter of errors
        '''
        saut = self.width / 9
        for i in range(9+1):
            if i % 3 == 0 or i == 0:
                trait = 4
            else:
                trait = 1
            pygame.draw.line(surface, (0,0,0), (100, 30+i*saut), (100+self.width, 30+i*saut), trait)
            pygame.draw.line(surface, (0,0,0), (100+i*saut, 30), (100+i*saut, 30+self.height), trait)
        for i in range(9):
            for j in range(9):
                self.cells[i][j].printnum_incell(surface)

        ffont = pygame.font.Font('Police/8-bit-operator/8bitOperatorPlus-Regular.ttf',20)
        fill = ffont.render('Number of errors:  '+str(self.errpron), True, (0,0,0))
        surface.blit(fill,(730,450))

    def mouseon(self, pos = (0,0)):
        '''
        mouseon returns the coordinate of the cell in the sudoku grid where the mouse is,
        if the mouse is on the sudoku grid, returns (-10,-10) otherwise
        '''
        pos = pygame.mouse.get_pos()
        saut= self.width / 9
        if 100 < pos[0] < 100+self.width and 30 < pos[1] < 30+self.height:
            return (int((pos[0]-100)//saut),int((pos[1]-30)//saut))
        else:
            return (-10,-10)

################################################################
class Cell():
    '''
    class used to represents cells and number in it
    '''
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def printnum_incell(self, surface, col = (0,0,0)):
        '''
        printnum_incell prints numbers in cells
        '''
        font = pygame.font.Font('Police/8-bit-operator/8bitOperatorPlus-Regular.ttf',30)
        saut = self.width / 9
        x = self.row * saut+109
        y = self.col * saut+40
        if self.value != 0:
            txt = font.render(str(self.value), True, col)
            surface.blit(txt,(x+10,y))
