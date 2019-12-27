from unittest import TestCase
import unittest

from the_game.backend.snake_model import Snake
from the_game.backend.snake_model import Position
from the_game.backend.snake_model import Playground
from the_game.backend.snake_model import Food


class TestGeneric(TestCase):
    def test_list_behaviour(self):
        my_list = []
        [[my_list.append((j, i)) for i in range(20)] for j in range(20)]
        my_body = [(i, 3) for i in range(10)]

        list_size = len(my_list)
        body_size = len(my_body)

        for segment in my_body:
            if segment in my_list:
                my_list.remove(segment)

        assert len(my_list) == list_size - body_size


class TestSnake(TestCase):
    def test_init(self):
        s = Snake()
        assert s.position.pos == (Playground.size[0] / 2, Playground.size[1] / 2)

    def test_get_speed_and_turn(self):
        s = Snake()
        assert s.get_speed() == (-1, 0)

        s.turn('lt')
        assert s.get_speed() == (0, -1)  # lt

        s.turn('lt')
        s.turn('rt')
        assert s.get_speed() == (0, -1)

        s.turn('dn')
        assert s.get_speed() == (1, 0)

        s.turn('up')
        assert s.get_speed() == (1, 0)

        s.turn('rt')
        assert s.get_speed() == (0, 1)

        s.turn('up')
        assert s.get_speed() == (-1, 0)

        s.turn('up')
        assert s.get_speed() == (-1, 0)

        s.turn('lt')
        assert s.get_speed() == (0, -1)

    def test_move(self):
        s = Snake()

        x_shift = Playground.size[1] // 2

        def move_n_cells(n, dest_x, dest_y):
            [s.move() for _ in range(1, n)]

            assert s.get_position() == (dest_y, dest_x)

        n = 100

        s.turn('up')
        move_n_cells(n, x_shift, 0)

        s.turn('rt')
        move_n_cells(n, Playground.size[0] - 1, 0)

        s.turn('dn')
        move_n_cells(n, Playground.size[0] - 1, Playground.size[0] - 1)

        s.turn('lt')
        move_n_cells(n, 0, Playground.size[0] - 1)

    def test_get_body(self):
        s = Snake()

        x_shift = Playground.size[1] // 2
        y_shift = Playground.size[0] // 2

        def move_snake_by_straight(n, dest_x, dest_y, direction=(-1, 0), print_flag=False):
            for i in range(1, n+1):
                s.move()
                # print_body(s)

            assert s.get_position() == (dest_y + y_shift, dest_x + x_shift)

            i = 0
            j = 0
            for segment in s.get_body():
                if print_flag:
                    print(segment.pos, "i: ", i, "j: ", j)
                assert segment.pos == (dest_y - i + y_shift, dest_x - j + y_shift)
                i += direction[0]
                j += direction[1]

        move_snake_by_straight(10, 0, -10)

        s.turn('lt')
        move_snake_by_straight(10, -10, -10, direction=(0, -1))

        s.turn('dn')
        move_snake_by_straight(10, -10, 0, direction=(1, 0))

        s.turn('rt')
        move_snake_by_straight(10, 0, 0, direction=(0, 1))


        s2 = Snake()
        s2.move()

        s2.turn('lt')
        [s2.move() for _ in range(2)]

        s2_body = s2.get_body()
        assert s2_body[0].pos == (-1 + y_shift, -2 + x_shift)
        assert s2_body[1].pos == (-1 + y_shift, -1 + x_shift)
        assert s2_body[2].pos == (-1 + y_shift, 0 + x_shift)
        assert s2_body[3].pos == (0 + y_shift, 0 + x_shift)

    def test_self_collision(self):
        s = Snake(length=10)

        x_shift = Playground.size[1] // 2
        y_shift = Playground.size[0] // 2

        def n_moves_to(di, n):
            s.turn(di)
            for i in range(n):
                if s.move() == Snake.self_collision:
                    assert s.position.get_pos() == (2 + y_shift, 1 + x_shift)

        n_moves_to('rt', 2)
        n_moves_to('dn', 2)
        n_moves_to('lt', 5)

    def test_wall_collision(self):
        s = Snake()

        x_shift = Playground.size[1] // 2

        def n_moves_to(di, n):
            s.turn(di)
            for _ in range(n):
                if s.move() == Snake.wall_collision:
                    assert s.position.get_pos() == (0, x_shift)

        n_moves_to('up', 100)

    @unittest.skip("Requires manual driving")
    def test_snake_main(self):
        s = Snake()

        def show_snake():
            print("----- Snake -----")
            for segment in s.get_body():
                print(segment.get_pos())
            print("===== Snake =====")
            print("----- Food -----")
            print(s.food.get_pos())
            print("===== Food =====")

        while(s.cli()):
            s.move()
            show_snake()


class TestPlayground(TestCase):
    def test_init(self):
        p = Playground()
        assert (-1, 0) in p.borders
        assert (-1, 19) in p.borders

        assert (20, 0) in p.borders
        assert (20, 19) in p.borders

        assert (0, -1) in p.borders
        assert (19, -1) in p.borders

        assert (0, 20) in p.borders
        assert (19, 20) in p.borders


class TestFood(TestCase):
    def test_change_pos(self):
        s = Snake()
        f = Food()
        f.change_pos(s.get_body())

        food_pos = f.get_pos()

        assert food_pos[0] < Playground.size[0]
        assert food_pos[1] < Playground.size[1]
        assert food_pos[0] >= 0
        assert food_pos[1] >= 0

    def test_index_funcs(self):
        Food()
        p = Playground()

        point1 = (1, 1)
        index1 = Playground.get_index(p, point1)
        assert index1 == (p.rows + 2) - 1
        assert Playground.convert_index(p, index1) == point1








