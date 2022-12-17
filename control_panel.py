import sys
import pygame
from pygame.locals import *

class CONTROL_PANEL:
    def __init__(self, x, y, window):
            self.blue = (34,78,56)
            
            self.btn_left = pygame.Rect((x - 128, y + 128), (128,128))
            self.btn_right = pygame.Rect((x+128, y + 128), (128, 128))
            self.btn_up = pygame.Rect((x, y), (128, 128))
            self.btn_down = pygame.Rect((x, y + 256), (128, 128))
    
            self.btn_restart = pygame.Rect((x + 40, y - 350), (320, 128))
            self.window = window
            
    def draw_btns(self):
        self.window.fill(self.blue, self.btn_left, 1)
        self.window.fill(self.blue, self.btn_right, 1)
        self.window.fill(self.blue, self.btn_up, 1)
        self.window.fill(self.blue, self.btn_down, 1)
        
        self.window.fill(self.blue, self.btn_restart)