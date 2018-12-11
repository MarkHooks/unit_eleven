import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        self.RADIUS = 10
        RED = (255, 0, 0)
        self.image = pygame.mainSurface((self.RADIUS * 2, self.RADIUS *2))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.RED, (25, 25), self.RADIUS, 0)
        self.speedx = 5
        self.speedy = 3

    def move(self):
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        if self.rect.top < 0 or self.rect.bottom > 500:
            self.speedy = -self.speedy
        if self.rect.left < 0 or self.rect.right > 500:
            self.speedx = - self.speedx
