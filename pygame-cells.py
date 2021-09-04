import sys
import pygame
from pygame.locals import *
import cells

# pygame setup --------------
pygame.init()

# colors
alive_color = pygame.Color(128, 128, 0)
dead_color = pygame.Color(50, 50, 50)
line_color = pygame.Color(100, 100, 100)

FPS = 30
Frames = pygame.time.Clock()

DISP = pygame.display.set_mode((500, 500))
DISP.fill(dead_color)
pygame.display.set_caption('Cellular automaton')
# ---------------------------



# game loop =======
exit = False
while not exit:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit = True
            
    Frames.tick(FPS)
# =================
# exit sequence
pygame.quit()
sys.exit()
