# draw snake
# draw food
# draw score
# draw gameover text
# draw background
import pygame
import config
from snake import *
from food import *
class Render:
    def __init__(self,screen):
        self.screen = screen
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
        game_over_text = self.font.render(f"Game Over", True, self.red)
        restart_text = self.font.render(f"Press R to Restart", True, self.white)
        exit_text = self.font.render(f"Press ESC to Exit", True, self.white)
        center_x = self.screen.get_width() // 2 - game_over_text.get_width() // 2
        game_over_x = center_x - game_over_text.get_width() // 2
        restart_x = center_x - restart_text.get_width() // 2
        exit_x = center_x - exit_text.get_width() //2

        center_y = self.screen.get_height() // 2 - game_over_text.get_height() // 2

        self.screen.blit(game_over_text, (game_over_x, center_y - 50) )
        self.screen.blit(restart_text, (restart_x, center_y) )
        self.screen.blit(exit_text, (exit_x, center_y + 30) )

        