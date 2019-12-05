####

import pygame
import random

from front_end.infoground import infoground
from front_end.playground import playground


####


class Window(object):

    def __init__(self, height=600, fps=42):
        """
        Initialize pygame, window, background, font and etc.

        :param width:
        :param height:
        :param fps:
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width  = 3 * height // 2
        self.height = height

        self.screen     = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((128, 128, 200))

        self.info_ground = infoground.InfoGround(self.screen,
                                                 self.width,
                                                 self.height, fps)
        self.play_ground = playground.PlayGround(self.screen,
                                                 self.width,
                                                 self.height)

    def run(self):
        """
        The mainloop

        """

        self.play_ground.draw_background()

        dfoo_x = 0
        dfoo_y = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_h:
                        dfoo_x = -3
                        dfoo_y = 0
                    elif event.key == pygame.K_j:
                        dfoo_x = 0
                        dfoo_y = 3
                    elif event.key == pygame.K_k:
                        dfoo_x = 0
                        dfoo_y = -3
                    elif event.key == pygame.K_l:
                        dfoo_x = 3
                        dfoo_y = 0

            self.info_ground.draw_tech_info()
            self.play_ground.foreground.change_foo((dfoo_x, dfoo_y))
            self.play_ground.draw_foo()
            pygame.display.flip()

        pygame.quit()


def main():
    Window().run()


if __name__ == "__main__":
    main()
