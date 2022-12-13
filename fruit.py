import sys
import pygame
from pygame.locals import *
from pygame.math import *
import random

class FRUIT:
    
    def __init__(self, x, y, surface, size, map_w, map_h, img, map_pos):
        self.color = pygame.Color("purple")
        self.surface = surface
        self.size = size
        self.map_w = map_w
        self.map_h = map_h
        self.randomize()
        self.img = img
        self.map_pos = map_pos
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * self.size) + self.map_pos, int(self.pos.y * self.size) + self.map_pos, self.size, self.size)
        self.surface.blit(self.img, fruit_rect)
        #pygame.draw.rect(self.surface, self.color, fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, self.map_w-1)
        self.y = random.randint(0, self.map_h-1)
        self.pos = Vector2(self.x, self.y)
        
        