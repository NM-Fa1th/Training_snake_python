import sys
import pygame
from pygame.locals import *
from pygame.math import Vector2
from message import MESSAGE

class SNAKE:
    def __init__(self, window, size, map_pos):
        self.body = [Vector2(5, 2), Vector2(5, 1), Vector2(5, 0)]
        self.window = window
        self.size = size
        self.direction = Vector2(0,1)
        self.new_block = False
        self.map_pos = map_pos
        
        self.head_up = pygame.image.load("head_up.png").convert_alpha()
        self.head_down = pygame.image.load("head_down.png").convert_alpha()
        self.head_left = pygame.image.load("head_left.png").convert_alpha()
        self.head_right = pygame.image.load("head_right.png").convert_alpha()
        
        self.tail_up = pygame.image.load("tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("tail_right.png").convert_alpha()
        
        self.body_horizontal = pygame.image.load("body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load("body_vertical.png").convert_alpha()
        
        self.body_tl = pygame.image.load("body_tl.png").convert_alpha()
        self.body_tr = pygame.image.load("body_tr.png").convert_alpha()
        self.body_bl = pygame.image.load("body_bl.png").convert_alpha()
        self.body_br = pygame.image.load("body_br.png").convert_alpha()
        
        self.head = self.head_down
        self.tail = self.tail_down
        
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            x_pos = int(block.x * self.size) + self.map_pos
            y_pos = int(block.y * self.size) + self.map_pos
            block_rect = pygame.Rect(x_pos, y_pos, self.size, self.size)
            
            if index == 0:
                self.window.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.window.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
                    self.window.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.window.blit(self.body_horizontal, block_rect)
                else:
                    #MESSAGE("debug " + str(previous_block) + str(next_block)  , 250, 25, self.window)
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == - 1 and next_block.x == -1 :
                        #MESSAGE("debug", 250, 25, self.window)
                        self.window.blit(self.body_tl, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == - 1 and next_block.x == 1 :
                        #MESSAGE("debug", 250, 25, self.window)
                        self.window.blit(self.body_tr, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1 :
                        #MESSAGE("debug", 250, 25, self.window)
                        self.window.blit(self.body_bl, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1 :
                        #MESSAGE("debug", 250, 25, self.window)
                        self.window.blit(self.body_br, block_rect)
                        
                        
    def update_head_graphics(self):
        head_relation = self.body[0] - self.body[1]
        
        if head_relation == Vector2(1, 0): 
            self.head = self.head_right
        if head_relation == Vector2(-1, 0): 
            self.head = self.head_left
        if head_relation == Vector2(0, 1): 
            self.head = self.head_down
        if head_relation == Vector2(0, -1): 
            self.head = self.head_up
            
    def update_tail_graphics(self):
        tail_relation = self.body[-1] - self.body[-2]
        
        if tail_relation == Vector2(1, 0): 
            self.tail = self.tail_left
        if tail_relation == Vector2(-1, 0): 
            self.tail = self.tail_right
        if tail_relation == Vector2(0, 1): 
            self.tail = self.tail_up
        if tail_relation == Vector2(0, -1): 
            self.tail = self.tail_down
            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]

        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[ : ]
        
    def add_block(self):
        self.new_block = True
        

        