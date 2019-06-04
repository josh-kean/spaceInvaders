#this class is for the space-invaders
import pygame


class Invaders:
    def __init__(self,  display, position=[100,100]):
        self.display = display
        self.position = position
        self.height = 40
        self.width = self.height
        self.colors = {'white': (255, 255, 255), 'black': (0,0,0), 'grey': (160, 160, 160)}
    #this will draw an invader onto the screen, you could load an image instead
    def draw_invader(self):
        pygame.draw.rect(self.display, self.colors['grey'], (self.position[0], self.position[1], self.height, self.width))
