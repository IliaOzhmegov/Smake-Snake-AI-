import pygame
import sys
from the_game.backend import snake_model

SCREEN_SIZE = WIDTH, HEIGHT = (600, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Press ESC to quit')
fps = pygame.time.Clock()
paused = False

# Ball setup
ball_pos1 = [50, 50]
ball_pos2 = [50, 240]
ball_pos3 = [50, 430]

# Snake
snake = snake_model.Snake()
scale_coef = WIDTH // snake.pg.Cols

# frames per second
FPS = 30
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()


def update():
    snake.move()

def get_pos_on_screen(snake_pos):
    return snake_pos * scale_coef + scale_coef // 2


def render():
    screen.fill(BLACK)

    snake_body = snake.get_body_list()
    for segment in snake_body:
        x_pos = get_pos_on_screen(segment[1])
        y_pos = get_pos_on_screen(segment[0])
        pygame.draw.rect(screen, GREEN, (x_pos - scale_coef //2, y_pos - scale_coef //2,
                                         scale_coef, scale_coef))

    food = snake.food.get_pos()
    x_pos = get_pos_on_screen(food[1])
    y_pos = get_pos_on_screen(food[0])
    pygame.draw.circle(screen, RED, [x_pos, y_pos], scale_coef // 2, 0)

    pygame.display.update()
    fps.tick(FPS)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_h:
                snake.turn("lt")
            elif event.key == pygame.K_j:
                snake.turn("dn")
            elif event.key == pygame.K_k:
                snake.turn("up")
            elif event.key == pygame.K_l:
                snake.turn("rt")

    dt = clock.tick()
    if not paused:
        time_elapsed_since_last_action += dt
        if time_elapsed_since_last_action > 250:
            update()
            time_elapsed_since_last_action = 0  # reset it to 0 so you can count again
        render()
