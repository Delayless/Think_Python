import turtle
import math


def arc(t, r, angle):
    """
    :param t: Turtle
    :param r: radius
    :param angle:圆心角Central angle
    :return: 无返回值
    """
    circumference = 2 * math.pi * r  # 周长
    # n越大速度越快,但是精度越低
    n = int(circumference / 50) + 1  # 根据周长选择不同的多边形逼近
    arc_length = circumference * (angle / 360)  # 弧长
    step_length = arc_length / n
    step_angle = angle / n

    t.lt(step_angle / 2)  # 转过一点角度,再前进能够更好的逼近圆弧

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

    t.rt(step_angle / 2)  # 转回来


def petal(t, r, angle):
    """Draws a petal using two arc
        一叶花瓣
    """
    for j in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)  # 花瓣两条弧对应的圆心角可以组成平行四边形,内错角互补
        # 画完之后可以回到原来的位置


def flower(t, petal_num):
    """
    :param t: Turtle
    :param petal_num: 花瓣数目
    """
    # 以下两个参数我都是大概逼近一些这个规律,具体的算法我暂时没解决
    angle = 20 + 360 / petal_num     # 花瓣越多,圆弧所对圆心角越小,即圆弧半径与花瓣数成反比
    r = 30 + petal_num * 2        # 花瓣越多,圆弧半径越大,即圆弧半径与花瓣数成正比
    for k in range(petal_num):
        petal(t, r, angle)
        t.lt(360 / petal_num)


bob = turtle.Turtle()
flower(bob, petal_num=7)
bob.hideturtle()
turtle.done()
