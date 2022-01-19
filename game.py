""" 
Pysnake - Yet Another PyGame Snake Clone

This is just a simple project to familiarize myself with pygame.

I also intend to remember the usage of GIT, pythonics best practices,
and overall python development.

Luiz Marin
"""

from turtle import width
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


class Snake(object):
    def __init__(self, size, speed, snake_pixels):
        self.size = 10
        self.speed = 8
        self.snake_pixels = snake_pixels

    def draw(size, snake_pixels):
        for pixel in snake_pixels:
            pygame.draw.rect(game_screen, white, [pixel[0], pixel[1], size, size])


def game():

    game_over = False

    while not game_over:

        # Set background
        game_screen.fill(black)


if __name__ == '__main__':
    game()
