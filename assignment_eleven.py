import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    mainSurface = pygame.Surface((50,50))
    pygame.display.set_caption("Break out")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    block = pygame.Surface((50,50))
    ball = block.get_rect()
    block.fill(BLACK)
    speedx = 5
    speedy = 5

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mainSurface.fill(WHITE)
            ball.top += speedy
            ball.left += speedx
            if ball.top <0 or ball.bottom >500:
                speedy = -speedy
            if ball.left <0 or ball.right > 500:
                speedx = -speedx
            mainSurface.blit(block, ball)
            pygame.display.update()