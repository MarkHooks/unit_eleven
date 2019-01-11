import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.width = width
        self.height = height
        # Create a surface with the correct height and width
        self.image = pygame.image.load("cannon copy1.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        #self.image.fill(color)

    def move(self, position):
        self.rect.x = position[0]
        if self.rect.right > 400:
            self.rect.x = 350
            pygame.display.update()
