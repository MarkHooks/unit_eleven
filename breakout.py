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
    REDER = (200, 0, 0)
    BLUE = (0, 0, 255)
    lose = pygame.image.load("skull copy.png")

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    pygame.init()
    main_window = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    pygame.display.set_caption("Breakout")
    bg = pygame.image.load("ocean.png")
    xpos = 0
    ypos = BRICK_Y_OFFSET

    my_paddle = paddle.Paddle(main_window, RED, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_group.add(my_paddle)
    my_paddle.rect.x = APPLICATION_WIDTH/2
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET

    my_ball = ball.Ball(REDER, ball_width, ball_height, RADIUS_OF_BALL)
    my_ball.rect.x = 200
    my_ball.rect.y = 200

    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]

    for color in colors:
        for x in range(2):
            for y in range(10):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
                brick_group.add(my_brick)
                my_brick.rect.x = xpos
                my_brick.rect.y = ypos
                xpos += (BRICK_SEP + BRICK_WIDTH)
            xpos = 0
            ypos += BRICK_SEP + BRICK_HEIGHT
    while True:
        mousefont = pygame.font.SysFont("Helvetica", 30)
        mouselable = mousefont.render(str(NUM_TURNS), 80, (255, 255, 255))
        main_window.blit(mouselable, (350, 30))
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                my_paddle.move(pygame.mouse.get_pos())
        if my_ball.rect.bottom > 590:
            my_ball.rect.x = 200
            my_ball.rect.y = 200
            NUM_TURNS -= 1
            print(NUM_TURNS)
        main_window.blit(bg,(0,0))
        #main_window.fill(BLUE)
        if len(brick_group) == 0:
            mousefont = pygame.font.SysFont("Helvetica", 30)
            mouselable = mousefont.render("You Win", 1, (0, 255, 0))
            main_window.blit(mouselable, (30, 30))
            pygame.display.update()
            pygame.time.wait(1000)
        if NUM_TURNS == 1 and my_ball.rect.bottom > 580:
            #mousefont = pygame.font.SysFont("Helvetica", 30)
            #mouselable = mousefont.render("You Lose", 1, (255, 0, 0))
            main_window.blit(lose, (75, 250))
            pygame.display.update()
        if NUM_TURNS == 0:
            pygame.time.wait(100000)
        my_ball.move(NUM_TURNS)
        my_ball.colide(paddle_group, brick_group)
        main_window.blit(my_ball.image, my_ball.rect)

        for a_brick in brick_group:
            main_window.blit(a_brick.image, a_brick.rect)

        main_window.blit(my_paddle.image, my_paddle.rect)

        pygame.display.update()



main()
