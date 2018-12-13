import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.color = color
        self.radius = radius
        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((self.radius * 2, self.radius *2))
        self.rect = self.image.get_rect()
        # pygame.draw.circle(self.image, self.color, (25, 25), self.radius, 0)
        self.speedx = 5
        self.speedy = 3
        # Add a circle to represent the ball to the surface just created.

    def move(self):
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        if self.rect.top < 0 or self.rect.bottom > 500:
            self.speedy = -self.speedy
        if self.rect.left < 0 or self.rect.right > 500:
            self.speedx = - self.speedx

