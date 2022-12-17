import sys
import pygame
from pygame.locals import *
from pygame.math import Vector2
from fruit import FRUIT
from player import SNAKE
from control_panel import CONTROL_PANEL

class MAIN:
    def __init__(self, window, cell_size, map_size, map_pos):
        self.apple_image = pygame.image.load("apple.png").convert_alpha()
        self.fruit = FRUIT(5, 5, window, cell_size, map_size, map_size, self.apple_image, map_pos)
        self.snake = SNAKE(window, cell_size, map_pos)
        self.control_keys = CONTROL_PANEL(580, 1700, window)
        #create panel
                
    def update(self):
         self.snake.move_snake()
         self.check_collision()
         self.check_fail()
         
    def draw_elements(self):
         self.fruit.draw_fruit()
         self.snake.draw_snake()
         
    def check_collision(self):
          if self.fruit.pos == self.snake.body[0]:
              self.fruit.randomize()
              self.snake.add_block()
              
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.fruit.map_w or not 0 <= self.snake.body[0].y < self.fruit.map_h:
            self.game_over()
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def game_over(self):
        pygame.quit()
        sys.exit()
        
    def handle_user_input(self, ev):

        if (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_left.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_LEFT):
            if self.snake.direction.x != 1:
                self.snake.direction = Vector2(-1, 0)
        elif (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_right.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_RIGHT):
            if self.snake.direction.x != -1:
                self.snake.direction = Vector2(1, 0)
        elif (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_up.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_UP):
            if self.snake.direction.y != 1:
                self.snake.direction = Vector2(0, -1)
        elif (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_down.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_DOWN):
            if self.snake.direction.y != -1:
                self.snake.direction = Vector2(0, 1)
