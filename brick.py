import pygame
class Brick(pygame.sprite.Sprite):

    def __init__(self, width, color):
        self.BRICK_HEIGHT = 8
    def draw_brick(self, x_pos, y_pos):
        pygame.draw.rect(self.mainSurface, color, (x_pos, y_pos, self.BRICK_WIDTH, self.BRICK_HEIGHT), 0)