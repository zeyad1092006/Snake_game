# draw snake
# draw food
# draw score
# draw gameover text
# draw background
import pygame
import config
from snake import *
from food import *
class render:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.WIDTH , config.HEIGHT))
        self.green = config.COLORES['green']
        self.red = config.COLORES['red']
        self.white = config.COLORES['white']
        self.background = config.COLORES['navy']
        self.font = pygame.font.Font(None, 24)
        self.block_size = config.BLOCK_SIZE
        
    def draw_background(self):
        self.screen.fill(self.background)

    def draw_snake(self, snake:"Snake"):
        for x , y in snake.snake_body:
            pygame.draw.rect(self.screen, self.green,
                [x , y ,self.block_size, self.block_size] )

    def draw_food(self, food:"Food"):
        x_food = food.position[0]
        y_food = food.position[1]
        pygame.draw.rect(self.screen, self.red,
            [x_food, y_food ,self.block_size, self.block_size])

    def draw_score(self, score):
        text = self.font.render(f"Score: {str(score)}",True, self.white)
        self.screen.blit(text, (10,10))

    def draw_game_over(self):
        text = self.font.render(f"Game Over", True, self.red)
        center_x = self.screen.get_width() // 2 - text.get_width() // 2
        center_y = self.screen.get_height() // 2 - text.get_height() // 2
        self.screen.blit(text, (center_x, center_y) )

        