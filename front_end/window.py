####

import pygame
import random


####


class SnakeWindow(object):

    def __init__(self, height=600, fps=42):
        """
        Initialize pygame, window, background, font and etc.

        :param width:
        :param height:
        :param fps:
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width      = 3 * height // 2
        self.height     = height
        self.screen     = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((128, 128, 128))

        self.clock    = pygame.time.Clock()
        self.fps      = fps
        self.playtime = 0.0
        self.font     = pygame.font.SysFont('mono', 20, bold=True)

        self.color1 = 0
        self.color2 = 0

    def draw_background(self):
        xpos = self.width // 3
        ypos = 0
        xsize = self.height
        ysize = self.height
        BG = BackGround(xpos, ypos, xsize, ysize)
        BG.draw_lines(self.background)

    def run(self):
        """
        The mainloop

        """
        # self.paint()
        self.draw_background()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.draw_tech_info()
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def draw_tech_info(self):
        milliseconds = self.clock.tick(self.fps)
        self.playtime += milliseconds / 1000.0

        fw, fh = self.font.size("AAA")
        self.draw_text("PLAYTIME: {:^10.3f} seconds".format(self.playtime))
        self.draw_text("FPS: {:6.3}".format(self.clock.get_fps()), (0, fh))

    def draw_text(self, text, position=(0, 0)):
        """
        Center text in the window

        :param text:
        :param position: it is a tuple where will be placed the top left corner of the label.
        """
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, position)


class BackGround(object):

    def __init__(self, x_pos, y_pos, x_size, y_size, x_pace=20, y_pace=20, colour=(0, 30, 30)):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_size = x_size
        self.y_size = y_size
        self.x_pace = x_pace
        self.y_pace = y_pace
        self.colour = colour

        self.surface = pygame.Surface((self.x_size, self.y_size))

    def draw_lines(self, background):

        for i in range(self.x_pace, self.x_size, self.x_pace):
            pygame.draw.line(self.surface, self.colour, (i, 0), (i, self.x_size))
            pygame.draw.line(self.surface, self.colour, (0, i), (self.y_size, i))

        self.surface = self.surface.convert()
        background.blit(self.surface, (self.x_pos, self.y_pos))


def main():
    SnakeWindow().run()


if __name__ == "__main__":
    main()
