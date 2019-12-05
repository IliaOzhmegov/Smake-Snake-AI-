import pygame
import random
from front_end.playground import snake


class PlayGround(object):

    def __init__(self, main_screen, width, height):
        self.width = (width // 3) * 2
        self.height = height

        self.x_pos = width // 3
        self.y_pos = 0

        self.pace = 20
        self.psize = height // 20

        self.window_screen = main_screen

        self.background = BackGround(self.window_screen,
                                     self.width, self.height,
                                     self.x_pos, self.y_pos,
                                     self.pace)
        self.foreground = ForeGround(self.window_screen,
                                     self.width, self.height,
                                     self.x_pos, self.y_pos,
                                     self.pace)

    def draw_background(self):
        self.background.draw_lines()

    def draw_foo(self):
        self.foreground.draw_foo()


    # def draw(self, background):
    #     head_pos = self.snake.get_head_pos()
    #     left = self.csize * head_pos.pos_x
    #     top  = self.csize * head_pos.pos_y
    #
    #     pygame.draw.rect(self.surface, self.snake.get_colour(),
    #                      (left, left, self.csize, self.csize))
    #
    #     self.surface = self.surface.convert()
    #     background.blit(self.surface, (self.len * self.csize/2, 0))


class BackGround(object):

    def __init__(self, main_screen, width, height, x_pos, y_pos, pace):
        self.width  = width
        self.height = height

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.pace = pace
        self.psize = height // self.pace
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


class ForeGround(object):

    def __init__(self, main_screen, width, height, x_pos, y_pos, pace):
        self.width  = width
        self.height = height

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.pace  = pace
        self.psize = height // self.pace
        self.colour = (20, 200, 80)

        self.window_screen = main_screen
        self.surface = pygame.Surface((self.width, self.height))

        self.foreground = pygame.Surface(self.surface.get_size())
        self.foreground.set_colorkey((0, 0, 0))

        self.foo_x = width // 10
        self.foo_y = height // 10

    def change_foo(self, dfoo):
        self.foo_x += dfoo[0]
        self.foo_y += dfoo[1]

    def draw_foo(self):
        # self.foo_x += 1
        # self.foo_y += 1
        #
        # if self.foo_x > self.width + self.x_pos:
        #     self.foo_x = 0
        #     self.foo_x += random.randint(0, 50)
        # if self.foo_y > self.height + self.y_pos:
        #     self.foo_y = 0
        #     self.foo_y += random.randint(0, 50)

        self.foreground.window_screen.fill(0)
        pygame.draw.circle(self.foreground, self.colour,
                           (self.foo_x, self.foo_y),
                           self.psize // 2)
        self.foreground = self.foreground.convert_alpha()
        self.window_screen.blit(self.foreground,
                                (self.x_pos, self.y_pos))


class Cell(object):

    def __init__(self, position, psize=20):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.psize = psize



