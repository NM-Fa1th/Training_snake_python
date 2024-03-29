import sys
import pygame
from pygame.locals import *
from pygame.math import Vector2
from fruit import FRUIT
from player import SNAKE
from control_panel import CONTROL_PANEL
from message import MESSAGE

class MAIN:
    def __init__(self, window, cell_size, map_size, map_resolution):
        
        self.window = window
        self.cell_size = cell_size
        self.map_size = map_size
        
        self.dis_w, self.dis_h = self.window.get_size()
        
        self.orientation = 'vertical'
        
        self.map_margin = 10
        
        self.map_resolution = map_resolution
        
        self.control_keys = CONTROL_PANEL(580, 1700, window)
        
        self.hor1, self.hor2 = MESSAGE(500, 25, self.window), MESSAGE(500, 50, self.window)

        #self.check_orientation()
        
        self.map = pygame.Rect((self.map_margin, self.map_margin), (map_resolution, map_resolution))
        
        self.apple_image = pygame.image.load("apple.png").convert_alpha()
        self.fruit = FRUIT(5, 5, window, cell_size, map_size, map_size, self.apple_image, self.map_margin)
        self.snake = SNAKE(window, cell_size, self.map_margin)
        

                
    def update(self):
         self.check_orientation()
         self.map = pygame.Rect((self.map_margin, self.map_margin), (self.map_resolution, self.map_resolution))

         print("move")
         self.snake.move_snake()
         self.check_collision()
         self.check_fail()
         
    def draw_elements(self):
         self.draw_grass()
         self.fruit.draw_fruit()
         self.snake.draw_snake()
         self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_snd()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
              
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.fruit.map_w or not 0 <= self.snake.body[0].y < self.fruit.map_h:
            print("game over wall")
            self.game_over()
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                print("game over body" + str(self.snake.body) + str(block))
                self.game_over()
                
    def game_over(self):
        self.snake.play_game_over_snd()
        self.snake.reset()
        
    def handle_user_input(self, ev):
            if (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_left.collidepoint(ev.pos)) or (ev.type == KEYDOWN  and ev.key == K_LEFT):
                self.snake.rotate_left()
            elif (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_right.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_RIGHT):
                self.snake.rotate_right()
            elif (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_up.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_UP):
                self.snake.rotate_up()
            elif (ev.type == MOUSEBUTTONDOWN and self.control_keys.btn_down.collidepoint(ev.pos)) or (ev.type == KEYDOWN and ev.key == K_DOWN):
                self.snake.rotate_down()
                    
    def check_orientation(self):
        self.dis_w, self.dis_h = self.window.get_size()
        if self.dis_w < self.dis_h:
            self.orientation = "vertical"
            #self.hor2.set_msg("ver")
        else:
            self.orientation = "horizontal"
            #self.hor2.set_msg("hor")

            
        if self.orientation == "vertical":
            self.map_margin = self.dis_w/2 - self.map_resolution/2
            self.control_keys.update_panel_pos(580, 1700)
            self.snake.map_pos = self.map_margin
            self.fruit.map_pos = self.map_margin
        else:
            self.map_margin = self.dis_h/2 - self.map_resolution/2
            self.control_keys.update_panel_pos(1100, 380)
            self.snake.map_pos = self.map_margin
            self.fruit.map_pos = self.map_margin
            #self.hor1.set_msg("ver")
            
    def draw_world(self):
                self.window.fill((35 * 1.2, 50 * 1.2, 0), self.map)
                self.draw_elements()
                self.control_keys.draw_btns()
                #self.hor1.draw_message()
                #self.hor2.draw_message()

    def draw_grass(self):
        grass_color = (35 * 1.2, 65 * 1.2, 18 * 1.2)

        for row in range(self.map_size):
            if row % 2 == 0:
                for col in range(self.map_size):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(self.map_margin + (col * self.cell_size), self.map_margin + (row * self.cell_size), self.cell_size, self.cell_size)
                        pygame.draw.rect(self.window, grass_color, grass_rect)
            else:
                for col in range(self.map_size):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(self.map_margin + (col * self.cell_size),
                                                 self.map_margin + (row * self.cell_size), self.cell_size,
                                                 self.cell_size)
                        pygame.draw.rect(self.window, grass_color, grass_rect)

    def draw_score(self):
        font_style = pygame.font.SysFont(None, 80)
        score_text = str(len(self.snake.body) - 3)
        score_surface = font_style.render(score_text, True, (60, 80, 20))
        score_x = (self.map_margin + (self.cell_size * self.map_size) - 60)
        score_y = (self.map_margin + (self.cell_size * self.map_size) - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.fruit.img.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width, apple_rect.height)

        pygame.draw.rect(self.window, (167, 209, 61), bg_rect)
        self.window.blit(score_surface, score_rect)
        self.window.blit(self.fruit.img, apple_rect)
        pygame.draw.rect(self.window, (60*1.5, 80*1.5, 20*1.5), bg_rect, 3)
