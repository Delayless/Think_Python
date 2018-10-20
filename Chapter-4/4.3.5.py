import turtle


# 多边形外角和等于360
# t:函数Turtle的对象     length:边长
# n:外角      angle:圆弧的圆心角
def polygon(t, length, n, angle):
    # 因为现在还没学判断语句，所以分成两个for循环
    exterior_angle = 360 / n
    m = int(angle/360 * n)
    t.pd()
    for i in range(m):
        t.fd(length)
        t.lt(exterior_angle)
    # 把笔抬起来，把剩下的画完
    t.pu()
    for j in range(n-m):
        t.fd(length)
        t.lt(exterior_angle)


bob = turtle.Turtle()
print(bob)
for k in range(5):
    polygon(bob, 2, 30, 360)
    polygon(bob, 2, 60, 360)
    polygon(bob, 2, 90, 360)
    polygon(bob, 2, 120, 360)
    polygon(bob, 2, 150, 360)
    polygon(bob, float(input("Please input length:")),
            int(input("Please input n-sided:")), int(input('Please input angle:')))
turtle.done()
