import pytest
from unittest import TestCase
from .snake_model import Snake
from .snake_model import Position


class TestSnake(TestCase):
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

        def move_n_cells(n, dest_x, dest_y):
            for i in range(1, n):
                s.move()

            assert s.get_position() == (dest_y, dest_x)

        n = 100

        s.turn('up')
        move_n_cells(n, 0, -99)

        s.turn('rt')
        move_n_cells(n, 99, -99)

        s.turn('dn')
        move_n_cells(n, 99, 0)

        s.turn('lt')
        move_n_cells(n, 0, 0)

    def test_get_body(self):
        s = Snake()

        def print_body(s):
            print('----------')
            for segment in s.get_body():
                print(segment.pos)
            print('==========')

        def move_snake_by_straight(n, dest_x, dest_y, direction=(-1, 0), print_flag=False):
            for i in range(1, n+1):
                s.move()
                # print_body(s)

            assert s.get_position() == (dest_y, dest_x)

            i = 0
            j = 0
            for segment in s.get_body():
                if print_flag:
                    print(segment.pos, "i: ", i, "j: ", j)
                assert segment.pos == (dest_y - i, dest_x - j)
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
        for i in range(2):
            s2.move()

        s2_body = s2.get_body()
        assert s2_body[0].pos == (-1, -2)
        assert s2_body[1].pos == (-1, -1)
        assert s2_body[2].pos == (-1, 0)
        assert s2_body[3].pos == (0, 0)



        def foo(s):
            s_body = s.get_body()
            i = 0
            for cell in s_body:
                assert cell.pos == (i, 0)
                i += 1

            s.body.insert(0, Position((-1, 0)))
            s.body.pop()
            s.body.append(Position((5, 0)))
            for cell in s.get_body():
                print(cell.pos)






