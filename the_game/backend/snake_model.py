from random import randint


class Playground(object):
    Size = (20, 20)
    Rows = Size[0]
    Cols = Size[1]
    Length = Rows * Cols

    def __init__(self, size=Size):
        self.size = size
        self.borders = [(-1, i) for i in range(self.size[1])]        # top
        self.borders += [(size[0], i) for i in range(self.size[1])]  # bottom
        self.borders += [(i, -1) for i in range(self.size[0])]       # left
        self.borders += [(i, size[0]) for i in range(self.size[0])]  # right

    def convert_index(self, ind):  # TODO: ind starts with 0
        rows = ind // self.size[0]
        cols = ind % self.size[1]
        return rows, cols

    def get_index(self, pos):
        rows = pos[0]
        cols = pos[1]
        return rows*self.Cols + cols


class Food:
    def __init__(self):
        self.position = Position((0, 0))
        self.rows = Playground.Size[0]
        self.cols = Playground.Size[1]

    def change_pos(self, snake_body, pg):
        set_choices = list(range(Playground.Length))
        set_snake = [Playground.get_index(pg, i.get_pos()) for i in snake_body]
        for segment in set_snake:
            set_choices.remove(segment)

        r_index = randint(0, len(set_choices))
        self.position = Position(Playground.convert_index(pg, r_index))

    def get_pos(self):
        return self.position.pos


class Direction:
    up = (-1, 0)
    dn = (1, 0)
    lt = (0, -1)
    rt = (0, 1)
    Direction = {'up': up, 'dn': dn, 'lt': lt, 'rt': rt}

    def __init__(self, direc='up'):
        self.dir = Direction.Direction[direc]

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

    def __truediv__(self, other: int):
        y = self.pos[0] // other
        x = self.pos[1] // other
        return Position(origin=(y, x))

    def get_pos(self):
        return self.pos


class Snake(object):
    self_collision = "Injuring itself"
    wall_collision = "Wall collision"

    def __init__(self, length=4, position=Playground.Size):
        self.position = Position(position) / 2
        self.speed = Direction()

        self.length = length
        self.body = [self.position + Position((i, 0)) for i in range(self.length)]

        self.pg = Playground()
        self.borders = self.pg.borders
        self.food = Food()

    def __change_food_pos(self):
        self.food.change_pos(self.get_body(), self.pg)

    def get_body(self):
        return self.body

    def __move_body(self):  # TODO: it must be a private method
        self.body.insert(0, self.position)

        if self.position.get_pos() == self.food.get_pos():
            self.__change_food_pos()
            return

        self.body.pop()

    def __is_injuring_itself(self, new_position):
        segments = [segment.pos for segment in self.body]
        if new_position.get_pos() in segments:
            return True
        return False

    def __is_colliding_wall(self, new_position):
        if new_position.get_pos() in self.borders:
            return True
        return False

    def get_speed(self):
        return self.speed.dir

    def turn(self, new_dir):
        new_speed = self.speed + Direction(direc=new_dir)
        if any(new_speed) != 0:
            self.speed = Direction(direc=new_dir)

    def get_position(self):
        return self.position.pos

    def move(self):
        new_position = self.position + Position(self.speed.get_dir())

        if self.__is_injuring_itself(new_position):
            return Snake.self_collision

        if self.__is_colliding_wall(new_position):
            return Snake.wall_collision

        self.position = new_position
        self.__move_body()



