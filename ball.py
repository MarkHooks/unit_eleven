import pygame
import sys
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.color = color
        self.radius = radius
        self.window_width = windowWidth
        self.window_height = windowHeight
        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.image.load("cannon ball copy1.png")
        self.rect = self.image.get_rect()
        # pygame.draw.circle(self.image, self.color, (25, 25), self.radius, 0)
        self.speedx = 7
        self.speedy = 7
        # Add a circle to represent the ball to the surface just created.
        #pygame.draw.circle(self.image, color, (radius, radius), radius, 0)

    def move(self, num_turns):
        num_turns = 3
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.left < 0 or self.rect.right > 400:
            self.speedx = - self.speedx

    def colide(self, paddle_group, brick_group):
        if pygame.sprite.spritecollide(self, brick_group, True):
            self.speedx = self.speedx
            self.speedy = - self.speedy
        if pygame.sprite.spritecollide(self, paddle_group, False):
            self.speedx = self.speedx
            self.speedy = - self.speedy

