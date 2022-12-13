import sys
import pygame
from pygame.locals import *
from fruit import FRUIT
from player import SNAKE

class MAIN:
    def __init__(self, window, cell_size, map_size, map_pos):
        self.apple_image = pygame.image.load("apple.png").convert_alpha()
        self.fruit = FRUIT(5, 5, window, cell_size, map_size, map_size, self.apple_image, map_pos)
        self.snake = SNAKE(window, cell_size, map_pos)
                
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