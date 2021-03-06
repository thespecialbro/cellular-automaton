import sys
import math
import pygame
from pygame.locals import *
import cells

# pygame setup --------------
pygame.init()

# colors
alive_color =     (255, 255,   0)
dead_color =      ( 50,  50,  50)
highlight_color = (128, 128,   0)
highlight_color2= (200, 200,   0)
line_color =      (100, 100, 100)
text_color =      (  0, 255,   0)

FPS = 60
Frames = pygame.time.Clock()

disp_d = (500, 500)
DISP = pygame.display.set_mode(disp_d)
DISP.fill(dead_color)
pygame.display.set_caption('Cellular automaton')

text_font = pygame.font.SysFont('monospace', 14)
# ---------------------------

# life setup
grid_width = 50 # how many cells wide the grid is
grid_height = 50 # how many cells tall the grid is
cell_w = disp_d[0]/grid_width
cell_h = disp_d[1]/grid_height
GRID = None

def highlight_square(x, y):
    # highlight the square the mouse cursor is within
    # given coords are the mouse's position within the window
    hx = math.floor(x/disp_d[0]*grid_width)
    hy = math.floor(y/disp_d[1]*grid_height)
    color = highlight_color
    if GRID.grid[hy][hx].state: # slightly diff highlight color when over alive squares
        color = highlight_color2
    pygame.draw.rect(DISP, color, (hx*cell_w, hy*cell_h, cell_w, cell_h))
    return (hx, hy) # grid coordinates of the highlighted square


exit = False
running = False # whether the cells sim is running
frame_count = 0
generation_count = 0 # how many generations have passed in the simulation

def reset_grid():
    global GRID
    global generation_count
    GRID = cells.Grid(w=grid_width, h=grid_height)
    generation_count = 0

reset_grid() # initialize the grid of cells for the first time

# main loop =======
while not exit:
    frame_count += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            k = pygame.key.get_pressed()
            if k[pygame.K_SPACE]:
                running = not running # play/pause the cell simulation
            if k[pygame.K_r]:
                print('Resetting grid.')
                reset_grid()
                running = False

    for i in range(grid_height):
        for j in range(grid_width):
            draw_color = dead_color
            if GRID.grid[i][j].state:
                draw_color = alive_color
            pygame.draw.rect(DISP, draw_color, (j*cell_w, i*cell_h, cell_w, cell_h))

    if running and frame_count % 5 == 0:
        # simulate the cells
        GRID.step()
        generation_count += 1

    # highlight square the mouse is over
    mpos = pygame.mouse.get_pos()
    highltd = (0, 0) # grid coordinates of the highlighted square
    if 500 > mpos[0] > 0 and 500 > mpos[1] > 0:
        highltd = highlight_square(mpos[0], mpos[1])
        if pygame.mouse.get_pressed()[0]:
            GRID.grid[highltd[1]][highltd[0]].state = 1
        elif pygame.mouse.get_pressed()[2]:
            GRID.grid[highltd[1]][highltd[0]].state = 0


    # draw grid lines
    for i in range(grid_height + 1):
        pygame.draw.line(DISP, line_color, (0, cell_h*i), (disp_d[0], cell_h*i))

    for i in range(grid_width + 1):
        pygame.draw.line(DISP, line_color, (cell_w*i, 0), (cell_w*i, disp_d[1]))

    label = text_font.render('{}'.format(generation_count), 2, text_color)
    DISP.blit(label, (5, 5))

    pygame.display.update()
    Frames.tick(FPS)
# =================

# exit sequence
print('Exiting.')
print('Generations passed:', generation_count)
pygame.quit()
sys.exit()
