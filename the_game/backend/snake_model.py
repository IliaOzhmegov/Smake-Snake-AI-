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

    def get_dir(self):
        return self.dir

    def is_zero(self):
        return self.dir[0] == 0 and self.dir[1] == 0


class Position:
    def __init__(self, origin=(0, 0)):
        self.pos = origin

    def __add__(self, other):  # TODO: other argument always must be a Position object
        y = self.pos[0] + other.pos[0]
        x = self.pos[1] + other.pos[1]
        return Position(origin=(y, x))

    def __sub__(self, other):  # TODO: other argument always must be a Position object
        y = self.pos[0] - other.pos[0]
        x = self.pos[1] - other.pos[1]
        return Position(origin=(y, x))

    def get_pos(self):
        return self.pos


class Snake(object):

    def __init__(self, position=(0, 0)):
        self.position = Position(position)
        self.speed = Direction()
        self.length = 4

        self.body = [self.position + Position((i, 0)) for i in range(self.length)]

    def get_body(self):
        return self.body

    def __move_body(self):  # TODO: it must be a private method
        self.body.pop()
        self.body.insert(0, self.position)

    def get_speed(self):
        return self.speed.dir

    def turn(self, new_dir):
        new_speed = self.speed + Direction(dir=new_dir)
        if any(new_speed) != 0:
            self.speed = Direction(dir=new_dir)

    def get_position(self):
        return self.position.pos

    def move(self):
        self.position = self.position + Position(self.speed.get_dir())
        self.__move_body()


