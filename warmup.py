import pygame, sys
from pygame.locals import *
import block


pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
speedx = 5
speedy = 3
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32, 0)
pygame.display.set_caption("Animation")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
WIDTH = 25
HEIGHT = 25

my_block = block.Block(main_window, WIDTH, HEIGHT, BLUE)
my_block.rect.x = 10
my_block.rect.y = 10
main_window.blit(my_block.image, my_block.rect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
    if my_block.rect.top < 0 or my_block.rect.bottom > 500:
        speedy = -speedy
    if my_block.rect.left < 0 or my_block.rect.right > 500:
        speedx = - speedx

    main_window.fill(WHITE)
    my_block.rect.left += speedx
    my_block.rect.top += speedy
    main_window.blit(my_block.image, my_block.rect)
    pygame.display.update()


