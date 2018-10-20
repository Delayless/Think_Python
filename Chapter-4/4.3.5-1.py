import turtle
import math


def polygon(t, length, n, angle):
    """多边形外角和等于360
    t:函数Turtle的对象     length:边长
    n:将圆近似成n边形       angle:圆弧的圆心角
    我采用的方法是计算周长,走完angle/360个周长之后把笔抬起来继续走完这一圈
    而书上采用的方法是算出弧长然后只走过那么多弧度
    """
    # 因为现在还没学判断语句，所以分成两个for循环
    exterior_angle = 360 / n
    m = int(angle/360 * n)
    t.pd()
    for i in range(m):
        t.fd(length)
        t.lt(exterior_angle)
    # 把笔抬起来，把剩下的画完
    t.pu()
    for j in range(int(n - m)):
        t.fd(length)
        t.lt(exterior_angle)


def circle(p, r, angle):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / 100
    polygon(p, length, n, angle)


bob = turtle.Turtle()
circle(bob, 30, 120)
circle(bob, 60, 360)
circle(bob, 90, 360)
circle(bob, float(input("Please input circumference:")),
       int(input('Please input angle:')))
turtle.done()
