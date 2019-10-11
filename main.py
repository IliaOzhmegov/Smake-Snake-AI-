####

import pygame


####


class PGView(object):


    def __init__(self, width = 640, height = 480, fps = 30):
        """
        Initialize pygame, window, background, font and etc.

        :param width:
        :param height:
        :param fps:
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width      = width
        self.height     = height
        self.screen     = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()

        self.clock    = pygame.time.Clock()
        self.fps      = fps
        self.playtime = 0.0
        self.font     = pygame.font.SysFont('mono', 20, bold=True)

    def run(self):
        """
        The mainloop

        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0;

            fw, fh = self.font.size("AAA")
            self.draw_text("PLAYTIME: {:>6.3} seconds".format(self.playtime))
            self.draw_text("FPS: {:6.3}".format(self.clock.get_fps()), (0, fh))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def draw_text(self, text, position=(0, 0)):
        """
        Center text in the window

        :param text:
        :param position: it is a tuple where will be placed the top left corner of the label.
        """
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, position)


def main():
    PGView(600, 400).run()


if __name__ == "__main__":
    main()
