import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.width = width
        self.color = color
        self.height = height
        # Create a surface with the correct height and width
        self.image = pygame.image.load("wood2.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

