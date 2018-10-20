def print_twice(bruce):
    print(bruce)
    print(bruce)


# PEP 8
def do_twice(f, value):
    f(value)
    f(value)


def do_four(g, four_value):
    do_twice(g, four_value)
    do_twice(g, four_value)


do_four(print_twice, 'spam')