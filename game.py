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

#Set basic PyGame initialization variables
pygame.init()
screen_size = (600, 400)
game_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PySnake")
clock = pygame.time.Clock()
