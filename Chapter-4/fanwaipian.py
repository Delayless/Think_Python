import turtle


# 多边形外角和等于360
# t:函数Turtle的对象     length:边长
# n:外角      angle:圆弧的圆心角
def polygon(t, h, length, n, angle):
    # 因为现在还没学判断语句，所以分成两个for循环
    exterior_angle = 360 / n
    m = int(angle/360 * n)
    t.pd()
    for i in range(m):
        t.fd(length)
        t.lt(exterior_angle)
    for j in range(n-m):
        t.fd(length)
        h.fd(length)
        t.lt(exterior_angle)
        h.lt(exterior_angle)
    for k in range(m):
        h.fd(length)
        h.lt(exterior_angle)


bob = turtle.Turtle()
truce = turtle.Turtle()
polygon(bob, truce, length=2, n=150, angle=120)
turtle.done()
