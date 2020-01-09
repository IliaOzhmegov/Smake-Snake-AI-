from random import randint
import random


class Playground(object):
    size = (20, 20)
    rows = size[0]
    cols = size[1]
    length = rows * cols

    def __init__(self, size=size):
        self.dim = size
        self.borders = [(-1, i) for i in range(self.dim[1])]        # top
        self.borders += [(size[0], i) for i in range(self.dim[1])]  # bottom
        self.borders += [(i, -1) for i in range(self.dim[0])]       # left
        self.borders += [(i, size[0]) for i in range(self.dim[0])]  # right

    def convert_index(self, ind):
        rows = ind // self.dim[0]
        cols = ind % self.dim[1]
        return rows, cols

    def get_index(self, pos):
        rows = pos[0]
        cols = pos[1]
        return rows * self.cols + cols


class Food:
    def __init__(self):
        self.position = Position((0, 0))
        self.rows = Playground.size[0]
        self.cols = Playground.size[1]

    def change_pos(self, snake_body):
        n = Playground.size[0]
        m = Playground.size[1]

        choices_set = []
        [[choices_set.append((i, j)) for j in range(m)] for i in range(n)]
        snake_set = [seg.get_pos() for seg in snake_body]
        [choices_set.remove(seg) for seg in snake_set]

        self.position = Position(random.choice(choices_set))

    def get_pos(self):
        return self.position.pos


class Direction:
    up = (-1, 0)
    dn = (1, 0)
    lt = (0, -1)
    rt = (0, 1)
    get_direction = {'up': up, 'dn': dn, 'lt': lt, 'rt': rt}

    def __init__(self, direc='up'):
        self.dir = Direction.get_direction[direc]

    def __add__(self, other):
        return self.dir[0] + other.dir[0], self.dir[1] + other.dir[1]

    def get_dir(self):
        return self.dir

    def is_zero(self):
        return self.dir[0] == 0 and self.dir[1] == 0


class Position:
    def __init__(self, origin=(0, 0)):
        self.pos = origin

    def __add__(self, other):
        y = self.pos[0] + other.pos[0]
        x = self.pos[1] + other.pos[1]
        return Position(origin=(y, x))

    def __sub__(self, other):
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

    def __init__(self, length=4, position=Playground.size):
        self.__position = Position(position) / 2
        self.__speed = Direction()

        self.__length = length
        self.__body = [self.__position + Position((i, 0)) for i in range(self.__length)]

        self.__pg = Playground()
        self.__borders = self.__pg.borders
        self.__food = Food()
        self.__food.change_pos(self.get_body())

    def __change_food_pos(self):
        self.__food.change_pos(self.get_body())

    def __move_body(self):  # TODO: it must be a private method
        self.__body.insert(0, self.__position)

        if self.__position.get_pos() == self.__food.get_pos():
            self.__change_food_pos()
            return

        self.__body.pop()

    def __is_injuring_itself(self, new_position):
        segments = [segment.pos for segment in self.__body]
        if new_position.get_pos() in segments:
            return True
        return False

    def __is_colliding_wall(self, new_position):
        if new_position.get_pos() in self.__borders:
            return True
        return False

    def get_body(self):
        return self.__body

    def get_body_list(self):
        return [segment.get_pos() for segment in self.get_body()]

    def get_speed(self):
        return self.__speed.dir

    def get_position(self):
        return self.__position.pos

    def get_allowed_space(self):
        return self.__pg.rows, self.__pg.rows

    def get_seen_food_pos(self):
        return self.__food.get_pos()

    def turn(self, new_dir):
        new_speed = self.__speed + Direction(direc=new_dir)
        if any(new_speed) != 0:
            self.__speed = Direction(direc=new_dir)

    def move(self):
        new_position = self.__position + Position(self.__speed.get_dir())

        if self.__is_injuring_itself(new_position):
            return Snake.self_collision

        if self.__is_colliding_wall(new_position):
            return Snake.wall_collision

        self.__position = new_position
        self.__move_body()

    def cli(self):
        command = input("Input your command (h/j/k/l) or (q for quitting):")

        if command == "h":
            self.turn("lt")
        elif command == "j":
            self.turn("dn")
        elif command == "k":
            self.turn("up")
        elif command == "l":
            self.turn("rt")
        elif command == "q":
            return False
        else:
            # for the future
            pass
        return True


