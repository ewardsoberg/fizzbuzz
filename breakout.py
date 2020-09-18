import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 100, 180)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BALL_RADIUS = 10

score = 0
lives = 3


class Ball:
    def __init__(self, x_ball, y_ball, x_step, y_step, color_ball, radius, screen):
        self.x = x_ball
        self.y = y_ball
        self.x_step = x_step
        self.y_step = y_step
        self.color = color_ball
        self.radius = radius
        self.screen = screen

    def move_ball(self):
        self.x += self.x_step
        self.y += self.y_step

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HEIGHT - self.radius:
            self.y_step *= -1

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Paddle:
    def __init__(self, x_paddle, y_paddle, color_paddle, width_paddle, height_paddle, screen):
        self.x = x_paddle
        self.y = y_paddle
        self.color = color_paddle
        self.width = width_paddle
        self.height = height_paddle
        self.screen = screen

    def move_left(self, pixels):
        self.x -= pixels
        if self.x < 0:
            self.x = 0

    def move_right(self, pixels):
        self.x += pixels
        if self.x > 770:
            self.x = 770

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))


class Brick:
    def __init__(self, x_brick, y_brick, color_brick, width_brick, height_brick, screen):
        self.x = x_brick
        self.y = y_brick
        self.color = color_brick
        self.width = width_brick
        self.height = height_brick
        self.screen = screen

    def draw_brick(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x_ball = random.randrange(BALL_RADIUS, SCREEN_WIDTH-BALL_RADIUS)
    y_ball = random.randrange(BALL_RADIUS, SCREEN_HEIGHT-BALL_RADIUS)
    x_step = 2
    y_step = 2
    color_ball = RED
    radius = BALL_RADIUS
    red_ball = Ball(x_ball, y_ball, x_step, y_step, color_ball, radius, screen)

    x_paddle = 400
    y_paddle = 560
    color_paddle = WHITE
    width_paddle = 30
    height_paddle = 5
    paddle = Paddle(x_paddle, y_paddle, color_paddle, width_paddle, height_paddle, screen)

    brick1 = []
    for b1 in range(20):
        color_brick = BLUE
        width_brick = 35
        height_brick = 10
        x_brick = 10 + b1 * 39
        y_brick = 5
        b1 = Brick(x_brick, y_brick, color_brick, width_brick, height_brick, screen)
        brick1.append(b1)

    brick2 = []
    for b2 in range(20):
        color_brick = YELLOW
        width_brick = 55
        height_brick = 15
        x_brick = 8 + b2 * 66
        y_brick = 20
        b2 = Brick(x_brick, y_brick, color_brick, width_brick, height_brick, screen)
        brick2.append(b2)

    brick3 = []
    for b3 in range(20):
        color_brick = PINK
        width_brick = 75
        height_brick = 20
        x_brick = 2 + b3 * 80
        y_brick = 40
        b3 = Brick(x_brick, y_brick, color_brick, width_brick, height_brick, screen)
        brick3.append(b3)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left(5)
        if keys[pygame.K_RIGHT]:
            paddle.move_right(5)

        screen.fill(BLACK)
        red_ball.move_ball()
        red_ball.draw_ball()
        paddle.draw_paddle()

        for b1 in brick1:
            b1.draw_brick()
        for b2 in brick2:
            b2.draw_brick()
        for b3 in brick3:
            b3.draw_brick()

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
