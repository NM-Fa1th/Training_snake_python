import sys
import pygame
from pygame.locals import *
from pygame.math import Vector2
from message import MESSAGE

class CONTROL_PANEL:
    def __init__(self, x, y, window):
            self.blue = (34,78,56)
            
            self.pos = Vector2(x, y)
            
            self.left_pos = Vector2(-128, 128)
            self.right_pos = Vector2(128, 128)
            self.up_pos = Vector2(0, 0)
            self.down_pos = Vector2(0, 256)
            
            self.restart_pos = Vector2(40, -350)
            
            self.btn_left = pygame.Rect(self.pos + self.left_pos, (128,128))
            self.btn_right = pygame.Rect(self.pos + self.right_pos, (128, 128))
            self.btn_up = pygame.Rect(self.pos + self.up_pos, (128, 128))
            self.btn_down = pygame.Rect(self.pos + self.down_pos, (128, 128))
    
            self.btn_restart = pygame.Rect(self.pos + self.restart_pos, (320, 128))
            self.window = window
            self.debug1 =  MESSAGE(250, 25, self.window)
            
    def update_panel_pos(self, x, y):
            self.pos = Vector2(x, y)
    
            self.btn_left.update(self.pos + self.left_pos, (128, 128))
            self.btn_right.update(self.pos + self.right_pos, (128, 128))
            self.btn_up.update(self.pos + self.up_pos, (128, 128))            
            self.btn_down.update(self.pos + self.down_pos, (128, 128))
    
            self.btn_restart.update(self.pos + self.restart_pos, (320, 128))
            self.debug1.set_msg(str(self.pos + self.left_pos))
            
        
            
    def draw_btns(self):
        self.window.fill(self.blue, self.btn_left, 1)
        self.window.fill(self.blue, self.btn_right, 1)
        self.window.fill(self.blue, self.btn_up, 1)
        self.window.fill(self.blue, self.btn_down, 1)
        
        self.window.fill(self.blue, self.btn_restart)
        self.debug1.draw_message()