import pygame
from front_end.playground import snake


class BackGround(object):

    def __init__(self, main_screen, width, height):
        self.width = (width // 3) * 2
        self.height = height

        self.x_pos = width // 3
        self.y_pos = 0

        self.pace = 20
        self.psize = height // 20
        self.colour = (20, 80, 200)

        self.window_screen = main_screen
        self.surface = pygame.Surface((self.width, self.height))

        self.background = pygame.Surface(self.surface.get_size()).convert()
        self.background.fill((0, 0, 0))

    def draw_lines(self):

        print("Size of the playground: ", self.psize)
        for i in range(self.pace, self.width, self.pace):
            pygame.draw.line(self.surface, self.colour, (i, 0), (i, self.width))
            pygame.draw.line(self.surface, self.colour, (0, i), (self.width, i))

        self.surface = self.surface.convert()
        self.window_screen.blit(self.surface, (self.x_pos, self.y_pos))


class Cell(object):

    def __init__(self, position, psize=20):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.psize = psize


class PlayGround(object):

    def __init__(self, background, width, height, pace):
        self.x_pos = width // 3
        self.y_pos = 0
        self.size = height
        self.pace = pace
        self.surface = pygame.Surface((self.size, self.size))

        self.bg = BackGround(self.x_pos, self.y_pos, self.size, self.pace)
        # self.snake = snake.Snake(start)

    def draw_background(self):
        return bg.draw_lines(self.background)

    def draw(self, background):
        head_pos = self.snake.get_head_pos()
        left = self.csize * head_pos.pos_x
        top  = self.csize * head_pos.pos_y

        pygame.draw.rect(self.surface, self.snake.get_colour(),
                         (left, left, self.csize, self.csize))

        self.surface = self.surface.convert()
        background.blit(self.surface, (self.len * self.csize/2, 0))


