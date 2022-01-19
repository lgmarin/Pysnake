""" 
Pysnake - Yet Another PyGame Snake Clone

This is just a simple project to familiarize myself with pygame.

I also intend to remember the usage of GIT and overall python development and best practices.

Luiz Marin
"""
import pygame
import time
import random

# Set basic PyGame initialization variables
pygame.init()
screen_size = (600, 400)
game_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()

# Define basic colors to be used later
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255,165,0)

# Set fonts for the game score and messages
message_font = pygame.font.SysFont('comicsans', 30)
score_font = pygame.font.SysFont('comicsans', 25)


class Snake(object):
    def __init__(self, x, y, size, speed):
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.pixels = []
        self.isAlive = True
        

    def move(self, length):
        # Move the snake by creating another pixel at front
        # If not eaten, then destroy last pixel
        self.pixels.append([self.x, self.y])
        if len(self.pixels) > length:
            del self.pixels[0]

        # Verify if the snake run into itself
        for pixel in self.pixels[:-1]:
            if pixel == [self.x,self.y]:
                self.isAlive = False

    def isAlive(self):
        if self.isAlive == False:
            return False

    def draw(self):
        for pixel in self.pixels:
            pygame.draw.rect(game_screen, white, [pixel[0], pixel[1], self.size, self.size])

def drawScore(score):
    """
    Draw Score on the screen
    """
    text =  score_font.render("Score: " + str(score), True, orange)
    game_screen.blit(text, [0,0])


def game():

    game_over = False
    game_closed = False

    # Define screeen boundaries and starting point
    max_x, max_y = screen_size
    x_speed = 0
    y_speed = 0
    Snake.pixels = []
    snake_length = 1

    #Create snake (x_pos, y_pos, size, speed)
    snake = Snake(max_x/2, max_y/2, 10, 8)

    # Random food position
    food_x = round(random.randrange(0, max_x - snake.size) / 10) * 10
    food_y = round(random.randrange(0, max_y - snake.size) / 10) * 10

    while not game_closed:

        while game_over:
            clock.tick(snake.speed)

            game_screen.fill(black)
            game_over_msg = message_font.render("Game Over!", True, red)
            game_screen.blit(game_over_msg, [max_x/3, max_y/3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
         # Prepare Pygame events for keystrokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_closed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake.size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake.size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake.size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake.size

        # Verify if the snake is out of boundary
        if snake.x >= max_x or snake.x < 0 or snake.y >= max_y or snake.y < 0:
            game_over = True

        # Add the speed (or movement) to the snake position
        snake.x += x_speed
        snake.y += y_speed

        # Set background and draw food
        game_screen.fill(black)
        pygame.draw.rect(game_screen, orange, [food_x, food_y, snake.size, snake.size])

        #Move Snake and verify if it have eaten it's own tail
        snake.move(snake_length)
        if snake.isAlive == False:
            game_over == True

        snake.draw()
        drawScore(snake_length - 1)

        pygame.display.update()

        # Verify if the snake is coliding with food
        if snake.x == food_x and snake.y == food_y:
            # Create more food, for the hungry snake
            food_x = round(random.randrange(0,max_x - snake.size) / 10.0) * 10.0
            food_y = round(random.randrange(0,max_y - snake.size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake.speed)
        
    pygame.quit()
    quit()

if __name__ == '__main__':
    game()
