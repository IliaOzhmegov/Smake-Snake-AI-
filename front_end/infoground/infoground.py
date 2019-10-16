
import pygame


class InfoGround(object):

    def __init__(self, main_screen, width, height, fps):
        self.width  = width // 3
        self.height = height

        self.clock    = pygame.time.Clock()
        self.fps      = fps
        self.playtime = 0.0

        self.window_screen = main_screen
        self.surface = pygame.Surface((self.width, self.height))
        self.font    = pygame.font.SysFont('mono', 20, bold=True)

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
        self.window_screen.blit(surface, position)




