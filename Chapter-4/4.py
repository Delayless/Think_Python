import turtle
bob = turtle.Turtle()
bob.pd()


def triangle():
    bob.fd(100)
    bob.lt(90)


for i in range(4):
    triangle()
turtle.done()
