import pygame
import random
import numpy

class Config:
    BLOCK_SIZE = 40
    BORDER_WIDTH = BLOCK_SIZE // 4
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SCREEN_BLOCKS_FILL = (SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE)

    COLORS = {
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'RED': (255, 0, 0),
        'GREEN': (0, 128, 0),
        'DARK_VIOLET': (127, 0, 255),
        'YELLOW': (255, 255, 0),
        'LAVENDER': (230, 230, 250),
        'DARK_MAGENTA': (139, 0, 139),
        'THISTLE': (216, 191, 216),
        'MEDIUM_SLATE_BLUE': (123, 104, 238),
        'OLD_LACE': (255, 248, 232),
        'TURQUOISE': (48, 213, 200),
        'BURNT_ORANGE': (191, 87, 0)
    }

    FPS = 15
    FONT_STYLE = 'Azonix'

class Snake:
    def __init__(self):
        self.position = [Config.BLOCK_SIZE * 5 % Config.SCREEN_WIDTH, Config.BLOCK_SIZE * 3 % Config.SCREEN_HEIGHT]
        self.body = [[Config.BLOCK_SIZE * 5 % Config.SCREEN_WIDTH, Config.BLOCK_SIZE * 3 % Config.SCREEN_HEIGHT],
                     [Config.BLOCK_SIZE * 4 % Config.SCREEN_WIDTH, Config.BLOCK_SIZE * 3 % Config.SCREEN_HEIGHT],
                     [Config.BLOCK_SIZE * 3 % Config.SCREEN_WIDTH, Config.BLOCK_SIZE * 3 % Config.SCREEN_HEIGHT]]
        self.direction = 'RIGHT'
        self.block_size = Config.BLOCK_SIZE

    def move(self, grow = False):
        if self.direction == 'UP':
            self.position[1] -= self.block_size
        elif self.direction == 'DOWN':
            self.position[1] += self.block_size
        elif self.direction == 'LEFT':
            self.position[0] -= self.block_size
        elif self.direction == 'RIGHT':
            self.position[0] += self.block_size

        self.body.insert(0, list(self.position))

        if not grow:
            self.body.pop()

    def change_direction(self, new_direction: str):
        opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction
        
    def check_collision(self) -> bool:
        if self.position[0] < 0 or self.position[0] >= Config.SCREEN_WIDTH:
            return True
        if self.position[1] < 0 or self.position[1] >= Config.SCREEN_HEIGHT:
            return True
        
        for block in self.body[1:]:
            if self.position[0] == block[0] and self.position[1] == block[1]:
                return True
        
        return False
    
    def check_food_collision(self, food_position) -> bool:
        return self.position[0] == food_position[0] and self.position[1] == food_position[1]
    
    def draw(self, screen):
        for position in self.body:
            pygame.draw.rect(screen, Config.COLORS['DARK_VIOLET'], pygame.Rect(position[0], position[1], self.block_size - Config.BORDER_WIDTH, 
                                                                                self.block_size - Config.BORDER_WIDTH))

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.block_size = Config.BLOCK_SIZE

    def generate_position(self):
        return [random.randrange(0, Config.SCREEN_WIDTH // Config.BLOCK_SIZE) * Config.BLOCK_SIZE, 
                random.randrange(0, Config.SCREEN_HEIGHT // Config.BLOCK_SIZE) * Config.BLOCK_SIZE]
    
    def respawn(self, snake_body):
        food_spawned = False
        while not food_spawned:
            self.position = self.generate_position()
            if self.position not in snake_body:
                food_spawned = True

    def draw(self, screen):
        pygame.draw.rect(screen, Config.COLORS['DARK_MAGENTA'], 
                         pygame.Rect(self.position[0], self.position[1], self.block_size - Config.BORDER_WIDTH, self.block_size - Config.BORDER_WIDTH))
    
class Grid:
    def __init__(self):
        self.blocks = numpy.zeros(Config.SCREEN_BLOCKS_FILL)
        self.block_size = Config.BLOCK_SIZE
        self.border_width = Config.BORDER_WIDTH

    def draw(self, screen):
        for x, y in numpy.ndindex(self.blocks.shape):
            pygame.draw.rect(screen, Config.COLORS['LAVENDER'], 
                             (x * self.block_size, y * self.block_size, self.block_size - self.border_width, self.block_size - self.border_width))
    
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont(Config.FONT_STYLE, Config.BLOCK_SIZE * 2 % min(Config.SCREEN_HEIGHT, Config.SCREEN_WIDTH))

    def increase(self):
        self.value += 1

    def draw(self, screen):
        score_text = self.font.render('SCORE: ' + str(self.value), True, Config.COLORS['BURNT_ORANGE'])
        screen.blit(score_text, [10, 10])
    
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()
        self.grid = Grid()
        self.score = Score()
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                    self.snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                    self.snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                    self.snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                    self.snake.direction = 'RIGHT'

    def update(self):
        grow = self.snake.check_food_collision(self.food.position)

        self.snake.move(grow = grow)

        if grow:
            self.score.increase()
            self.food.respawn(self.snake.body)

        if self.snake.check_collision():
            self.running = False
    
    def draw(self):
       self.screen.fill(Config.COLORS['WHITE'])
       self.grid.draw(self.screen)
       self.snake.draw(self.screen)
       self.food.draw(self.screen)
       self.score.draw(self.screen)
       pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(Config.FPS)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()