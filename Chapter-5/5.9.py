# import math


def do_n(t, n):
    if n > 0:
        t()
        print(-5.2 % 2)
        do_n(t, n-1)


def printf_hello():
    print("hello")


do_n(printf_hello, 2)
