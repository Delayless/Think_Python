import turtle


def draw(t, length, n):
    if n == 0:
        return
    angle = 40
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


bob = turtle.Turtle()
draw(bob, 7, 6)
turtle.done()