#!/usr/bin/python
import sys

import pygame
from pygame.locals import *
from message import MESSAGE
from main import MAIN


pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
# Resolution is ignored on Android
window = pygame.display.set_mode((1360, 720), pygame.DOUBLEBUF,  32)

red=(255,0,0)
green=(0,255,0)
blue=(34,78,56)
head_col = (50, 20, 150)
msg_col=(170, 70, 10)

wall_col=(0, 120, 0)

map = [
1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]
    
def blitWalls(suf, color, size, map):
    for i in range(len(map)):
        x = i%10 * size
        y = i//10 * size
        if(map[i] == 1):
            pygame.draw.rect(suf, color, [x, y, size, size])
            #msg(str(map[i]), red, x + size/2, y)
            
def game():
    
    #game_over = False
    
    map_size = 11
    #cell_size = int(dis_w/map_size)
    cell_size = 64
    map_resolution = cell_size * map_size
    
    clock = pygame.time.Clock()

    fps=30
    
    speed = 1.5
    
    #create game
    main_game = MAIN(window, cell_size, map_size, map_resolution)
    
    #timer to update
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, int(1000/speed))
    
    while True:
        
        #blitWalls(window, wall_col, cell_size, map)
        
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == SCREEN_UPDATE:
                main_game.update()
            if ev.type == MOUSEBUTTONDOWN or ev.type == KEYDOWN:
                main_game.handle_user_input(ev)

        #draw bg
        window.fill((100 * 0.9, 140 * 0.9, 0))
        
        #draw world
        main_game.draw_world()

        pygame.display.update()
        clock.tick(fps)

game()