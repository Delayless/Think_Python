import turtle


# 多边形外角和等于360
# t:函数Turtle的对象     length:边长    n:外角
def polygon(t, length, n):
    angle = 360 / n  # 没必要放到for循环里
    for i in range(n):
        t.fd(length)
        t.lt(angle)


bob = turtle.Turtle()
for j in range(5):
    polygon(bob, float(input("Please input length:")),
            int(input("Please input n-sided:")))
turtle.done()
