def number(the_number, arg):
    return arg[0](the_number, arg[1]) if arg else the_number


def zero (arg = None): return number(0, arg)
def one  (arg = None): return number(1, arg)
def two  (arg = None): return number(2, arg)
def three(arg = None): return number(3, arg)
def four (arg = None): return number(4, arg)
def five (arg = None): return number(5, arg)
def six  (arg = None): return number(6, arg)
def seven(arg = None): return number(7, arg)
def eight(arg = None): return number(8, arg)
def nine (arg = None): return number(9, arg)


def plus      (value): return int.__add__, value
def minus     (value): return int.__sub__, value
def times     (value): return int.__mul__, value
def divided_by(value): return int.__floordiv__, value


assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3


def quad(a, b, c):
    return lambda x: (a(x) if callable(a) else a)*(x ** 2) + \
                     (b(x) if callable(b) else b) * x + \
                     (a(x) if callable(c) else c)


assert quad(0, 0, 3)(0) == 3
assert quad(quad(1, 0, 0), quad(0, 2, 0), 3)(0) == 3