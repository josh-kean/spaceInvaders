import pygame

class Player:
    def __init__(self, display, position):
        self.display = display
        self.width = 50
        self.height = 25
        self.position = position
        self.colors = {'white': (255, 255, 255), 'black': (0,0,0)}

    def draw_player(self):
        pygame.draw.rect(self.display, self.colors['black'], (self.position[0], self.position[1], self.width, self.height))
