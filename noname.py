#! /usr/bin/env python
#coding=utf-8

import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
COBALTGREEN = (61, 145, 64)
DARKBLUE = (25, 25, 112)
DARKGRAY = (40, 40, 40)
GRAY = (140, 140, 140)
FORESTGREEN = (34, 139, 34)
GOLDENROD = (218, 165, 32)
GREEN = (0, 255, 0)
IVORY = (205, 205, 193)
ORANGE = (255, 127, 0)
PINK = (255, 105, 180)
PURPLE = (142, 56, 142)
RED = (255, 0, 0)
SLATEBLUE = (131, 111, 255)
YELLOW = (238, 238, 0)

CELLSIZE = 20
WINDOWWIDTH = 706
WINDOWHEIGHT = 530

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

grid = []
margin = 2

def createGrid():
    for x in range(WINDOWWIDTH / CELLSIZE):
        grid.append([])
        for y in range(WINDOWHEIGHT / CELLSIZE):
            grid[x].append(False)
            

def changeGrid((x,y)):
    grid[x][y] = not grid[x][y]

def drawGrid():
    for x in range(WINDOWWIDTH / CELLSIZE):
        for y in range(WINDOWHEIGHT / CELLSIZE):
            if grid[x][y] == True:
                color = BLUE
            else:
                color = GRAY
            pygame.draw.rect(screen, color, [(margin+CELLSIZE)*x+margin, (margin+CELLSIZE)*y+margin,CELLSIZE,CELLSIZE])
    
createGrid()    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = pos[0]//(CELLSIZE+margin), pos[1] // (CELLSIZE+margin)
            #print 'mouse pos', pos
            #print 'row, col', row, col
            changeGrid((row,col))

    drawGrid()
    pygame.display.update()
    clock.tick(30)
    

