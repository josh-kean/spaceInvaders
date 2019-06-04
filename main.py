import pygame
from invaders import invaders


pygame.init()

width = 500
height = width
display = pygame.display.set_mode((width, height))

colors = {'white': (255, 255, 255), 'black': (0,0,0)}
clock = pygame.time.Clock()

def create_invader_positions():
    positions = []
    for x in range(50, width-50,50):
        for y in range(50, 50*3, 50):
            positions.append([x,y])
    return positions

def space_invaders(display):
    invaderOne = invaders(display)
    event = pygame.event.poll()
    #attacked willl be true if the invader collides with the player
    attacked = False
    event = pygame.event.poll()
    while attacked == False:
        for event in pygame.event.get():
            pygame.quit()
            quit()

        display.fill(colors['white'])
        for position in create_invader_positions():
            invaders(display, position).draw_invader()
        pygame.display.update()
        clock.tick(10)

def start_screen():
    # display.fill(colors['white'])
    space_invaders(display)
    pygame.display.update()

start_screen()
