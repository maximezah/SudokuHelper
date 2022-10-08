import pygame
import numpy as np
from time import time
from copy import deepcopy
import random

from SolveSudok import *
from rndgen import *
from classes_file import *

pygame.init()

#In this file, each function represents a defined screen.
#To navigate from screen to screen, we call the wanted function from the present function
################################################################
def mainmenu():
    '''
    This is the mainmenu screen
    User can choose different other menus
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('mainmenu')  #we will display a screen called 'ecran', with the chosen dimensions in set_mode
    ecran.fill((0,0,0)) #we fill our screen in black, defined by (0,0,0) in pygame

    title = text((255,0,0),500, 100, 80,'Sudoku Helper') #we use the class text to gen the titles
    title1 = text((255,0,0),500, 170, 50,'Main Menu')

    startbutt= button((0,0,0), 350,300, 300,50,'Start') #we use the class button to gen buttons
    controlsbutt = button((0,0,0), 350,350, 300,50,'Controls')
    creditsbutt= button((0,0,0), 350,400, 300,50,'Credits')
    quitbutt = button((0,0,0), 350,450, 300,50,'Quit')

    #we create an infinite loop with running
    running = True
    while running:
        pygame.display.flip() #we display the screen and update it
        title.printtxt(ecran,'Police/8-bit-operator/8bitOperatorPlus8-Bold.ttf') #we use the method in the text class to print the titles
        title1.printtxt(ecran,'Police/8-bit-operator/8bitOperatorPlus8-Bold.ttf')
        startbutt.printbutt(ecran) #we use the method in the button class to print the buttons
        controlsbutt.printbutt(ecran)
        creditsbutt.printbutt(ecran)
        quitbutt.printbutt(ecran)
        for event in pygame.event.get(): #for every events that might happens (user inputs), we define a specific output
            if event.type == pygame.QUIT: #if user click on the upper left screen cross, we quit pygame (end the programm)
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and quitbutt.mouseon():
              pygame.quit() #if user click on Quit button, we quit pygame
            if event.type == pygame.MOUSEBUTTONUP and startbutt.mouseon():
              startmenu() #if user click on start button, we call function startmenu()
            if event.type == pygame.MOUSEBUTTONUP and controlsbutt.mouseon():
              Controls() #if user click on start button, we call function Controls()
            if event.type == pygame.MOUSEBUTTONUP and creditsbutt.mouseon():
              Credits() #if user click on start button, we call function Credits()
        pygame.display.update() #we update the screen at every loop run

################################################################
def Credits():
    '''
    This is the Credits screen
    User sees the credits
    '''
    ecran = pygame.display.set_mode((1000,600)) #with each new function, we delete previous screen
    pygame.display.set_caption('Credits')       #by printing a new black screen on the previous one,
    ecran.fill((0,0,0))                         #always called 'ecran'

    title = text((255,0,0),500, 100, 80,'Credits')
    l1 = text((255,255,255),500, 240, 40,'Maxime Zahler')
    l2 = text((255,255,255),500, 300, 40,'Arnaud Castellana')
    l3 = text((255,255,255),500, 360, 40,'Colin Carruzzo')

    backbutt= button((0,0,0), 350,550, 300,50,'Back')

    running = True
    while running:
        pygame.display.flip()
        title.printtxt(ecran,'Police/8-bit-operator/8bitOperatorPlus8-Bold.ttf')
        l1.printtxt(ecran,'Police/alex-brush/AlexBrush-Regular.ttf')
        l2.printtxt(ecran,'Police/alex-brush/AlexBrush-Regular.ttf')
        l3.printtxt(ecran,'Police/alex-brush/AlexBrush-Regular.ttf')
        backbutt.printbutt(ecran)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
                mainmenu() #if user click on back Button, we call mainmenu(), which is the previous screen in this case
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    mainmenu() #here, we allow to user to press the backspace key to get back also (same output as the back button)

################################################################
def Controls():
    '''
    This is the Controls screen
    User sees the controls of the application
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('Controls Menu')
    ecran.fill((0,0,0))

    title = text((255,0,0),500, 100, 80,'Controls')
    l1 = text((255,255,255),500, 180, 20,'You can navigate in the windows with your mouse.')
    l2 = text((255,255,255),500, 230, 20,'In the different menus, you will find different buttons:')
    l3 = text((255,255,255),500, 280, 20,'Back -> click to get back to previous menu    Solve -> click to see the solution of the sudoku')
    l4 = text((255,255,255),500, 330, 20,'Hint -> click to get a random cell in sudoku filled with right value')
    l5 = text((255,255,255),500, 380, 20,'Val -> click to validate your input when filling/solving a sudoku')
    l6 = text((255,255,255),500, 430, 20,'To enter a value in a cell, place your cursor in it and press the number on your keyboard.')
    l7 = text((255,255,255),500, 470, 20,'If you need to change it, press backspace and press the new number.')
    l8 = text((255,255,255),500, 520, 20,'You can mark a cell by clicking on it. Remove a marker by pressing e with your cursor in the cell.')

    backbutt= button((0,0,0), 350,550, 300,50,'Back')

    running = True
    while running:
        pygame.display.flip()
        title.printtxt(ecran,'Police/8-bit-operator/8bitOperatorPlus8-Bold.ttf')
        l1.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l2.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l3.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l4.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l5.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l6.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l7.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l8.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        backbutt.printbutt(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
                mainmenu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    mainmenu()

################################################################
def startmenu():
    '''
    This is the startmenu screen
    User can choose to generate a grid randomly or to fill in his 'own' grid
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('startmenu')
    ecran.fill((0,0,0))

    title = text((255,0,0),500, 100, 80,'Start Menu')

    rndgen_butt= button((0,0,0), 350,300, 300,50,'Random Generating')
    usergen_butt = button((0,0,0), 350,350, 300,50,'User Generating')
    backbutt= button((0,0,0), 350,550, 300,50,'Back')

    running = True
    while running:
        pygame.display.flip()
        title.printtxt(ecran,'Police/8-bit-operator/8bitOperatorPlus8-Bold.ttf')
        rndgen_butt.printbutt(ecran)
        usergen_butt.printbutt(ecran)
        backbutt.printbutt(ecran)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and rndgen_butt.mouseon():
                rnd_gen_diff_level()
            if event.type == pygame.MOUSEBUTTONUP and usergen_butt.mouseon():
                fillin()
            elif event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
                mainmenu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    mainmenu()
    pygame.display.update()

################################################################
def rnd_gen_diff_level():
    '''
    This is the 'choosing difficulty menu' screen, comming after user chooses random generated rndgrid
    User can choose between 3 difficulty levels
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('rnd_gen_diff_level')
    ecran.fill((0,0,0))

    backbutt= button((0,0,0), 350,550, 300,50,'Back')
    easybutt= button((0,0,0), 350,250, 300,50,'Easy')
    mediumbutt= button((0,0,0), 350,300, 300,50,'Medium')
    hardbutt= button((0,0,0), 350,350, 300,50,'Hard')

    title = text((255,0,0),500, 100, 80,'Difficulty')
    l1 = text((255,255,255),500, 200, 20,'The generation of your grid can take up to a minute')

    running = True
    while running:
        pygame.display.flip()

        backbutt.printbutt(ecran)
        easybutt.printbutt(ecran)
        mediumbutt.printbutt(ecran)
        hardbutt.printbutt(ecran)

        title.printtxt(ecran,'Police/8-bit-operator/8bitOperatorPlus8-Bold.ttf')
        l1.printtxt(ecran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and easybutt.mouseon():
              rndgen(5)
            if event.type == pygame.MOUSEBUTTONUP and mediumbutt.mouseon():
              rndgen(6)
            if event.type == pygame.MOUSEBUTTONUP and hardbutt.mouseon():
              rndgen(7)
            if event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
              startmenu()

################################################################
def rndgen(dl):
    '''
    This is the random generating screen
    User can fill in a randomly generated grid
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('rndgen')
    ecran.fill((255,255,255))

    grille = rndgrid(540,540,dl)           #we use the class rndgrid to generate a grid

    copyugrille = deepcopy(grille.ugrille) #we copy the inital grid, to be able to solve it without changing it
    solver = SolveSudok(copyugrille)       #we solve the copy of the initial grid
    solvedS, recurs = solver[1],solver[2]  #we save the output of SolveSudok (the complete grid and the number of recursions)
    grille.printgrid(ecran)                #we use the method printgrid to print the initial grid on 'ecran'

    backbutt= button((0,0,0), 850,520, 100,50,'Back')
    hintbutt= button((0,0,0), 850,100, 100,50,'Hint')
    valbutt = button((0,0,0), 850,300, 100,50,'Val')
    solvebutt= button((0,0,0), 850,200, 100,50,'Solve')

    debut = time.time() #we save the starting time

    hint_c = 0  # we initiliase a counter of hints (see below )

    running = True
    while running:
        #we print a clock (time counter), that is updated by placing a white rectangle
        #on the clock and then printing again the update clock
        pygame.draw.rect(ecran,(255,255,255),pygame.Rect(700,430,300,25),0) #built-in method to print a rectangle
        #(255,255,255) is white, pygame.Rect has the coordinate and the size of the rectangle as arguments, the 0 is for the border (so no border)
        temps_passe = time.time()-debut #we update the time passed
        print_temps_passe = time.strftime('%M:%S', time.gmtime(temps_passe)) #we put the time to print in the right format (minutes and seconds)
        ffont = pygame.font.Font('Police/8-bit-operator/8bitOperatorPlus-Regular.ttf',20)
        fill = ffont.render('Clock:' +str(print_temps_passe), True, (0,0,0))
        ecran.blit(fill,(730,430)) #we print the time on the white rectangle

        backbutt.printbutt(ecran)
        hintbutt.printbutt(ecran)
        valbutt.printbutt(ecran)
        solvebutt.printbutt(ecran)

        #if sudoku grid is finished, we call summary() screen
        if np.sum(grille.ugrille) == 405: #sudoku is finished when sum = 405 (see CheckSoved())
            summary(grille.ugrille, grille.cells, grille.errpron, print_temps_passe, recurs, hint_c)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
                startmenu()
            if event.type == pygame.MOUSEBUTTONUP: #we print an empty recrtangle,with blue border if a cell is clicked on (we call that a marker)
                pygame.draw.rect(ecran,(124,234,255),pygame.Rect(grille.mouseon()[0]*60+103,grille.mouseon()[1]*60+33,55,55),2)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e: #if user has mouse on a cell and press e (for erase), we print an empty rectangle with white border (used to erase a before placed marker)
                pygame.draw.rect(ecran,(255,255,255),pygame.Rect(grille.mouseon()[0]*60+103,grille.mouseon()[1]*60+33,55,55),2)
            #if user press a number with the mouse in a cell that is empty, we print it in the screen and register the number in tgrille if the number is right, otherwise we add 1 to the counter of errors
            if event.type == pygame.KEYDOWN and (100<pygame.mouse.get_pos()[0]<640) and (30<pygame.mouse.get_pos()[1]<570):
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 \
                or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    if grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value == 0:
                        ffont = pygame.font.SysFont('comicsans',50)
                        fill = ffont.render(str(event.key-48), True, (124,234,255))
                        ecran.blit(fill,((grille.mouseon()[0])*60+115,(grille.mouseon()[1])*60+20))
                        if event.key-48==solvedS[grille.mouseon()[0]][grille.mouseon()[1]]:
                            grille.tgrille[grille.mouseon()[0]][grille.mouseon()[1]]= event.key-48
                        if event.key-48 != solvedS[grille.mouseon()[0]][grille.mouseon()[1]]:
                            grille.errpron += 1
            #if user press val button, we update the screen with the right inputs printed on the grid, the wrong erased
            if event.type == pygame.MOUSEBUTTONUP and valbutt.mouseon():
                    ecran.fill((255,255,255))
                    grille.ugrille = grille.ugrille+grille.tgrille #we add the right inputs to ugrille from tgrille
                    for i in range(9):
                        for j in range(9):
                            grille.cells[i][j].value = grille.ugrille[i][j]#we add the right inputs to each cell, that are used to print the numbers on the screen
                    grille.printgrid(ecran)
                    grille.tgrille = np.zeros((9,9), dtype = int) #we re-initiliase tgrille each time user press val Button
            #if user press backspace key and has mouse in a cell, we erase the number in the screen, re-initilase the cell values in the class and add -1 to the error counter if the number inputed was wrong
            if event.type == pygame.KEYDOWN and (100<pygame.mouse.get_pos()[0]<640) and (30<pygame.mouse.get_pos()[1]<570):
                if event.key == pygame.K_BACKSPACE:
                    if grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value == 0: #we erase only if the cell is empty in initial sudoku or after val button is pressed
                        pygame.draw.rect(ecran, (255,255,255), pygame.Rect((grille.mouseon()[0])*60+105,(grille.mouseon()[1])*60+35, 50,50)) #we draw a white rectangle in the cell to erase the value
                        grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value = 0 #we re-initialise the value in the grid (ugrille and cells)
                        grille.ugrille[grille.mouseon()[0]][grille.mouseon()[1]] = 0
                        if grille.tgrille[grille.mouseon()[0]][grille.mouseon()[1]] == 0:
                            grille.errpron -= 1 #if the number was wrong (cell is 0 in tgrille), we remove one error
                        grille.tgrille[grille.mouseon()[0]][grille.mouseon()[1]] = 0 #we re-initialise the value in the grid (tgrille)
            #if user wants an hint, he presses the hint button
            if event.type == pygame.MOUSEBUTTONUP and hintbutt.mouseon():
                hint_c += 1 # we add one to the counter
                boo = True # we create a loop that turns until one value is printed on the screen
                while boo:
                    x = random.randint(0,8) #we generated random coordinates
                    y = random.randint(0,8)
                    if grille.cells[x][y].value == 0: #if the coordinate are the ones of an empty cell, we change values in the grid, by the right values (from solvedS)
                        grille.cells[x][y].value = solvedS[x][y]
                        grille.ugrille[x][y] = solvedS[x][y]
                        grille.cells[x][y].printnum_incell(ecran) #we use the method printnum_incell to print the values on the screen
                        break #we break the loop
                ecran.fill((255,255,255))
                grille.printgrid(ecran) #we update the screen
            #if user wants to solve sudoku, he presses solve button, which calls solvefunc with the actual grid as arguments
            #once solvefunc has finished the grid, summary() is called (see at the start of the function)
            if event.type == pygame.MOUSEBUTTONUP and solvebutt.mouseon():
                solvefunc(ecran, grille.ugrille, grille.cells)
        pygame.display.update()

################################################################
def fillin():
    '''
    This is the fillin screen, coming after User generating from startmenu
    User can fill in his own Sudoku
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('fillin')
    ecran.fill((255,255,255))

    grille = usergrid(540,540)
    grille.printgrid(ecran)

    l1 = text((0,0,0),850, 50, 15,'Please, fill in the initial grid you want to solve.')
    l2 = text((0,0,0),850, 70, 15,'When you are done, press Val')

    valbutt = button((0,0,0),850,250, 100,50,'Val')
    backbutt= button((0,0,0), 850,520, 100,50,'Back')

    running = True
    while running:
        l1.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l2.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        valbutt.printbutt(ecran)
        backbutt.printbutt(ecran)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
              startmenu()
             #we let user fill in his own sudoku, but use verify function to make sure the input sudoku is not impossible
            if event.type == pygame.KEYDOWN and (100<pygame.mouse.get_pos()[0]<640) and (30<pygame.mouse.get_pos()[1]<570):
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 \
                or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    if verify(grille.ugrille, (grille.mouseon()[1],grille.mouseon()[0]), event.key-48):
                        ssfont = pygame.font.SysFont('comicsans',50)
                        fill = ssfont.render(str(event.key-48), True, (124,234,255))
                        ecran.blit(fill,((grille.mouseon()[0])*60+115,(grille.mouseon()[1])*60+25))
                        grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value = event.key-48
                        grille.ugrille[grille.mouseon()[1]][grille.mouseon()[0]] = event.key-48 #here, we have a necessary inversion (see 1 before 0)
            #once user is done, he presses val and is transferred to play screen, with the inputed grid as arguments
            if event.type == pygame.MOUSEBUTTONUP and valbutt.mouseon():
                 play(grille.ugrille, grille.cells)
            #user can erase an input values, if he made a mistake
            if event.type == pygame.KEYDOWN and (100<pygame.mouse.get_pos()[0]<640) and (30<pygame.mouse.get_pos()[1]<570):
                if event.key == pygame.K_BACKSPACE:
                    pygame.draw.rect(ecran, (255,255,255), pygame.Rect((grille.mouseon()[0])*60+105,(grille.mouseon()[1])*60+35, 50,50))
                    grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value = 0
                    grille.ugrille[grille.mouseon()[1]][grille.mouseon()[0]] = 0

        pygame.display.update()

################################################################
def play(g, c):
    '''
    This is the play screen, coming after fillin. (similar to rndgen screen, expect for the inversion from fillin function)
    User can fill in the grid
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('play')
    ecran.fill((255,255,255))

    grille = usergrid(540,540)
    grille.ugrille = g
    grille.cells = c

    copyugrille = deepcopy(grille.ugrille)
    solver = SolveSudok(copyugrille)
    solvedS, recurs  = solver[1],solver[2]
    grille.printgrid(ecran)

    backbutt= button((0,0,0), 850,520, 100,50,'Back')
    hintbutt= button((0,0,0), 850,100, 100,50,'Hint')
    valbutt = button((0,0,0), 850,300, 100,50,'Val')
    Solvebutt = button((0,0,0), 850,200, 100,50,'Solve')

    debut = time.time()

    hint_c = 0

    running = True
    while running:

        pygame.draw.rect(ecran,(255,255,255),pygame.Rect(700,430,300,25),0)
        temps_passe = time.time()-debut
        print_temps_passe = time.strftime('%M:%S', time.gmtime(temps_passe))
        ffont = pygame.font.Font('Police/8-bit-operator/8bitOperatorPlus-Regular.ttf',20)
        fill = ffont.render('Clock:' +str(print_temps_passe), True, (0,0,0))
        ecran.blit(fill,(730,430))

        backbutt.printbutt(ecran)
        hintbutt.printbutt(ecran)
        valbutt.printbutt(ecran)
        Solvebutt.printbutt(ecran)

        if np.sum(grille.ugrille) == 405:
            summary(grille.ugrille, grille.cells, grille.errpron, print_temps_passe, solver[2], hint_c)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
                startmenu()
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(ecran,(124,234,255),pygame.Rect(grille.mouseon()[0]*60+103,grille.mouseon()[1]*60+33,55,55),2)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                pygame.draw.rect(ecran,(255,255,255),pygame.Rect(grille.mouseon()[0]*60+103,grille.mouseon()[1]*60+33,55,55),2)
            if event.type == pygame.KEYDOWN and (100<pygame.mouse.get_pos()[0]<640) and (30<pygame.mouse.get_pos()[1]<570):
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 \
                or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    if grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value == 0:
                        ffont = pygame.font.SysFont('comicsans',50)
                        fill = ffont.render(str(event.key-48), True, (124,234,255))
                        ecran.blit(fill,((grille.mouseon()[0])*60+115,(grille.mouseon()[1])*60+20))
                        if event.key-48==solvedS[grille.mouseon()[1]][grille.mouseon()[0]]:
                            grille.tgrille[grille.mouseon()[1]][grille.mouseon()[0]]= event.key-48
                        if event.key-48 != solvedS[grille.mouseon()[1]][grille.mouseon()[0]]:
                            grille.errpron += 1
            if event.type == pygame.MOUSEBUTTONUP and valbutt.mouseon():
                    ecran.fill((255,255,255))
                    grille.ugrille = grille.ugrille+grille.tgrille
                    for i in range(9):
                        for j in range(9):
                            grille.cells[i][j].value = grille.ugrille[j][i]
                    grille.printgrid(ecran)
                    grille.tgrille = np.zeros((9,9), dtype = int)
            if event.type == pygame.KEYDOWN and (100<pygame.mouse.get_pos()[0]<640) and (30<pygame.mouse.get_pos()[1]<570):
                if event.key == pygame.K_BACKSPACE:
                    if grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value == 0:
                        pygame.draw.rect(ecran, (255,255,255), pygame.Rect((grille.mouseon()[0])*60+105,(grille.mouseon()[1])*60+35, 50,50))
                        grille.cells[grille.mouseon()[0]][grille.mouseon()[1]].value = 0
                        grille.ugrille[grille.mouseon()[1]][grille.mouseon()[0]] = 0
                        if grille.tgrille[grille.mouseon()[1]][grille.mouseon()[0]] == 0:
                            grille.errpron -= 1
                        grille.tgrille[grille.mouseon()[1]][grille.mouseon()[0]] = 0
            if event.type == pygame.MOUSEBUTTONUP and hintbutt.mouseon():
                hint_c += 1
                boo = True
                while boo:
                    x = random.randint(0,8)
                    y = random.randint(0,8)
                    if grille.cells[y][x].value == 0:
                        grille.cells[y][x].value = solvedS[x][y]
                        grille.ugrille[x][y] = solvedS[x][y]
                        grille.cells[y][x].printnum_incell(ecran)
                        break
                ecran.fill((255,255,255))
                grille.printgrid(ecran)
            if event.type == pygame.MOUSEBUTTONUP and Solvebutt.mouseon():
                usersolvefunc(ecran, grille.ugrille, grille.cells)
        pygame.display.update()

################################################################
def summary(g,c,e,t,r,h):
    '''
    This is the summary screen
    User sees summary statistics about the sudoku that they finished
    '''
    ecran = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('summary')
    ecran.fill((255,255,255))

    #we get all the wanted 'statistics' on the solved sudoku from the play or rndgen function
    grille = usergrid(540,540)
    grille.ugrille = g
    grille.cells = c
    grille.errpron = e
    print_temps_passe = t
    recurs = r
    hint_c = h

    grille.printgrid(ecran)

    backbutt = button((0,0,0), 740,520, 200,50,'Main Menu')
    l1 = text((0,0,255),850, 100, 40,'Well done!')
    l2 = text((0,0,0),840, 150, 20,'You have finished the sudoku.')
    l3 = text((0,0,0),840, 250, 20,'You have filled in '+str(recurs)+' cells.')
    l4 = text((0,0,0),840, 300, 20,'It took you '+str(print_temps_passe)+' (min:sec).')
    l5 = text((0,0,0),840, 350, 20,'You have used '+str(hint_c)+' hint(s).')

    running = True
    while running:
        l1.printtxt(ecran)
        l2.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l3.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l4.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        l5.printtxt(ecran,'Police/open-sans/OpenSans-Light.ttf')
        backbutt.printbutt(ecran)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and backbutt.mouseon():
                mainmenu()

        pygame.display.update()
