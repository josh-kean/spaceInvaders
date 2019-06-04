import pygame
from invaders import Invaders
from player import Player


pygame.init()

width = 1000
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

def move_player(event):
    playerSpeed = 20
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return -playerSpeed
        if event.key == pygame.K_RIGHT:
            return playerSpeed
    if event.type == pygame.KEYUP:
        return 0

def space_invaders(display):
    # invaderOne = invaders(display)
    event = pygame.event.poll()
    invaders = create_invaders(display)
    player = Player(display, [int(width/2), height-50])
    #attacked willl be true if the invader collides with the player
    attacked = False
    event = pygame.event.poll()
    #sets the speed of the space invader
    invaderSpeed = 2
    moveInvaderX = invaderSpeed
    moveInvaderY = 0

    movePlayer = 0
    while attacked == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                movePlayer = move_player(event)

        display.fill(colors['black'])
        invaderPositionsX = [invader.position[0] for invader in invaders]
        invaderPositionsY = [invader.position[1] for invader in invaders]
        if min(invaderPositionsX) == 0:
            moveInvaderX = invaderSpeed
            moveInvaderY = invaderSpeed
        if max(invaderPositionsX) >= width-50:
            moveInvaderX = -invaderSpeed
            moveInvaderY = invaderSpeed

        player.position[0] += movePlayer
        player.draw_player()

        for invader in invaders:
            invader.position[0] += moveInvaderX
            invader.position[1] += moveInvaderY
            invader.draw_invader()
        moveInvaderY = 0
        if player.position[0] < player.width or player.position[0] > width-player.width-10:
            movePlayer = 0
        pygame.display.update()
        clock.tick(60)

def start_screen():
    # display.fill(colors['white'])
    space_invaders(display)
    pygame.display.update()

start_screen()
