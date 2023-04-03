import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# Set the caption of the window
pygame.display.set_caption("Snake Game")

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the font
font = pygame.font.SysFont(None, 25)

# Define the snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(width / 2, height / 2)]
        self.direction = random.choice([up, down, left, right])
        self.color = green
    
    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0]*-1,point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*10)), (cur[1] + (y*10)))
        if new in self.positions[2:] or new[0] < 0 or new[0] > width-10 or new[1] < 0 or new[1] > height-10:
            self.reset()
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return True
    
    def reset(self):
        self.length = 1
        self.positions = [(width / 2, height / 2)]
        self.direction = random.choice([up, down, left, right])
    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (10, 10))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, black, r, 1)

# Define the food class
class Food:
    def __init__(self):
        x = random.randrange(0, width, 10)
        y = random.randrange(0, height, 10)
        self.position = (x, y)
        self.color = red
    
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (10, 10))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, black, r, 1)

# Define the directions
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Define the main function
def main():
    # Set the clock and the initial score
    clock = pygame.time.Clock()
    score = 0
    level = 1
    snake = Snake()
    food = Food()
    
    # Set the game loop
    while True:
        # Set the event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                   
