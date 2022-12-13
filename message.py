import sys
import pygame
from pygame.locals import *

class MESSAGE:
    def __init__(self, msg, x, y, window):
        font_style = pygame.font.SysFont(None, 100)
        
        mesg_w, mesg_h = font_style.size(msg)
        mes = font_style.render(msg, True, "black")
    
        window.blit(mes, [x - mesg_w/2, y])
