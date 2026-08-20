from snake import *
from food import *
from render import *
import config
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.speed = config.GAME_SPEED
        self.block_size = config.BLOCK_SIZE
        self.score = config.SCORE
        self.screen = pygame.display.set_mode((self.width , self.height))
        pygame.display.set_caption("Snake Game")

        self.snake = Snake(self.block_size  , self.width //2 , self.height// 2)
        self.food = Food(self.block_size , self.width , self.height , self.snake.snake_body)
        self.render = Render(self.screen)

        self.running = True
        self.game_over = False

    def run(self):
        while self.running:
            self.handle_events()
            self.render.draw_background()

            if not self.game_over:
                self.snake.move()

                if self.did_eat():
                    self.score += 1
                    self.food = Food(self.block_size, self.width, self.height, self.snake.snake_body)
                    self.speed += 1
                else:
                    self.snake.remove_tail()

                if self.did_collide():
                    self.game_over = True

            self.render.draw_snake(self.snake)
            self.render.draw_food(self.food)
            self.render.draw_score(self.score)

            if self.game_over:
                self.render.draw_game_over()
                pygame.display.flip()
                # pygame.time.wait(2000)
                
            pygame.display.flip()
            if not self.game_over:
                # pygame.display.flip()
                self.clock.tick(self.speed)
                
        pygame.quit()     
                



    def did_eat(self):
        return (
        self.snake.head[0] == self.food.position[0] 
        and self.snake.head[1] == self.food.position[1]
        )

    def did_collide(self):
        return (
            self.snake.head[0] < 0 
            or self.snake.head[0] >= self.width
            or self.snake.head[1] < 0
            or self.snake.head[1] >= self.height
            or self.snake.head in self.snake.snake_body[1:]
        )





    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key  == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                else:
                    self.handle_key_press(event.key)


    def handle_key_press(self, key):
        if key == pygame.K_UP and self.snake.diretion != 'down':
            self.snake.diretion = "up"
        
        if key == pygame.K_DOWN and self.snake.diretion != 'up':
            self.snake.diretion = "down"
        
        if key == pygame.K_RIGHT and self.snake.diretion != 'left':
            self.snake.diretion = "right"
        
        if key == pygame.K_LEFT and self.snake.diretion != 'right':
            self.snake.diretion = "left"


    def restart_game(self):
        self.snake = Snake(self.block_size  , self.width //2 , self.height// 2)
        self.food = Food(self.block_size , self.width , self.height , self.snake.snake_body)
        self.score = config.SCORE
        self.speed = config.GAME_SPEED
        self.game_over = False
