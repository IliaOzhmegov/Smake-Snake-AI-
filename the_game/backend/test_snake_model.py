import pytest
from unittest import TestCase
from .snake_model import Snake


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

