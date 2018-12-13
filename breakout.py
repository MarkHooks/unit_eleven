import pygame, sys
import ball
import brick
import paddle
from pygame.locals import *


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3
    ball_width = RADIUS_OF_BALL * 2
    ball_height = RADIUS_OF_BALL * 2
    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    pygame.init()
    main_window = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    pygame.display.set_caption("Breakout")

    xpos = 0
    ypos = BRICK_Y_OFFSET
    for x in range(10):
        colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
        for color in colors:
            brick_color = color
            my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, brick_color)
            my_brick.rect.x = xpos
            my_brick.rect.y = ypos

            main_window.blit(my_brick.image, my_brick.rect)
        #ypos += BRICK_Y_OFFSET + BRICK_HEIGHT
        xpos += BRICK_SEP + BRICK_WIDTH

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        #main_window.fill(WHITE)
        #  my_ball = ball.Ball(RED, ball_width, ball_height, RADIUS_OF_BALL)
        # main_window.blit(my_ball.image, my_ball.rect)
        # if my_ball.rect.top < 0 or my_ball.rect.bottom > 500:
        #     speedy = - speedy
        # if my_ball.rect.left < 0 or my_ball.rect.right > 500:
        #     speedx = - speedx
        # main_window.blit(my_ball.image, my_ball.rect)

        # my_paddle = paddle.Paddle(main_window, WHITE, PADDLE_WIDTH, PADDLE_HEIGHT)
        # main_window.blit(my_paddle.image, my_paddle.rect)



        pygame.display.update()


main()
