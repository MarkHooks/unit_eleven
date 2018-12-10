import pygame
import sys
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        self.RADIUS = 10

    def move(self):
        block = pygame.Surface((50, 50))
        rect = block.get_rect()
        pygame.draw.rect(block, self.WHITE, (0, 0, 50, 50), 0)
        pygame.draw.circle(block, self.RED, (25, 25), 25, 0)
        speedx = 5
        speedy = 3

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                mainSurface.fill(self.WHITE)
                rect.top += speedy
                rect.left += speedx
                if rect.top < 0 or rect.bottom > 500:
                    speedy = -speedy
                if rect.left < 0 or rect.right > 500:
                    speedx = -speedx

                mainSurface.blit(block, rect)

                pygame.display.update()

