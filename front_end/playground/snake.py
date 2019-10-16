from front_end.playground import playground


class Snake(object):
    body = []

    def __init__(self, position=(0, 0), colour=(0, 255, 0)):
        self.speed_x = 0
        self.speed_y = 0

        self.head = playground.Cell(position)
        self.body.append(self.head)

        self.turns = {}

        self.colour = colour
        self.pos = position

    def get_colour(self):
        return self.colour

    def get_head_pos(self):
        return self.head

