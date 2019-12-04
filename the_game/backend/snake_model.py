class Playground(object):
    def __init__(self, size):
        self.size = size


class Direction:
    up = (-1, 0)
    dn = (1, 0)
    lt = (0, -1)
    rt = (0, 1)
    Direction = {'up': up, 'dn': dn, 'lt': lt, 'rt': rt}

    def __init__(self, dir='up'):
        self.dir = Direction.Direction[dir]

    def __add__(self, other):
        return self.dir[0] + other.dir[0], self.dir[1] + other.dir[1]

    def is_zero(self):
        return self.dir[0] == 0 and self.dir[1] == 0


class Position:
    def __init__(self, origin=(0, 0)):
        self.pos = origin

    def __add__(self, other):  # TODO: other argument always must be a Direction object
        y = self.pos[0] + other.dir[0]
        x = self.pos[1] + other.dir[1]
        return Position(origin=(y, x))


class Snake(object):

    def __init__(self, position=(0, 0)):
        self.position = Position(position)
        self.speed = Direction()

    def get_speed(self):
        return self.speed.dir

    def turn(self, new_dir):
        new_speed = self.speed + Direction(dir=new_dir)
        if any(new_speed) != 0:
            self.speed = Direction(dir=new_dir)

    def get_position(self):
        return self.position.pos

    def move(self):
        self.position = self.position + self.speed

