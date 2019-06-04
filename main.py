import pygame
from invaders import Invaders


pygame.init()

width = 500
height = width
display = pygame.display.set_mode((width, height))

colors = {'white': (255, 255, 255), 'black': (0,0,0)}
clock = pygame.time.Clock()

def create_invader_positions():
    positions = []
    for x in range(100, width-100,50):
        for y in range(50, 50*3, 50):
            positions.append([x,y])
    return positions

def create_invaders(display):
    listOfInvaders = []
    for position in create_invader_positions():
        listOfInvaders.append(Invaders(display, position))
    return listOfInvaders

def move_invaders(invaders):
    xPositions = [invader.position[0] for invader in invaders]
    if min(xPositions) > 0:
        return 50
    if max(xPositions) == width:
        return -50


def space_invaders(display):
    # invaderOne = invaders(display)
    event = pygame.event.poll()
    invaders = create_invaders(display)
    #attacked willl be true if the invader collides with the player
    attacked = False
    event = pygame.event.poll()
    moveInvaderX = 50
    moveInvaderY = 0
    while attacked == False:
        for event in pygame.event.get():
            pygame.quit()
            quit()

        display.fill(colors['white'])
        invaderPositionsX = [invader.position[0] for invader in invaders]
        invaderPositionsY = [invader.position[1] for invader in invaders]
        if min(invaderPositionsX) == 0:
            moveInvaderX = 50
            moveInvaderY = 50
        if max(invaderPositionsX) >= width:
            moveInvaderX = -50
            moveInvaderY = 50

        for invader in invaders:
            invader.position[0] += moveInvaderX
            invader.position[1] += moveInvaderY
            invader.draw_invader()
        moveInvaderY = 0
        pygame.display.update()
        clock.tick(10)

def start_screen():
    # display.fill(colors['white'])
    space_invaders(display)
    pygame.display.update()

start_screen()
