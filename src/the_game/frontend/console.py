from src.the_game.frontend.console_display_utils import Colors
from src.the_game.frontend.console_display_utils import coloured_bordered
from src.the_game.backend import snake_model
from time import sleep
import re

EMPTY_LINE = "                                                           \n"
TURNS = {'h': "lt", 'j': "dn", 'k': "up", 'l': "rt"}

snake = snake_model.Snake()
WIDTH, HEIGHT = snake.get_allowed_space()

class Command:
    def __init__(self):
        self.__commands = []

    def get_command(self):
        if len(self.__commands) == 0:
            input_ = input(':')
            actions = re.findall(r'(\d*[qhjkl])', input_)
            for action in actions:
                number = int(action[:-1]) if len(action) > 1 else 1
                number = 1 if number == 0 else WIDTH if number > WIDTH else number
                self.__commands.extend([action[-1] for _ in range(number)])
            if len(actions) == 0: return None
        command = self.__commands[0]
        self.__commands.pop(0)
        sleep(0.5)
        return command

The_command = Command()

coloured_bordered(4*EMPTY_LINE +
                  "                         Snake Game                        \n"
                  "                         Press ENTER                       \n" +
                  7*EMPTY_LINE +
                  "                      by Ilia Ozhmegov                     \n"
                  "                           2020                            \n" +
                  4*EMPTY_LINE)
coloured_bordered(5*EMPTY_LINE +
                  "                          Manual                           \n"
                  "                         q - quit                          \n" +
                  EMPTY_LINE +
                  "                         h - left                          \n"
                  "                         l - right                         \n"
                  "                         k - up                            \n"
                  "                         j - down                          \n" +
                  2*EMPTY_LINE +
                  "                    Press ENTER to play                    \n" +
                  4*EMPTY_LINE)


def render_snake(snake_body_, food_):
    block_colour = Colors.bg.lightgrey
    snake_colour = Colors.bg.green
    food_colour  = Colors.bg.red
    reset = Colors.reset

    block = '   '
    empty_block = block_colour + block + reset

    content = [[empty_block for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for item in snake_body_:
        i, j = item[0], item[1]
        content[i][j] = snake_colour + block + reset
    i, j = food[0], food[1]
    content[i][j] = food_colour + block + reset

    content = '\n'.join([''.join(item) for item in content])
    Colors.clear()
    print(content)


def command_hanlder(command):
    if command in TURNS:
        dir = TURNS[command]
        snake.turn(dir)
    elif command == 'q':
        return False
    return True




continue_ = True
while continue_:
    snake_body = snake.get_body_list()
    food = snake.get_seen_food_pos()
    render_snake(snake_body, food)

    continue_ = command_hanlder(The_command.get_command())
    snake.move()

