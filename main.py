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
        self.background.fill((128, 128, 128))

        self.clock    = pygame.time.Clock()
        self.fps      = fps
        self.playtime = 0.0
        self.font     = pygame.font.SysFont('mono', 20, bold=True)

    def paint(self):
        pygame.draw.circle(self.background, (255, 128, 55), (200, 200), 100, 10)
        pygame.draw.polygon(self.background, (0, 200, 200),
                            ((100, 100), (200, 100),
                             (120, 200), (150, 50), (180, 200)), 3)
        pygame.draw.arc(self.background, (0, 50, 200), (0, 0, self.width, self.height), -3.14/4, 3.14/4 * 3)

        for point in range(0, self.width, 64):  # range(start, stop, step)
            pygame.draw.line(self.background, (255, 0, point/self.width * 255), (0, 0), (480, point), 1)

        myball = Ball()
        myball.blit(self.background)


    def run(self):
        """
        The mainloop

        """
        self.paint()
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
            self.draw_text("PLAYTIME: {:^10.3f} seconds".format(self.playtime))
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


class Ball(object):

    def __init__(self, radius=50, colour=(0, 0, 255), x=320, y=240):
        self.radius = radius
        self.color  = colour
        self.x = x
        self.y = y

        self.surface = pygame.Surface((2 * self.radius, 2 * self.radius))
        self.surface.set_colorkey((0,0,0))         # make black the transparent color (red,green,blue)
        pygame.draw.circle(self.surface, colour, (radius, radius), radius)
        self.radius = self.surface.convert_alpha()

    def blit(self, background):
        background.blit(self.surface, (self.x, self.y))


def main():
    PGView(600, 400).run()


if __name__ == "__main__":
    main()
