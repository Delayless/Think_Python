import turtle
import math
"""*************************************************************
important:math.sin()等用的是弧度而不是角度,所以要angle * math.pi/180
这个问题花了我很长的时间排查
****************************************************************
"""


def triangle(t, n, length):
    """
    画完之后Turtle朝向发生变化,指向另外一条腰
    所以只需循环就可以,无需再次手动转向
    """
    angle = 360 / n     # 中间被等分的角,即顶角
    bottom_angle = (180-angle) / 2    # 180 - (180-360/n) / 2化简
    print(angle)
    print(bottom_angle)
    # 正弦定理求底边长度
    bottom_length = math.sin(angle * math.pi / 180) * length / math.sin(bottom_angle  * math.pi / 180)
    # 余弦定理
    # bottom_length = math.sqrt(2*(length**2)*(1-math.cos(angle * math.pi / 180)))
    # 还可以过顶点像底边做一条垂直线作为辅助线,答案是这种方法,也挺好的
    for i in range(n):
        t.fd(length)         # 腰长
        t.lt(180 - bottom_angle)   # 底角的外角
        t.fd(bottom_length)  # 底边长
        t.lt(180 - bottom_angle)   # 底角的外角
        t.fd(length)         # 腰长
        t.lt(180)            # 掉头


bob = turtle.Turtle()
bob.speed(1)
triangle(bob, 5, 80)
bob.hideturtle()
turtle.done()
