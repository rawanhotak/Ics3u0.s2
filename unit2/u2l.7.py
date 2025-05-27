import pygame
from pygame.locals import *
gameOn = True
pygame.init() # initialize the game window
# pygame needs a window
screen = pygame.display.set_mode((500, 400), 0, 32) # define the window size and position
pygame.display.set_caption('Drawing - Press q to quit')
WHITE = (255, 255, 255)
screen.fill(WHITE)
count = 0
sensitivity = 10
