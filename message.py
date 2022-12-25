import sys
import pygame
from pygame.locals import *

class MESSAGE:
    def __init__(self, x, y, window):
        self.window = window
        self.x = x
        self.y = y
        self.font_style = pygame.font.SysFont(None, 100)
        
        self.msg = ""
        
        self.mesg_w, self.mesg_h = 0, 0
        self.mes = self.font_style.render(self.msg, True, "black")
        
    def set_msg(self, msg):
        self.msg = msg
        self.mesg_w, self.mesg_h = self.font_style.size(msg)
        self.mes = self.font_style.render(self.msg, True, "black")
        
        
    def draw_message(self):
        self.window.blit(self.mes, [self.x - self.mesg_w/2, self.y])
